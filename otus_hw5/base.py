# -*- coding: utf-8 -*-
from datetime import date


def table(cls):
    Base.__tables__.append(cls)
    return cls


class instancemethod(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, klass=None):
        def newfunc(*args):
            return self.f(obj, *args)
        return newfunc

# region Datatypes


class Field:
    def __init__(self, db_type, **options):
        self.name = ""
        self.type = db_type
        self.options = options

    def __eq__(self, other):
        self.where_stmt = "{}={}".format(self.name, other)
        return self

    def __gt__(self, other):
        self.where_stmt = "{}>{}".format(self.name, other)
        return self

    def __lt__(self, other):
        self.where_stmt = "{}<{}".format(self.name, other)
        return self


class Integer(Field):
    def __init__(self, primary_key=False, autoincrement=False):
        super().__init__("integer", primary_key=primary_key, autoincrement=autoincrement)


class Boolean(Field):
    def __init__(self, **options):
        super().__init__("integer", **options)


class String(Field):
    def __init__(self, default="NULL"):
        super().__init__("text", default=default)

    def __eq__(self, other):
        self.where_stmt = "{}='{}'".format(self.name, other)
        return self

    def __gt__(self, other):
        self.where_stmt = "{}>'{}'".format(self.name, other)
        return self

    def __lt__(self, other):
        self.where_stmt = "{}<'{}'".format(self.name, other)
        return self


class Real(Field):
    def __init__(self, **options):
        super().__init__("real", **options)


class Blob(Field):
    def __init__(self, **options):
        super().__init__("blob", **options)


class Date(Field):
    def __init__(self, **options):
        super().__init__("text", **options)

# endregion


def get_fields_from_class(cls):
    return [attr for _class in reversed(cls.mro())
            for attr in _class.__dict__.keys()
            if issubclass(type(getattr(cls, attr)), Field)]


class Query:
    def __init__(self, statement):
        self._stmt = statement

    def where(self, *args):
        self._stmt += "WHERE " + " AND ".join([arg.where_stmt for arg in args])
        return self

    def all(self):
        print(self._stmt)


class Selector:
    def __call__(self, cls, *args):
        _stmt = "SELECT {}"
        fields = get_fields_from_class(cls)
        for field in fields:
            field_obj = getattr(cls, field)
            field_obj.name = field
        columns = ", ".join([arg.name for arg in args])
        _stmt = _stmt.format(columns)
        _stmt += " FROM {} ".format(cls.__tablename__ or cls.__name__.lower())
        return Query(_stmt)


class Updater:
    def __call__(self, instance):
        _stmt = "UPDATE {}"
        _inst = instance
        fields = get_fields_from_class(_inst.__class__)
        columns = ", ".join(["{}={}".format(field, getattr(_inst, field)) for field in fields if
                                     not isinstance(getattr(_inst, field), (str, date))])
        columns += ", " + ", ".join(["{}='{}'".format(field, getattr(_inst, field)) for field in fields if
                                     isinstance(getattr(_inst, field), (str, date))])
        _stmt = _stmt.format(_inst.__tablename__ or _inst.__class__.__name__.lower())
        _stmt += " SET {}".format(columns)
        _stmt += " WHERE id={}".format(_inst.id)
        print(_stmt)


class Base:
    __tables__ = []
    __tablename__ = None

    def __init__(self, *args, **kwargs):
        self.__table = self.__class__.__name__

        self.__fields = get_fields_from_class(self.__class__)

        for field in self.__fields:
            self.__dict__.setdefault(field, kwargs[field])

    @classmethod
    def create_table(cls):
        def prepare_fields():
            result = ""

            fields = get_fields_from_class(cls)

            for field in fields:
                datatype = getattr(getattr(cls, field), "type")
                options = getattr(getattr(cls, field), "options")
                options = [k for k in options.items()]
                result += " {} {}".format(field, datatype)
                for option in options:
                    if isinstance(option[1], bool):
                        if option[1]:
                            result += " {}".format(option[0].replace("_", " "))
                    else:
                        result += " {} {}".format(option[0].replace("_", " "), option[1])
                result += ",\n"

            return result

        tablename = cls.__tablename__ or cls.__name__.lower()
        stmt = "CREATE TABLE {0} \n({1})".format(tablename, prepare_fields())
        print(stmt)

    @classmethod
    def create_all(cls):
        for table in cls.__tables__:
            table.create_table()

    select = classmethod(Selector())
    update = instancemethod(Updater())


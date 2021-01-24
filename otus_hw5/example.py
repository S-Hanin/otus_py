# -*- coding:utf-8 -*-
from datetime import date

from base import table
from base import Base, Integer, String, Date, Boolean


@table
class User(Base):
    id = Integer(primary_key=True)
    name = String()
    birthdate = Date()


@table
class Admin(User):
    __tablename__ = "admins"

    admin = Boolean()


def main():
    def echo(item):
        print(item.id)
        print(item.name)
        print(item.birthdate)
        print("-"*80)

    user1 = User(id=1, name="John", birthdate=date(1984, 10, 8))
    user2 = User(id=2, name="Julia", birthdate=date(1985, 5, 11))
    echo(user1)
    echo(user2)
    echo(user1)
    admin1 = Admin(id=1, name="John", birthdate=date(1984, 10, 8), admin=True)
    echo(admin1)
    # User.create_table()
    Base.create_all()

    User.select(User.id, User.name).where(User.id > 1, User.name == "John").all()
    User.select(User.id, User.name).where(User.id > 2, User.name == "Julia").all()
    user1.update()
    user2.update()


if __name__ == "__main__":
    main()

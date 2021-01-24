# -*- coding: utf8 -*-
import json
from collections import UserDict

from config import db
from models import Good, Image


class JSDict(UserDict):
    def __getattr__(self, item):
        return self[item]

    @staticmethod
    def from_dict(other_dict):
        result = JSDict()
        for k, v in other_dict.items():
            result[k] = v
        return result


def create_good_record(name, description, price):
    good = Good()
    good.name = name
    good.description = description
    good.price = price
    return good


def create_image_record(good, path):
    img = Image()
    img.path = path
    img.good = good
    return img


def main():
    with open("test_goods.json") as fh:
        goods = json.load(fh)

    for good in goods:
        good = JSDict.from_dict(good)
        good_rec = Good(name=good.name, description=good.description, price=good.price)
        for img in good.images:
            img = JSDict.from_dict(img)
            img_rec = Image(path=img.path, good=good_rec)
            db.session.add(img_rec)
        db.session.add(good_rec)
        db.session.commit()


if __name__ == "__main__":
    main()

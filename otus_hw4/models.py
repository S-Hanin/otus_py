# -*- coding: utf8 -*-

from config import db


class Good(db.Model):
    __tablename__ = "goods"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    images = db.relationship("Image", back_populates="good")


class Image(db.Model):
    __tablename__ = "good_img"

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String)
    good_id = db.Column(db.Integer, db.ForeignKey('goods.id'))
    good = db.relationship("Good", back_populates="images")


def main():
    db.create_all()


if __name__ == "__main__":
    main()

# -*- coding: utf8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///otus_hw4.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def main():
    pass


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-

from flask import render_template

from config import app
from models import Good


@app.route('/')
def goods_list():
    return render_template("goods_list.html", goods=Good.query.all())


@app.route('/<int:good_id>/')
def good_description(good_id):
    return render_template("good.html", good=Good.query.filter(Good.id == good_id))


if __name__ == '__main__':
    app.run(debug=True)

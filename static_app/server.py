#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: 布丁(dingweihuaic@126.com)
#
# Created: 2018/3/13 下午1:51

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    data = 'Hello, World'
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

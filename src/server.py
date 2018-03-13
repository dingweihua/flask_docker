#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: 布丁(dingweihuaic@126.com)
#
# Created: 2018/3/13 上午10:13

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

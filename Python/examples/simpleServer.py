#!/usr/bin/env python3
from bottle import route, run, template
from serverFunctions import misc

@route('/')
def root():
    return misc.root()


@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)

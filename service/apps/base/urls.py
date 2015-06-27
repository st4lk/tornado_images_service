# coding: utf-8
from .handlers import HomeHandler
from tornado.web import url

patterns = [
    url(r'/', HomeHandler, name="home"),
]

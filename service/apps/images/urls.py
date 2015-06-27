# coding: utf-8
from .handlers import ImageHandler
from tornado.web import url

patterns = [
    url(r'/api/images', ImageHandler, name="images"),
]

# -*- coding: utf-8 -*-
import tornado.web


class ImageHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("TODO")

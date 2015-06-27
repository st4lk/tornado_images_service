import os
import tornado.httpserver
import tornado.ioloop
from tornado.options import options
from service.app import Application
from service.urls import patterns
from service.settings import settings


def main():
    application = Application(patterns, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", options.port))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

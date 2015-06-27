from tornado.escape import json_encode


class JSONResponseMixin(object):
    def respond_json(self, data, status=200):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json_encode(data))

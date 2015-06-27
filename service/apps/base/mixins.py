from tornado.escape import json_encode


class JSONResponseMixin(object):
    def set_default_headers(self):
        super(JSONResponseMixin, self).set_default_headers()
        self.set_header("Content-Type", "application/json; charset=UTF-8")

    def respond_json(self, data, status=200):
        self.write(json_encode(data))

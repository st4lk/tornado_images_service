# -*- coding: utf-8 -*-
import uuid
import tornado.web
from tornado import gen
from service.apps.base.mixins import JSONResponseMixin
from .s3 import AmazonS3Mixin


class ImageHandler(AmazonS3Mixin, JSONResponseMixin, tornado.web.RequestHandler):
    @gen.coroutine
    def post(self):
        if 'image' not in self.request.files:
            self.respond_json({'error': "No image is specified"}, 400)
            return
        success = True
        bucket = yield self.get_bucket()
        for image in self.request.files['image']:
            result = yield self.upload_file_s3(bucket, str(uuid.uuid4()), image.body,
                {'Content-Type': image['content_type']})
            if result.status != 200:
                success = False
                break
        if success:
            self.respond_json({'result': 'ok'})
        else:
            self.respond_json({'result': 'fail'}, 400)

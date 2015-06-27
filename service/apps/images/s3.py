import logging
from tornado import gen
from botornado.s3.connection import AsyncS3Connection
from botornado.s3.key import AsyncKey

l = logging.getLogger(__name__)


class AmazonS3Mixin(object):

    @gen.coroutine
    def get_bucket(self, bucket_name=None):
        conn = AsyncS3Connection(aws_access_key_id=self.settings['aws_key'],
                            aws_secret_access_key=self.settings['aws_secret'])
        bucket = yield gen.Task(conn.get_bucket, bucket_name or self.settings['s3_bucket'])
        raise gen.Return(bucket)

    @gen.coroutine
    def upload_file_s3(self, bucket, name, content, meta=None, public=True):
        k = AsyncKey(bucket)
        k.key = name
        if meta:
            for meta_key, meta_value in meta.iteritems():
                k.set_metadata(meta_key, meta_value)
        params = {}
        if public:
            params['policy'] = 'public-read'
        result = yield gen.Task(k.set_contents_from_string, content, **params)
        l.info(u"Amazon S3: {0}".format(
            k.generate_url(expires_in=0, query_auth=False, force_http=True)))
        raise gen.Return(result)

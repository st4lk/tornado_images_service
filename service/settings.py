import os
import tornado
from tornado.options import define, options


BASE_DIR = os.path.dirname(__file__)

define("port", default=5000, help="run on the given port", type=int)
define("debug", default=False, help="debug mode", type=bool)
define("s3_bucket", default="bucketfortestprojects")
define("aws_key", default=None)
define("aws_secret", default=None)

tornado.options.parse_command_line()

settings = {
    'debug': options.debug,
    'template_path': os.path.join(BASE_DIR, 'templates'),
    's3_bucket': os.environ.get('S3_BUCKET', options.s3_bucket),
    'aws_key': os.environ.get('AWS_ACCESS_KEY', options.aws_key),
    'aws_secret': os.environ.get('AWS_SECRET_KEY', options.aws_secret),
}

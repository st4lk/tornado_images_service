import os
import tornado
from tornado.options import define, options


BASE_DIR = os.path.dirname(__file__)

define("port", default=5000, help="run on the given port", type=int)
define("debug", default=False, help="debug mode", type=bool)

tornado.options.parse_command_line()

settings = {
    'debug': options.debug,
    'template_path': os.path.join(BASE_DIR, 'templates'),
}

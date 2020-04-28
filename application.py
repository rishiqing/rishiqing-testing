import platform

import tornado.ioloop
import tornado.web

from web.testingHandler import TestingHandler

"""
web server application entry
use tornado
"""
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("rishiqing automated testing server")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/autoTesting", TestingHandler)
    ], debug=True)


if __name__ == "__main__":
    if platform.system() == "Windows":
        import asyncio
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = make_app()
    app.listen(8848)
    tornado.ioloop.IOLoop.current().start()
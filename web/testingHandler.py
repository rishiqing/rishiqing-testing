import tornado.web

from framework.assemlby.uitest import test_all


class TestingHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        test_all()
        self.write({'message': 'success'})
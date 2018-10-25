import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""

    def get(self):

        self.write("hello wolfcode")


if __name__ == '__main__':
    app = tornado.web.Application([(r"/",IndexHandler)])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
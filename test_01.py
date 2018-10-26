import tornado.web
import tornado.ioloop
import tornado.options

class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""

    def get(self):

        

        self.write("hello wolfcode")




if __name__ == '__main__':
    #添加下面这条语句的话,会转换 启动时候,会转换那些在给模块传递的参数,
    #举例,python manage -h cc -b ff 这些.
    tornado.options.parse_command_line()

    #开启debug模式
    app = tornado.web.Application([(r"/",IndexHandler)],debug=True)
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
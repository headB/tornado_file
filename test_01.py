import tornado.web
import tornado.ioloop
import tornado.options
#如果要手动启动多进程的话,需要外部引入其他的模块
import tornado.httpserver

tornado.options.define("port",default=8000,type=int,help="what the help you talk about?")


class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""

    def get(self):

        self.write("hello wolfcode")


class EchoInfo(tornado.web.RequestHandler):

    def post(self):

        self.write("I am the Kumanxuan")




if __name__ == '__main__':
    #添加下面这条语句的话,会转换 启动时候,会转换那些在给模块传递的参数,
    #举例,python manage -h cc -b ff 这些.
    tornado.options.parse_command_line()
    # tornado.options.parse_config_file("config.py")
    
    


    #开启debug模式
    #app = tornado.web.Application([(r"/",IndexHandler)],debug=True)
    #注意了,关于如果开启多进程的时候,记得一定需要把debug模式关掉,不然就出现问题.
    app = tornado.web.Application([(r"/",IndexHandler),(r"/li",EchoInfo)],debug=True)
    #app.listen(tornado.options.options.port)

    #下面这些是多进程的代码部分==========开始================
    # http_server = tornado.httpserver.HTTPServer(app)
    # http_server.bind(8090)
    # http_server.start(0)

    #下面这些是多进程的代码部分==========结束=================

    #普通的单线程部分==========开始=============
    app.listen(8060)
    #========================结束=============


    tornado.ioloop.IOLoop.current().start()
    

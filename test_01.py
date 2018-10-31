import tornado.web
from tornado.web import url,RequestHandler
import tornado.ioloop
import tornado.options
#如果要手动启动多进程的话,需要外部引入其他的模块
import tornado.httpserver
#添加日志功能
from tornado.options import parse_command_line,options
#options.logging = None
parse_command_line()

tornado.options.define("port",default=8000,type=int,help="what the help you talk about?")


def function1():

    x1 = 1
    x2 = 2

    if x1 == 1:
        raise NameError("you have fail")

    return "xx"



class IndexHandler(RequestHandler):
    """主页处理类"""

    def get(self):
        
        try:
            # function1()
            # 1 / 0 
            values1 = self.get_query_argument("name",strip=True)

        except (NameError) as e:
            print(e)
            self.write("发生错误,可能是因为缺少name参数,get方式的")

        except Exception:
            self.write("发生其他错误!")
    
        else:
            self.write("hello wolfcode")
        finally:
            self.write("我是最后的最后!")


class EchoInfo(RequestHandler):

    def post(self):

        try:
            values1 = self.get_arguments("name",strip=True)
        except Exception as e:
            self.write("缺少关键字name的数值")

        else:
            print(values1)
            self.write("hello wolfcode")
        finally:
            self.write("我是最后的最后!")


#测试文件上传??
class uploadInfo(RequestHandler):

    #定义上传方法
    #post方法
    def post(self):
        images = self.request.files
        images_info = images.get("image")
        with open("image.png","wb") as file1:
            file1.write(images_info[0]["body"])

        self.write("OK")



if __name__ == '__main__':
    #添加下面这条语句的话,会转换 启动时候,会转换那些在给模块传递的参数,
    #举例,python manage -h cc -b ff 这些.
    tornado.options.parse_command_line()
    # tornado.options.parse_config_file("config.py")
    
    


    #开启debug模式
    #app = tornado.web.Application([(r"/",IndexHandler)],debug=True)
    #注意了,关于如果开启多进程的时候,记得一定需要把debug模式关掉,不然就出现问题.
    app = tornado.web.Application([
        (r"/",IndexHandler),
        (r"/li",EchoInfo),
        url(r"/kumanxuan",EchoInfo,name="testUrl"),
        url(r"/upload",uploadInfo,name="upload"),
        
        ],debug=True)
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
    

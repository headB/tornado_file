import tornado.web
from tornado.web import url,RequestHandler,StaticFileHandler,Application
import tornado.ioloop
import tornado.options
#如果要手动启动多进程的话,需要外部引入其他的模块
import tornado.httpserver
#添加日志功能
from tornado.options import parse_command_line,options
#options.logging = None
parse_command_line()
import os
#os sys
#稍微想一下他们的区别


#开始操作数据库
import torndb


current_path = os.path.dirname(__file__)

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

#测试提取uri
class testUri(RequestHandler):

    #这里定义get方法,好像django的,看起来挺习惯的!
    def get(self,name,age):
        self.write(" first is %s, the second is %s" %(name,age))


#测试模板
class testTemplates(RequestHandler):

    def get(self):

        #尝试快速穿件一个生成式

        numbers = [ x for x in range(5)]

        #传递反向姐系url地址
        url = self.reverse_url("testUrl")

        info = {
            "url":url,
            "name":"beelte",
            "age":'18',
            "numbers":numbers,
        }


        self.render("info.html",**info)


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


#测试json是否自动转换
class testJson(RequestHandler):

    def get(self):

        #测试跳转
        url = self.get_query_argument("url",None,strip=True)
        
        print(url)
        print(type(url))
        if url == None:

            self.redirect("https://www.baidu.com")

        else:
            #设置字典
            dict_content = {
                "name":"lizhixuan",
                "age":"18"
            }

            self.set_header("name","kumanxuan")
            self.set_status(211)
            
            self.write(dict_content)


#测试数据库
class testDB(RequestHandler):

    def get(self):

        request = self.get_query_argument("req",None,strip=True)

        if request == "insert":

            info = self.application.db.execute("insert into houses(`title`) values('cctv')")
            info1 = self.application.db.execute_rowcount("insert into houses(`title`) values('cctv')")

            print(info)
            print(info1)

            self.write("sucess!")
        
        else:

            info = self.application.db.query("select * from houses")

            print(info)
            
            self.write("hello world!")

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
        (r"/testdb",testDB),
        url(r"/kumanxuan",EchoInfo,name="testUrl"),
        url(r"/upload",uploadInfo,name="upload"),
        url(r"/template",testTemplates,name="template"),
        url(r"/detail/(.+)/(\d+)",testUri,name='testUri'),
        url(r"/detail/(?P<age>\d+)/(?P<name>.+)",testUri,name='testUri1'),
        url(r"/json",testJson,name='json'),
        (r'^/view/(.*)$', StaticFileHandler, {"path":os.path.join(current_path, "statics"),"default_filename":"info.html"}),
        ],debug=True,
        static_path=os.path.join(os.path.dirname(__file__),"statics"),
        template_path=os.path.join(os.path.dirname(__file__),"templates"),
        )

    app.db = torndb.Connection(
            host="127.0.0.1",
            database="itcast",
            user="root",
            password="kumanxuan@gzitcast"
        )

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
    

# hello, world
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class RootRequestHandler(RequestHandler):
    def get(self):
        self.write("Hi")


if __name__ == "__main__":
    app = Application([
        (r"/", RootRequestHandler)
    ])

    port = 8881
    app.listen(port)
    print(f"hi, we are listening on port {port}")
    IOLoop.current().start()



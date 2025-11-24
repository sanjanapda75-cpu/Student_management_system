
class myhandler(simpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/':
            self.path='index.html'
        return super().do_GET()

if _name_=="_main_":
server=htttpserver(('localhost', 8000), myhandler)
print("serving on http://localhost:8000")
server.serve_forever()

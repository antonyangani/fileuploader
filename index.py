import tornado.web
import tornado.ioloop
import io 
import socket

hostname = socket.gethostname()
server_ip = socket.gethostbyname( hostname )

# This method is for creating custom html files and adds in the URL to the video file that was just created

class createHTML():
    def create_file(self, name, video_url):
        with io.open('template/video.html', 'r', encoding='utf8') as f:
            content = f.read()
            content = content.replace('EnterURL', f"{video_url}")
            with io.open(f"shipping/{name}.html", "w", encoding='utf8') as d:
                video_page = d.writelines(content)
        return video_page

class uploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        files = self.request.files["imgFile"]
        server_ip_data = server_ip
        for f in files:
            # The file upload process 
            filehandler = open(f"img/{f.filename}", "wb")
            filehandler.write(f.body)
            filehandler.close()
            url = f"http://{server_ip}:8000/img/{f.filename}"
            
            c = createHTML()
            con = c.create_file(f.filename, url)

        self.write(f"<a href='{url}'>Link to Pic</a>")
        
        



if __name__ == "__main__":
    app = tornado.web.Application([
        ("/img/(.*)", tornado.web.StaticFileHandler, {"path" : "img"}),
        ("/", uploadHandler)
    ])
    app.listen(8000)
    print("App is listening on 8000 ... ")

    tornado.ioloop.IOLoop.instance().start()

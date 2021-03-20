import tornado.web
import tornado.ioloop
import io 


class createHTML():
    def create_file(self, name, video_url):
        with io.open('template/video.html', 'r', encoding='utf8') as f:
            content = f.read()
            content = content.replace('EnterURL', f"{video_url}")
            with io.open(f"shipping/{name}.html", "w", encoding='utf8') as d:
                video_page = d.writelines(content)
                # video_page = f.writelines(content.encode('utf-8', 'ignore'))
        return video_page

class uploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        files = self.request.files["imgFile"]
        for f in files:
            # The file upload process 
            filehandler = open(f"img/{f.filename}", "wb")
            filehandler.write(f.body)
            filehandler.close()
            url = f"http://localhost:8000/img/{f.filename}"
            
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

# Why 

- This project is to help Angani streamline it's video uploading process
- Under the hood, it is a python project that allows for the uploading of a file and moving it to a shared storage area

# How to use it
- It has two important directories that need to be mounted onto the video streamer
- /data/static-html
- /data/media

example

-- docker run -dit -p 8000:8000 --name APP_NAME -v ~/data:/data/img groctech/video-uploader:latest

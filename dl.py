from youtube_dl import YoutubeDL

video_downloader = YoutubeDL({'format':'best'})
audio_downloader = YoutubeDL({'format':'bestaudio'})

# def video(link):
  
#     vid =	video_downloader.extract_info(link,download =	False)
#     aud = audio_downloader.extract_info(link,download =	False)
#     return vid['url'],vid['description'],vid['title'],vid['thumbnail'], vid['like_count'],vid['dislike_count'],aud['url']

class downloader:
    def __init__(self,link):
        self.link = link
        self.vid_info = video_downloader.extract_info(self.link,download =	False)
        self.video_url = self.vid_info['url']
        self.vid_description = self.vid_info['description']
        self.vid_title = self.vid_info['title']
        self.vid_thumb = self.vid_info['thumbnail']
        self.likes = self.vid_info['like_count']
        self.unlikes = self.vid_info['dislike_count']
        self.aud_info = audio_downloader.extract_info(self.link,download =	False)
        self.audio_url = self.aud_info['url']

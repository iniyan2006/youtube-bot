from dl import downloader
from pyrogram import Client, filters, emoji
import pafy
from utils import settings
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
# instans for utils
msg_settings = settings()
app = Client('yt_bot',
             config_file='config.ini',
             parse_mode='html'
          )
#markup for audio and video

#start command 
@app.on_message(filters.command(['start']))
def start_command(client,message):
  start_message = f"""
        hello {emoji.SPARKLES} {message.from_user.first_name} {emoji.SPARKLES}
        This  bot will download youtube videos through links.
        just send me a valid video link I will send the video
        """
  message.reply_text(
    start_message
     )

#thumbnail command
@app.on_message(filters.command(['thumb']))
def thumb(client,message):
  url = str(message.text).split()
  print(url)
  print(url[1])
  img_dl = pafy.new(url[1])
  message.reply_photo(img_dl.bigthumb)
#description command
@app.on_message(filters.command(['des']))
def description(client, message):
  link = str(message.text).split()
  url = downloader(link[1])
  message.reply_text(url.vid_description)
#filters private messages
@app.on_message(filters.private)
def sending(client,message):
  if   "youtube" or "youtu.be" in message.text:
    pass
  try:
  
    response =  message.reply("please wait downloading...")
    img = pafy.new(message.text)
    info = downloader(message.text)    

    audio_video_link = InlineKeyboardMarkup(
    [
      [
        InlineKeyboardButton(f"Video {emoji.FILM_FRAMES} ", url= info.video_url ),
        InlineKeyboardButton(f"Audio {emoji.HEADPHONE} ", url= info.audio_url )

      ]
    ] 
    )        
    
    response.edit_text("uploading...")
    upload_sticker = message.reply_sticker(msg_settings.sticker)
    message.reply_photo(img.bigthumb,
      caption =     f""" 
          <b>Title</b> :  {info.vid_title} +
        <b>Like count</b> {emoji.THUMBS_UP} : {info.likes} 
        <b>Dislike count</b> {emoji.THUMBS_DOWN}  : {info.unlikes} 
        <b><i>Video link</i></b> {emoji.FILM_FRAMES}	:  {emoji.DOWN_ARROW} <a href=\"{info.video_url}\">click here to download</a>
        <b><i>Audio link</i></b> {emoji.HEADPHONE} : {emoji.DOWN_ARROW} <a href=\"{info.audio_url}\">click here to download</a>
          """,
      reply_markup = audio_video_link
      )
    response.edit_text("your content is loaded")
    upload_sticker.delete()
  except :
  
    response.edit_text(f'error ‼️ downloading the video\n \tsend another link.. ‼️')
app.run()

from turtle import width
from PIL import Image, ImageDraw, ImageFont
import requests
import json
import tweepy

quoteFontStyle = ImageFont.truetype('Lato/Lato-Bold.ttf', 280)
authorFontStyle = ImageFont.truetype('Lato/Lato-Bold.ttf', 200)

api_key = ""
api_key_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def postDailyQuote():
    response = requests.get("https://zenquotes.io/api/today")
    quote_data = json.loads(response.text)
    quote = '"' + quote_data[0] ['q'] + '"'
    author = quote_data[0] ['a']


    template = Image.open('backgroundimage.jpeg')
    width, height = template.size
    image = ImageDraw.Draw(template)
    w, h = image.textsize(quote)
    image.text(((width - w)/2, (height - h)/2.5), quote, anchor="ms", fill="white", font=quoteFontStyle)
    image.text(((width - w)/2, (height - h)/1.5), author, anchor="ms", fill="white", font=authorFontStyle)
    template.save("backgroundimagewithtext.jpeg")

    api.update_status_with_media("#dailyquote #quote", "backgroundimagewithtext.jpeg")
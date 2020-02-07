#!/usr/bin/env python
import json
import telegram

#token that can be generated talking with @BotFather on telegram
with open('../../.telegram_token','r') as f:
    my_token = f.readline()
    print(my_token)

def send(msg, chat_id='@TWCDC', token=my_token):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)

with open("TWCDC.json","r",encoding="utf-8") as json_file:
    posts = json.load(json_file)
    posts = sorted(posts, key = lambda i: i['date'][0])
    timestamp = ""
    with open('timestamp','r') as t:
        timestamp = t.read()
    #print(timestamp)
    posts = [ post for post in posts if post['date'][0] > timestamp ]
    msg = ""
    for post in posts:
        if('text' in post):
            timestamp = post['date'][0]
            msg = post['source'][0] + '\n' + post['text'] + '\n日期: ' + post['date'][0] + '\n來源: ' + 'https://facebook.com/' + post['url']
            #msg = 'https://facebook.com/' + post['url']
            print(post['date'][0])
            send(msg)
            with open('timestamp','w') as t:
                t.write(post['date'][0])

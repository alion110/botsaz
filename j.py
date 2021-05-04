import asyncio
import time
import os
import asyncio
import threading
import random
from datetime import datetime
import pytz
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import pyromod.listen
api_id = 4109627
api_hash = '5874fe255bec03272faaa41ac22e55dc'
me = 1223702732
biochi = True
khar = []
chats = {}
app = Client("acountifyt", api_id, api_hash)
last = time.time()




async def bla(sec):
    await asyncio.sleep(sec)

@app.on_message(filters.reply & filters.regex("^([Ii]d)$")) #get id by replying on messages
async def id(client, message):
    if message.from_user.id == me: 
        ids = message.reply_to_message.from_user.id
        await client.edit_message_text(message.chat.id, message.message_id, f'`{ids}`')

@app.on_message(filters.me & filters.regex("^\/ping$"))
async def ping(client, message):
    await app.edit_message_text(message.chat.id, message.message_id, "┈┅┅━━━━✦━━━━┅┅┈\n             Im Online\n┈┅┅━━━━✦━━━━┅┅┈")

@app.on_message(filters.command(['setprofile', 'setprof'],['/','!','+','-',''])) #set telegram profile
async def setprofilephoto(client, message):
       if message.from_user.id == me: 
        try:
            gif = message.reply_to_message.video if message.reply_to_message.video else None
            photo = message.reply_to_message.photo if message.reply_to_message.photo else None
            if photo:
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس .**')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس ..**')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس ...**')
                await message.reply_to_message.download('profile.png')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس ..**')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس .**')
                await client.set_profile_photo(photo = 'downloads/profile.png')
                os.remove('downloads/profile.png')
                await client.edit_message_text(message.chat.id, message.message_id, '**پروفایل با موفقیت تنظیم شد 👁**')
                await bla(10)
                await app.delete_messages(message.chat.id, message.message_id)

            if gif: #it does not working right now :(
                await client.edit_message_text(message.chat.id, message.message_id, '**درحال دانلود گیف .**')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود گیف ..**')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود گیف ...**')
                await message.reply_to_message.download('profile.mp4')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود گیف ..**')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود گیف .**')
                await client.set_profile_photo(video = 'downloads/profile.mp4')
                os.remove('downloads/profile.mp4')
                await client.edit_message_text(message.chat.id, message.message_id, '**پروفایل با موفقیت تنظیم شد 👁**')
        except Exception as eljnskln:
            print(eljnskln)

@app.on_message(filters.command(['startbio', 'bio'],['/','!','+','-',''])) #Change Biography every 60 seconds !
async def strtbio(client, message):
    global biochi
    if message.from_user.id == me:
        try:
            emojies = ['🌵','🌱','🌾','🪐','☄️','✨','🔥','💥','🌪','🌟','🌎','🌙','🧘🏽‍♂️','🎧','🎤','🎸','🎮','🎯','♟','🎙','💣','⚔️','🗡','🔮','📿','💊','🧬','🖤']
            await app.edit_message_text(message.chat.id, message.message_id, '**تغییر خودکار بیو روشن شد✅**')
            while 1 == 1:
                rand = int(random.randint(0, 28))
                emo = emojies[rand]
                if biochi == False:
                    break
                await app.update_profile(first_name = 'Alion' ,bio=f"تاریخ یه فی البداهه اس{emo}")
                await bla(60)
        except:
            print('cant')
@app.on_message(filters.command(['stopbio', 'biooff'],['/','!','+','-',''])) #make off biography changer
async def stpbio(client, message):
    global biochi
    if message.from_user.id == me:
        biochi == False
        await app.edit_message_text(message.chat.id, message.message_id, '**تغییر خودکار بیو خاموش شد❗️**')

@app.on_message(filters.user(me) & filters.command(['tst', 'test'],['/','!','+','-',''])) #for test my codes !
async def test(client, message):
    answer = await client.listen(message.chat.id, filters.me)
    print(answer.message_id) 

@app.on_message(filters.me & filters.command(['download', 'save'],['/','!','+','-',''])) #Download files from telegram and save in local directory
async def downloader(client, message):
    video = message.reply_to_message.video if message.reply_to_message.video else None
    photo = message.reply_to_message.photo if message.reply_to_message.photo else None
    music = message.reply_to_message.audio if message.reply_to_message.audio else None
    text = message.reply_to_message.text if message.reply_to_message.text else None
    if video:
        await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
        await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
        await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
        await message.reply_to_message.download(f'{message.message_id}.mp4')
        await client.edit_message_text(message.chat.id, message.message_id, '**Downloaded !**')
        await bla(10)
        await app.delete_messages(message.chat.id, message.message_id)

    elif photo:
        await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
        await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
        await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
        await message.reply_to_message.download(f'{message.message_id}.png')
        await client.edit_message_text(message.chat.id, message.message_id, '**Downloaded !**')
        await bla(8)
        await app.delete_messages(message.chat.id, message.message_id)
    elif music:
        await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
        await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
        await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
        await message.reply_to_message.download(f'{message.message_id}.mp3')
        await client.edit_message_text(message.chat.id, message.message_id, '**Downloaded !**')
        await bla(8)
        await app.delete_messages(message.chat.id, message.message_id)
            
    else:
        whattosave = message.reply_to_message
        await whattosave.forward(me)
        await app.delete_messages(message.chat.id, message.message_id)

@app.on_message(filters.me & filters.command(['stick', 'photo', 'voice', 'audio'],['/','!','+','-',''])) #file converter :)
async def convertermessage(client, message):
    rp = message.reply_to_message
    if rp.sticker:
        print('got')
        try:
            await rp.download('files1.png')
            await client.send_photo(message.chat.id, 'downloads/files1.png', reply_to_message_id = rp.message_id)
            await app.delete_messages(message.chat.id, message.message_id)
            os.remove('downloads/files1.png')
        except Exception as ert:
            print(ert)
    if rp.photo:
        print('got')
        try:
            await rp.download('files2.webp')
            print('downloaded')
            await client.send_sticker(message.chat.id, 'downloads/files2.webp', reply_to_message_id = rp.message_id)
            print('sent')
            await app.delete_messages(message.chat.id, message.message_id)
            os.remove('downloads/files2.webp')
        except Exception as erti:
            print(erti)
    if rp.voice:
        print('got')
        try:
            await rp.download('files2.mp3')
            print('downloaded')
            await client.send_audio(message.chat.id, 'downloads/files2.mp3', reply_to_message_id = rp.message_id)
            print('sent')
            await app.delete_messages(message.chat.id, message.message_id)
            os.remove('downloads/files2.mp3')
        except Exception as erti:
            print(erti)
    if rp.audio:
        print('got')
        try:
            await rp.download('files2.ogg')
            print('downloaded')
            await client.send_voice(message.chat.id, 'downloads/files2.ogg', reply_to_message_id = rp.message_id)
            print('sent')
            await app.delete_messages(message.chat.id, message.message_id)
            os.remove('downloads/files2.ogg')
        except Exception as erti:
            print(erti)
@app.on_message(filters.me & filters.command(['load'], ['/','!','+','-','']))
async def loader(client, message):
    freete = '|'
    text111 = '███████████████████████████|'
    try:
        for i in text111:
            freete += i
            await client.edit_message_text(message.chat.id, message.message_id, freete)
        await client.edit_message_text(message.chat.id, message.message_id, f'{freete}\n                   **Completely Loaded !**')

    except Exception as mepiorejgerj:
        print(mepiorejgerj)



@app.on_message(filters.text)
async def youme(client, message):
    global khar , last
    callme = ['alion', 'Alion', 'الیون', 'علیون', 'علی یون', 'الی یون', 'علیکون']
    callmej = '**HEY :)**'
    sorena = ['sorena','Sorena', 'سورنا', 'علی سورنا', 'ناخدا جلال', 'nakohoda jelal','Nakhoda Jelal','پیچک','pichak']
    sorenaj = '**بریم سورنا گوش بدیم** 🦌🖤'
    putak = ['putak','Putak', 'پوتک','پیامبر','خودکشی','khodkoshi','changar', 'چنگار']
    putakj = '**بریم پوتک گوش بدیم** 🖤🤘🏿'
    pishro = ['pishro','Pishro', 'پیشرو', 'parvaz', 'rail','ریل ','قیلی ویلی', 'اثر منفی', 'چاقال']
    pishroj = '**بریم پیشرو گوش بدیم** 🤘🏿👁🙏🏾✍🏾🙇🏾‍♂️🌘🌪'
    #print(message)
    try : 
        if message.from_user.id == me: 
            #print(message)
            if message.text == '!re':   #idk really for what :(
                await message.reply_text('**ربات با موفقیت ریستارت شد ☄️**')
                await app.restart()
        else:    
            if message.from_user.id in khar:
                return
            if time.time()-last<6:
                return
            for i in callme:
                if i in message.text:
                    last = time.time()
                    await message.reply_text(callmej)
                    await bla(10)
            for i in sorena:
                if i in message.text:
                    last = time.time()
                    await message.reply_text(sorenaj)
                    await bla(10)
            for i in putak:
                if i in message.text:
                    last = time.time()
                    await message.reply_text(putakj)
                    await bla(10)
                    
            for i in pishro:
                if i in message.text:
                    last = time.time()
                    await message.reply_text(pishroj)
                    await bla(10)
    except Exception as r:
        print(r)
try:
    app.run()
except Exception as kol:
    print(kol)
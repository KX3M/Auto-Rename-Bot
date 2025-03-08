import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "29895250")
    API_HASH  = os.environ.get("API_HASH", "29ca1e2311efdf950eea03a6ae2bc8ee")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8092013853:AAFMWjbX7QDnHY8Rm85TcBWAxAnzQ9SxHFA") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","PyBotz")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://sanji:sanji@sanjibots2689.xxgs2.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/a8e6aef1e2e383e68e122-3f263288e18b91f679.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6076683960 6586630448').split()]
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'solo_leveling_tamil_arise').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002283909105"))
    PORT = int(os.environ.get("PORT", ""))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))
    # Assuming you need to load STRING_SESSION from an environment vari
    STRING_SESSION = os.getenv("STRING_SESSION", None)  # or some default value
    


class Txt(object):
    # part of text configuration
        
    START_TXT = """<i>Hey!! {} You 
 Yeah, you! This bot isn't just any rename bot—it's fast, powerful, and gets the job done! Rename files, change thumbnails, and even convert videos to files or vice versa. Oh, and did I mention custom thumbnails and captions? Yeah, it does that too! So, stop wasting time and start using it already!
</i>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ `[episode]` :- To Replace Episode Number
✓ `[quality]` :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S01[episode] [quality][Dual Audio] @PythonBotz</code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/PythonBotz'>PythonBotz</a>
    
<b>♻️ Bot Made By :</b> @PythonBotz"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🥺 joine Plz: @PythonBotz
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>My UPI - <code>atif@superyes</code></b> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Joine @PythonBotz To Help """






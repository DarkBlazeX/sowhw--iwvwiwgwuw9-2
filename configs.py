import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "21003274"))
  API_HASH = os.environ.get("API_HASH", "47bbfbda757efd499b84edffcbe2f269")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7215053201:AAFNTRDq4LHM5uCx29xQbWPy5Djk8H8xyFA")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "ZxFileStore_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002183710308"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "shrinkme.io")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "e04edae72e34268418d96d7190d598978ae20b91")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "7087809870"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://darkblaze9090:sEtcxpcR6BO02EnW@cluster0.vr1hlmm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002177283696")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002147668142"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/ZX_BHAI)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/ZX_BHAI)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""

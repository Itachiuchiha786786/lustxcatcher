class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6402009857"
    sudo_users = ["6402009857"]
    GROUP_ID = -1001992198513
    TOKEN = "7271611709:AAHfLc4cAEvk-tNFYvHniy60p2rZZt8Roe0"
    mongo_url = "mongodb+srv://levi:levi@cluster0.5nctdgf.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/7e5398823512d307128a3.jpg", "https://telegra.ph/file/c45dcb207d81e97cb4f6a.jpg", "https://telegra.ph/file/0bc6d65878e8300fbf0f8.jpg", "https://telegra.ph/file/0afb45203ff162ee7227b.jpg"]
    SUPPORT_CHAT = "+pmOzZ6tPbWxmZTg1"
    UPDATE_CHAT = "+pmOzZ6tPbWxmZTg1"
    BOT_USERNAME = "Seizetestbot"
    CHARA_CHANNEL_ID = -1002023474262
    api_id = "20457610"
    api_hash = "b7de0dfecd19375d3f84dbedaeb92537"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

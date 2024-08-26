class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6236734355"
    sudo_users = ["6236734355"]
    GROUP_ID = "-1002041586214"
    TOKEN = "7164182815:AAEBBXi4yrw0Rg5tVkFxnK3exxL8wFNum7I"
    mongo_url = "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/7e5398823512d307128a3.jpg", "https://telegra.ph/file/c45dcb207d81e97cb4f6a.jpg", "https://telegra.ph/file/0bc6d65878e8300fbf0f8.jpg", "https://telegra.ph/file/0afb45203ff162ee7227b.jpg"]
    SUPPORT_CHAT = "jajaj"
    UPDATE_CHAT = "hsisjs"
    BOT_USERNAME = "Landlelebrobot"
    CHARA_CHANNEL_ID = "-1002023474262"
    api_id = "20457610"
    api_hash = "b7de0dfecd19375d3f84dbedaeb92537"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

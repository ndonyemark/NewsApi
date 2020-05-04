class Config:

   
    # print(NEWS_API_BASE_URL)

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True
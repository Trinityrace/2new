# | 

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL=('http://newsapi.org/v2/top-headlines?''apiKey=cdd57f0bbd8840fc9ccf8c6718290746')
    # pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
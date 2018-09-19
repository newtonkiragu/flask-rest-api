'''Set up environment specific configurations'''
import os


class Config(object):
    '''Parent configuration class'''
    DEBUG = False
    CSRF_ENABLED = True

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

class Testing(Config):
    '''Configuration for testing'''
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    """Configuration for Staging."""
    DEBUG = False


class Production(Config):
    '''Configuration for production'''
    DEBUG = False
    TESTING = False


config_options = {
    'development': DevConfig,
    'testing': Testing,
    'staging' : StagingConfig,
    'production': Production
}
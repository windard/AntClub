# coding=utf-8

from config.default import DevelopmentConfig
from config.test import TestingConfig

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

try:
    from config.production import ProductionConfig
    config.update(production=ProductionConfig)
except:
    pass
    
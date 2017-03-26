# coding=utf-8

from config.default import DevelopmentConfig
from config.test import TestingConfig
from config.production import ProductionConfig

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

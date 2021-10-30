import os
import json
import pandas as pd
from .helper import DictToObject

class Config:
    _instance = None
    _settings = None
    def __init__(self):
        self.makeSingleton()

    def makeSingleton(self):
        if Config._instance is not None:
            return Config._instance
        Config._instance = self
        self.getConfig()
        self.overrideConfigFromCmd()

    def getConfig(self, configPath="../config.json" ):
        if Config._instance._settings is None:
            settings = pd.read_json(configPath).to_dict()
            settings['env'] = settings["settings"]["environments"][settings["settings"]["default_env"]] #set env/browser params from the config
            settings["settings"]["browser"]["default_browser_profile"] = settings["settings"]["browser_profiles"][settings["settings"]["browser"]["default_browser_profile"]]
            settings['browser'] = settings["settings"]["browser"]
            Config._instance._settings = DictToObject(settings) #shorter syntax: settings.browser.default_browser_profile
        return Config._instance._settings

    @staticmethod
    def overrideConfigFromCmd(): #override default config from runtime -> span different browsers/envs/profiles
        if os.environ.get('UPDATE_JSON_SETTINGS') is not None:
            Config._instance._settings = DictToObject(json.loads(os.environ.get('UPDATE_JSON_SETTINGS')))






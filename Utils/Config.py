import json
from sys import settrace

class Config:
    def create_config():
        settings = {
            "Gems": 0,
            "Gold": 0,
            "Tickets": 0,
            "Starpoints": 0,
            "BrawlBoxTokens": 0,
            "BigBoxTokens": 0,
            "Trophies": 0,
            "BrawlerTrophies": 0,
            "BrawlerTrophiesForRank": 0,
            "BrawlerPowerLevel": 8,
            "BrawlerUpgradePoints": 0,
            "ShowPacketsInLog": False,
            "Maintenance": False,
            "Patch": False,
            "PatchUrl": "",
            "UpdateUrl": ""
        }

        with open('config.json', 'w') as config_file:
            json.dump(settings, config_file)
    
    def GetValue():
        config_settings = {}

        Config_file = open('config.json', 'r')
        config_values = Config_file.read()

        config_settings = json.loads(config_values)
        return config_settings
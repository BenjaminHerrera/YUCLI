from kivy.config import Config

Config.set('kivy', 'log_level', 'critical')

from yucli import console

Config.set('kivy', 'log_level', 'warning')
Config.write()
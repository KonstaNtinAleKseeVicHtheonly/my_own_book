from dataclasses import dataclass

from environs import Env

@dataclass
class TgBot:
    token:str 

@dataclass
class Config:
    my_bot: TgBot


def load_config(path=None)-> Config:
    env = Env()
    env.read_env(path)
    return Config(my_bot=TgBot(token=env('BOT_TOKEN')))


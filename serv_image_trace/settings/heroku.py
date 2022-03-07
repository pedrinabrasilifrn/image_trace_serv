#Carrega a biblioteca django enviroment
import environ

#Importa tudo que está presente no arquivo base
from serv_image_trace.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db(),
}
from email.mime import base
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = os.environ.get("SECRET_KEY") or "K<N>D'MSn!os@d0_@23u*`hue&%@`K*(JJH#@DS@&@@=+L@9WDdsd!@ie`>?<DPW:WD<>WDW"
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
    "sqlite:///" + os.path.join(basedir, "app.db")
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  
  MAIL_SERVER = "smtp.googlemail.com"
  MAIL_PORT = 587
  MAIL_USE_TLS = 1
  MAIL_USERNAME = "ikromshi"
  #MAIL_PASSWORD = "FallBreak123"
  MAIL_PASSWORD = "olulcaybigpkefcu"
  ADMINS = ['bozzocil@gmail.com']


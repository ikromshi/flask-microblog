from email.mime import base
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = os.environ.get("SECRET_KEY") or "K<N>D'MSn!os@d0_@23u*`hue&%@`K*(JJH#@DS@&@@=+L@9WDdsd!@ie`>?<DPW:WD<>WDW"
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///" + os.path.join(basedir, "app.db")
  SQLALCHEMY_TRACK_MODIFICATIONS = False
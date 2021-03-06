import os, os.path as p
import dotenv
import uuid


dotenv.load_dotenv(p.join(p.dirname(__file__), ".env"))


class Development:
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", uuid.uuid4().hex)


class Production(Development):
    DEBUG = False

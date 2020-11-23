import os
import json
import shutil
import uuid

from flask import abort
from database import base
from database.config import dev


RESOURCE_DIR = "./SERVER_DATA"
SECRETS_PATH = "./secret.json"


def validate(access_token):
    global ACCESS_TOKEN
    if access_token != ACCESS_TOKEN:
        abort(401, "Call Requires Authentication")


def load_access_token(path):
    if os.path.exists(SECRETS_PATH):
        with open(path, 'r') as f:
            secret = json.load(f)
            if "access_token" in secret:
                return secret["access_token"]
    return ""


ACCESS_TOKEN = load_access_token(SECRETS_PATH)


def main():
    global ACCESS_TOKEN, RESOURCE_DIR, SECRETS_PATH
    if not os.path.exists(dev.SQLALCHEMY_DATABASE_DEBUG_DIR):
        os.mkdir(dev.SQLALCHEMY_DATABASE_DEBUG_DIR)

    if not os.path.exists(RESOURCE_DIR):
        os.mkdir(RESOURCE_DIR)
    else:
        shutil.rmtree(RESOURCE_DIR, ignore_errors=True)
        os.mkdir(RESOURCE_DIR)

    if not os.path.exists(SECRETS_PATH):
        with open(SECRETS_PATH, 'w') as f:
            f.write(json.dumps({
                "access_token": str(uuid.uuid4())
            }))
        ACCESS_TOKEN = load_access_token(SECRETS_PATH)

    print("access_token", ACCESS_TOKEN)

    base.recreate_database()


if __name__ == "__main__":
    main()

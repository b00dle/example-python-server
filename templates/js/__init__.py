from flask import send_from_directory


PATH = "templates/js"


def produce(file):
    if ".js" in file:
        return send_from_directory(PATH, file)
    return send_from_directory(PATH, file + ".js")
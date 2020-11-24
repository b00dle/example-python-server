from flask import send_from_directory


PATH = "templates/csv"


def produce(file):
    if ".csv" in file:
        return send_from_directory(PATH, file)
    return send_from_directory(PATH, file + ".csv")
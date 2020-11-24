from flask import render_template


def produce():
    """
    This function just responds to the browser URL
    localhost:44100/
    :return: the rendered template 'home.html'
    """
    return render_template("para-cords.html")

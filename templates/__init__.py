def attach_to(app):
    from templates import home
    from templates import para_cords
    from templates import csv
    from templates import js

    @app.route("/")
    def route_home():
        return home.produce()

    @app.route("/para-cords")
    def route_para_cords():
        return para_cords.produce()

    @app.route("/js/<path:file>.js")
    def route_js(file):
        return js.produce(file)

    @app.route("/csv/<path:file>.csv")
    def route_csv(file):
        return csv.produce(file)

def attach_to(app):
    from templates import home

    @app.route("/")
    def route_home():
        return home.produce()
import connexion
import templates
import rest_api

app = connexion.App(__name__, specification_dir="./")
rest_api.attach_to(app)
templates.attach_to(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=44100)

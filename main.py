##############################
# DreamBot Project
# Design by Dreamily854
##############################

import flask
import logging

flask_set = {
    "static_folder": "WebUI/",
    "static_url_path": "/"
}
app = flask.Flask(__name__, **flask_set)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=30011, debug=True)

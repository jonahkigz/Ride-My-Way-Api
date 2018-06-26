from flask import Flask, redirect
from .v1.rides.views import rides
from flasgger import Swagger

app = Flask(__name__)

template = {
    "swagger": 2.0,
    "version": "v1",
}

Swagger(app, template=template)

@app.route('/')
def index():
    return redirect('/')
app.register_blueprint(rides)


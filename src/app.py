from flask import Flask, render_template, request
from views import views
import pandas as pd

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

if __name__ == "__main__":
    app.run(debug=True, port=8000)


df = pd.read_csv('pvc.csv')


def index():
    return render_template(index.html)

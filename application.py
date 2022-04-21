from flask import Flask, render_template, request
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        form_data = request.form
        name = request.form.get('name')
        return render_template('index.html', title='Home', name=name, form_data=form_data), 200
    name = request.form.get('name')
    return render_template('index.html', title='Home', name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Page not found"), 404


if __name__ == "__main__":
    app.run(debug=True)

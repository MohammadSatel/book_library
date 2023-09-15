import logging
from flask import Flask, render_template

app = Flask(__name__, template_folder="../front/templates", static_folder="../front/static")

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s: %(message)s')

@app.route("/")
def home():
    logging.info('Home page accessed')
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

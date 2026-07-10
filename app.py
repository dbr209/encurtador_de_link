from flask import Flask

from routes import main
from database.schema import create_urls_table

app = Flask(__name__)

app.register_blueprint(main)

if __name__ == "__main__":
    create_urls_table()
    app.run(debug=True)
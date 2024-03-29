from flask import Flask
from flask_cors import CORS
import os
from routes.diagnosis_routes import diagnosis


app = Flask(__name__)

app.register_blueprint(diagnosis)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    # app.run(debug=True)
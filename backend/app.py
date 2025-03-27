from flask import Flask
from flask_cors import CORS
from routes import blog_routes

app = Flask(__name__)
CORS(app)

# Register routes
app.register_blueprint(blog_routes)

if __name__ == "__main__":
    app.run(debug=True)

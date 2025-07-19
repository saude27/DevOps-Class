from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Access the database URL from the environment
DATABASE_URL = os.getenv("DATABASE_URL")
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}@{os.environ["POSTGRES_HOST"]}:{os.environ["POSTGRES_PORT"]}/{os.environ["POSTGRES_DB"]}'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@db:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            "completed": self.completed
        }

# Define the API endpoints
@app.route("/api/todos", methods=["GET"])
def get_todos_api():
    todos = Todo.query.all()
    return jsonify([todo.serialize() for todo in todos]),   200

@app.route("/api/todos", methods=["POST"])
def add_todo_api():
    data = request.get_json()
    if data and "text" in data:
        new_todo = Todo(text=data["text"])
        db.session.add(new_todo)
        db.session.commit()
        return jsonify(new_todo.serialize()),   201
    else:
        return jsonify({"error": "Invalid request data"}),   400

@app.route("/api/todos/<int:id>", methods=["PUT"])
def update_todo_api(id):
    data = request.get_json()
    todo = Todo.query.get(id)
    if todo:
        if "completed" in data:
            todo.completed = data["completed"]
        db.session.commit()
        return jsonify(todo.serialize()),   200
    else:
        return jsonify({"error": "Todo not found"}),   404

@app.route("/api/todos/<int:id>", methods=["DELETE"])
def delete_todo_api(id):
    todo = Todo.query.get(id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"message": "Todo deleted successfully"}),   200
    else:
        return jsonify({"error": "Todo not found"}),   404

@app.cli.command('create_db')
def create_db():
    with app.app_context():
        db.create_all()
        print('Database and tables created!')

# Healtcheck
@app.route('/health')
def health_check():
    return jsonify(status='ok')

if __name__ == '__main__':
    app.run(debug=True)

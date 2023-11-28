# Import Flask and create an app instance:

from flask import Flask, jsonify
app = Flask(__name__)

# Create a route that returns JSON data representing a to-do list:


@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = [
        {"id": 1, "task": "Buy groceries", "completed": False},
        {"id": 2, "task": "Read a book", "completed": False},
        {"id": 3, "task": "Write a blog post", "completed": True}
    ]
    return jsonify(todos)


@app.route('/')
def index():
    return app.send_static_file('index.html')


# Run the server:


if __name__ == '__main__':
    app.run(debug=True)[]=[[[=]]]

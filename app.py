from flask import Flask
app = Flask(__name__)


@app.route('/', defaults={'query_path': 'index'})
@app.route('/<path:query_path>')
def match_path(query_path):
    return f'Query path: {query_path}'

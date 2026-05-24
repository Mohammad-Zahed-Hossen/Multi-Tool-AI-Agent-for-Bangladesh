from flask import Flask, request, jsonify
from tools import institutions_tool, hospitals_tool, restaurants_tool

app = Flask(__name__)


@app.route('/')
def index():
    return 'Multi-tool AI Agent app'


@app.route('/institutions')
def institutions():
    q = request.args.get('q','')
    results = institutions_tool.find_by_name(q) if q else institutions_tool.list_all()
    return jsonify(results)


@app.route('/hospitals')
def hospitals():
    q = request.args.get('q','')
    results = hospitals_tool.find_by_name(q) if q else hospitals_tool.list_all()
    return jsonify(results)


@app.route('/restaurants')
def restaurants():
    q = request.args.get('q','')
    results = restaurants_tool.find_by_name(q) if q else restaurants_tool.list_all()
    return jsonify(results)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

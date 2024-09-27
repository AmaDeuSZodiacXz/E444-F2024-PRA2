from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello,Dave!</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Page Not Found</h1>', 404

if __name__ == '__main__':
    app.run(debug=True)

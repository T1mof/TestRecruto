from flask import Flask, request, render_template

app = Flask(__name__)

@app.get('/')
def users_get():
    name = request.args.get('name', '')
    message = request.args.get('message', '')
    return render_template('index.html', name=name, message=message)

if __name__ == '__main__':
	app.run(debug=True, port=5000)
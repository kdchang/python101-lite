from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube


app = Flask(__name__)

@app.route('/')
def index():
	filename = request.args.get('filename')
	return render_template('index.html', filename=filename)


@app.route('/submit', methods=['POST'])
def post_submit():
    url = request.form.get('url')
    YouTube(url).streams.first().download()
    filename = YouTube(url).streams.first().default_filename
    
    return redirect(url_for('index', filename=filename))


if __name__ == '__main__':
	app.run(debug=True)

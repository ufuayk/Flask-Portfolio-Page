from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/github')
def github():
    return redirect("https://github.com/yourname") # You can fill this with the link to your GitHub account.

if __name__ == '__main__':
    app.run(debug=True)
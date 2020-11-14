from flask import Flask, render_template
app = Flask(__name__)

@app.route('/about')
def about():
    name = "Erlon"
    return render_template('about.html', name=name)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
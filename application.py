from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',name='world')
@app.route('/Doug')
def doug():
    return render_template('index.html', name='Doug')
if __name__ == '__main__':
    # execute only if run as the entry point into the program
    app.run()
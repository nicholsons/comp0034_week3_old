from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Group XX Home')


@app.route('/matplotlib')
def matplotlib():
    return render_template('matplotlib.html', title="Matplotlib charts")


@app.route('/express')
def express():
    return render_template('express.html', title="Plotly express charts")


if __name__ == '__main__':
    app.run()

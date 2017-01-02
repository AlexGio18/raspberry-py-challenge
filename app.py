from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello world'

@app.route('/pie/<fruit>')
def pie(fruit):
  return render_template('pie.html', fruit=fruit)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
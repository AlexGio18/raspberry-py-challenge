from flask import Flask, json, render_template, jsonify, redirect, abort, make_response

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error':'Not found'}), 404)

pies = [
  {
    'id': 1,
    'name':u'Raspberry Pie',
    'fruit':u'raspberry',
    'ingredients':['raspberry','sugar','flour']
  },
  {
    'id':2,
    'name':u'Apple Pie',
    'fruit':u'apple',
    'ingredients':['apple','sugar','flour']
  }
]
@app.route('/')
def index():
  return redirect('/pies', code=302)

@app.route('/pies', methods=['GET'])
def get_pies():
  return jsonify({'pies': pies})

@app.route('/pies/<fruit>')
def get_pie(fruit):
  pie = [pie for pie in pies if pie['fruit'] == fruit]
  if len(pie) == 0:
    abort(404)
  json_pie = jsonify(name=pie[0]['name'],
                       ingredients=pie[0]['ingredients'])
  parsed_pie = json.loads(json_pie)
  return parsed_pie["name"]

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
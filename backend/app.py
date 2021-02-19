from flask import Flask, request, jsonify
from classes import *

app = Flask(__name__)
json_decoder = JSON_Decoder()

@app.route('/addNote', methods=['POST'])
def addNote():
	json = request.json

	name = json.get('name')
	author = json.get('author')
	body = json.get('body')

	new_note = Note(name, author, body)
	new_note.add(new_note)
	return json_decoder.decode(new_note)

@app.route('/getNote')
def getNote():
	json = request.json

	code = json.get('code')

	if code in Note.objects:
		return Note.objects[code]
	return jsonify(status=404)

if __name__ == '__main__':
	app.run(debug=True)
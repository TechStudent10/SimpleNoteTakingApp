import random, string

class Random(object):
	@staticmethod
	def id(length=6):
		code = ''.join(random.choices(string.ascii_uppercase, k=length))
		return code

class Object(object):
	objects = {}

	def __init__(self):
		pass

	def getId(self):
		try:
			return self._id
		except NameError:
			return

	@classmethod
	def add(cls, obj):
		_id = obj.getId()
		if not _id:
			obj._id = Random.id()
			_id = obj.getId()

		cls.objects[_id] = obj

class Note(Object):
	def __init__(self, name, author, body):
		self._id = Random.id(8)
		self.name = name
		self.author = author
		self.body = body.split('\n')

	def toJSON(self):
		json = {
			'_id': self._id,
			'name': self.name,
			'author': self.author,
			'body': self.body
		}

		return json

class JSON_Decoder:
	def __init__(self):
		pass

	def decode(self, obj):
		try:
			return obj.toJSON()
		except AttributeError:
			return
class SearchRoomSession():
	def __init__(self, request):
		self.session = request.session

		search = self.session.get('room-search-key')

		if "room-search-key" not in request.session:
			search = self.session['room-search-key'] = {}

		self.search = search

	def add(self, target, value):
		self.search[str(target)] = value

		self.session.modified = True



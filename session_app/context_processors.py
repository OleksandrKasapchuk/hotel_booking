from .search_sessions import SearchRoomSession

def search_room_session(request):
	return {"search": SearchRoomSession(request)}
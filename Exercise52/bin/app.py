import web
from magicalyourney import map
from magicalyourney import player

urls = (
  '/start', 'StartEngine',
  '/game', 'GameEngine',
  '/', 'Index',
  '/reset', 'Reset',
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                  initializer={'room': None,'player': None,'user': None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")


class Reset(object):
    def GET(self):
		#the user can see his last-game score
		session.user.score = session.player.score
		session.room = map.START
		session.player = player.player1
		startPage = "/game"
		web.seeother(startPage)

class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values

		if not session.user:
			return web.seeother("/start")
		else:
			if session.room == None:
				session.room = map.START
				if session.player:
					#the user can see his last-game score
					session.user.score = session.player.score
				session.player = player.player1
		web.seeother("/game")
		

class StartEngine(object):
	def GET(self):
		if not session.user:
			return render.index()
		else:
			web.seeother("/")
	def POST(self):
		form = web.input(username=None)
		if form.username:
			if not session.user:
				session.user = player.User(form.username)
		else:
			session.user = player.user1
		web.seeother("/")

class GameEngine(object):
	def showRoom(self):
		return render.show_room(room=session.room,player = session.player, user = session.user)

	def GET(self):
		if session.room:
			if session.player.dead:
				ret = self.showRoom()
				session.room = None
				return ret
			else:
				return self.showRoom()
		else:
			return render.you_died()

	def POST(self):
		form = web.input(action=None)

		if session.room and form.action:
			if session.room.curlevel == session.room.totalLevels and not session.room.obstacle:
				
				#If a room has some items, the player gets them
				if session.room.items:
					session.player.items = session.room.items
				#Checks if the user input word is a key in the room path dictionary, 
				#this prevents the user from dying when he mistypes
				if not session.room.check_key(form.action):
					web.seeother("/game")
				else:
					session.player.score += session.room.points
					session.room = session.room.go(form.action, session.player)
					if session.room:
						lastLevel = session.room.checkJourney()
						web.seeother("/game")
					else:
						web.seeother("/game")
			else:
				action = session.room.doAction(form.action,session.player)
				lastLevel = session.room.checkJourney()
				if action == "death":
					session.player.dead = True
					session.player.deadMessage = session.room.currentDeath
					web.seeother("/game")
				else:
					web.seeother("/game")

if __name__ == "__main__":
    app.run()
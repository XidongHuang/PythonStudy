"""*************************************************************************
    > File Name: bin/app.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Thu 13 Oct 16:18:31 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5

import web
from gothonweb import map

urls = (
		'/game', 'GameEngine',
		'/', 'Index',
		)

app = web.application(urls, globals())

if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer = {'room': None})
	
	web.config._session = session
else:
	session = web.config._session


render = web.template.render("templates/")

class Index(object):
	def GET(self):
		session.room = map.START
		web.seeother("/game")

class GameEngine(object):
	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
			return render.you_died()

def POST(self):
	form = web.input(action=None)

	if session.room and form.action:
		session.room = session.room.go(form.action)
	
	web.seeother("/game")

if __name__ == "__main__":
	app.run()

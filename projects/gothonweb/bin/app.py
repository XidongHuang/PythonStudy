"""*************************************************************************
    > File Name: bin/app.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Thu 13 Oct 16:18:31 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5

import web

urls = (
		'/', 'Index'
		)

app = web.application(urls, globals())

render = web.template.render("templates/")

class Index(object):
	def GET(self):
		greeting = "Hello World"
		return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()

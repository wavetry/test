import web

render = web.template.render('templates/')
urls = (
  '/(*)', 'index'
)

class index:
    def GET(self,name):
        return render.index(name)

# class show(object):
# 	"""docstring for show"""
# 	def __init__(self, arg):
# 		super(show, self).__init__()
# 		self.arg = arg
# 	def GET(self):
# 		return render.show('hello world')
		
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
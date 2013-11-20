import webapp2
import entities
import json
from google.appengine.ext import db

#----JSON ON BLOG----#
# This class extracts all the blog entries from the database
# and puts each blog entry in a dictionary which in turn is added to a list
# This list is then converted to json and written out
class BlogJsonHandler(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'application/json'   
		blogs = db.GqlQuery("SELECT * FROM BlogPost ORDER BY created DESC limit 10")
		dic_list = []
		for blog in blogs:
			created_conv = blog.created.strftime("%Y-%m-%d %H:%M:%S")
			raw_dic = {'content': blog.content,'subject':blog.subject,'created':created_conv}
			dic_list.append(raw_dic)
		
		self.response.out.write(json.dumps(dic_list))

#----JSON ON PERMAHANDLER----#
# This class extracts a blog entry by id from the database
# and puts the blog entry in a dictionary
# This dictionary is then converted to json and written out
class PermaHandler(webapp2.RequestHandler):
	def get(self, post_id):
		self.response.headers['Content-Type'] = 'application/json'   
		b = entities.BlogPost.get_by_id (int(post_id));
		created_conv = b.created.strftime("%Y-%m-%d %H:%M:%S")
		raw_dic = {'content': b.content,'subject':b.subject,'created':created_conv}
		
		self.response.out.write(json.dumps(raw_dic))
		
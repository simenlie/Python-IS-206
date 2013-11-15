import webapp2
import os
import hmac
import resources
import jinja2
import entities
import json
import time
from google.appengine.ext import db
import problemset3

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

class ProblemSet5Handler(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'application/json'   
		blogs = db.GqlQuery("SELECT * FROM BlogPost ORDER BY created DESC limit 10")
		dic_list = []
		for blog in blogs:
			created_conv = blog.created.strftime("%Y-%m-%d %H:%M:%S")
			raw_dic = {'content': blog.content,'subject':blog.subject,'created':created_conv}
			dic_list.append(raw_dic)
		
		self.response.out.write(json.dumps(dic_list))
		

class PermaHandler(webapp2.RequestHandler):
	def get(self, post_id):
		self.response.headers['Content-Type'] = 'application/json'   
		b = problemset3.BlogPost.get_by_id (int(post_id));
		created_conv = b.created.strftime("%Y-%m-%d %H:%M:%S")
		raw_dic = {'content': b.content,'subject':b.subject,'created':created_conv}
		
		self.response.out.write(json.dumps(raw_dic))
		
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

class BlogPost(db.Model):
	subject = db.StringProperty(required = True)
	content = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)

class Handler(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)
		
	def render_str(self,template,**params):
		t=jinja_env.get_template(template)
		return t.render(params)
	
	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))
		
class BlogFront(Handler):

	def render_front(self, subject="",content="",error=""):
		blogs = db.GqlQuery("SELECT * FROM BlogPost ORDER BY created DESC limit 10")
		self.render("blog.html",subject = subject,content = content,error = error,blogs=blogs)

	def get(self):
		
		self.render_front()


class NewPost(Handler):

	def render_front(self, subject="",content="",error=""):
		blogs = db.GqlQuery("SELECT * FROM BlogPost ORDER BY created DESC")
		self.render("newpost.html",subject = subject,content = content,error = error,blogs=blogs)

	def get(self):
		
		self.render_front()
	
	def post(self):
		subject = self.request.get("subject")
		content = self.request.get("content")
		
		if subject and content:
			b = BlogPost(subject = subject, content = content)
			b.put()
			
			self.redirect("/blog/%d" % b.key().id())
		else:
			error = "We need both a title and some artwork!"
			self.render_front(subject,content,error)
						

class PermaHandler(Handler):
	def render_front(self, b=""):
		self.render("perma.html",b=b)
	def get(self, post_id):
		b = BlogPost.get_by_id (int(post_id));
		self.render_front(b)
		#self.response.write('This is the ProductHandler. The product id is %s' % b.subject)
			

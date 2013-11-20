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
import common
import entities

from google.appengine.ext import db

class BlogFront(common.Handler):
	def render_front(self, subject="",content="",error=""):
		blogs = db.GqlQuery("SELECT * FROM BlogPost ORDER BY created DESC limit 10")
		self.render("blog.html",subject = subject,content = content,error = error,blogs=blogs)

	def get(self):
		self.render_front()

class NewPost(common.Handler):
	def render_front(self, subject="",content="",error=""):
		blogs = db.GqlQuery("SELECT * FROM BlogPost ORDER BY created DESC")
		self.render("newpost.html",subject = subject,content = content,error = error,blogs=blogs)

	def get(self):
		self.render_front()
	
	def post(self):
		subject = self.request.get("subject")
		content = self.request.get("content")
		if subject and content:
			b = entities.BlogPost(subject = subject, content = content)
			b.put()
			self.redirect("/blog/%d" % b.key().id())
		else:
			error = "Fill in both subject and content!"
			self.render_front(subject,content,error)
						
class PermaHandler(common.Handler):
	def render_front(self, b=""):
		self.render("perma.html",b=b)
	def get(self, post_id):
		b = entities.BlogPost.get_by_id (int(post_id));
		self.render_front(b)
		#self.response.write('This is the ProductHandler. The product id is %s' % b.subject)
			

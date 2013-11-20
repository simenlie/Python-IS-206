# -*- coding: utf-8 -*-
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
# This is the main module. This is where the application is started from 
#
import webapp2
import cgi
import string
import re
import problemset2
import problemset3
import problemset4
import problemset5
import jinja2
import os
import common

# Uses Django templating language to have seperate html files, automatic escaping etc
template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

# MainHandler that gives the user the index.html page
# It is a subclass of the Handler class in my common module/file
# This Handler only have one function; get
class MainHandler(common.Handler):
	def get(self):
		self.render("index.html")
		
# Maps url paths to my handler classes
app = webapp2.WSGIApplication([
    ('/', MainHandler), 
	('/problem-set-2',problemset2.Rot13Handler),
	('/problem-set-2/signup',problemset2.SignupHandler),
	('/problem-set-2/welcome',problemset2.WelcomeHandler),
	('/blog', problemset3.BlogFront),
	(r'/blog/(\d+)', problemset3.PermaHandler),
	(r'/blog/(\d+).json', problemset5.PermaHandler),
	('/blog/newpost', problemset3.NewPost),
	('/blog/signup', problemset4.SignupHandler),
	('/blog/welcome', problemset4.WelcomeHandler),
	('/blog/login', problemset4.LoginHandler),
	('/blog/logout', problemset4.LogoutHandler),
	('/blog/.json', problemset5.BlogJsonHandler)
], debug=True)

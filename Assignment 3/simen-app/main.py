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
import webapp2
import cgi
import string
import re
import problemset3
import problemset4
import problemset5
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
		  
		  
		  
#SIGNUP
def checkPassword(password,verify):
	if password == verify:
		return password
	else:
		return None
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    
def checkUsername(username):
	if " " in username:
		return False
	elif USER_RE.match(username):
		return True
	else:
		return False
		
def checkPassIs(password):
	if password == "":
		return False
	else:
		return True
E_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def checkEmail(email):
	if email != "":
		return E_RE.match(email)
	else:
		return True
	

#Check if char is lowercase or uppercase
def case_checker(char,index):
	if char.islower():
		return string.lowercase[index]
	else:
		return string.uppercase[index]
		  
def rot13(s):
	lenface = len(s)
	edges = ""
	for i in range(lenface):
		if s[i].isalpha():
			if s[i].islower():
				current = string.lowercase.index(s[i])
			else:
				current = string.uppercase.index(s[i])
			changer = int(current) + 13
			if changer >= 26:
				newVal = changer - 26
				stris = case_checker(s[i],newVal)
				edges += stris
				#s=s.replace(letter,stris,1)
			else:
				stris2 = case_checker(s[i],changer)
				edges += stris2
				#s=s.replace(letter,stris2,1)
		else:
			edges += s[i]

	return edges
          
def valid_month(month):
	if month.capitalize() in months:
		return month.capitalize()
	else:
		return None
def escape_html(s):
	return cgi.escape(s, quote = True)
	
def valid_day(day):
	if day.isdigit():
		day = int(day)
		if day > 0 and day <= 31:
			return day

def valid_year(year):
	if year.isdigit():
		year = int(year)
		if year > 1900 and year < 2021:
			return year
form="""
<form method ="post">
What is your birthday?
<br>
<label> Month
<input type ="text" name="month" value="%(month)s"></label>
<br>
<label> Day
<input type ="text" name="day" value="%(day)s"></label>
<br>
<label> Year
<input type ="text" name="year" value="%(year)s"></label>
<div style="color: red">%(error)s</div>
<br>
<br>
<input type="submit">
</form>
"""

form2 = """
<form method="post">
<h1>Enter some text to ROT13:</h1>
<textarea name="text" style="height: 100px; width: 400px;">%(text)s</textarea>
<br>
<input type="submit">
</form>
"""



welcome = """
<h1>Welcome, %(username)s</h1>
"""

signupForm = """
<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>
  <body>
  <h1>Signup</h1>
<form method="post">

<label>
Username
<input  type="text" name="username" value="%(username)s">
<span style="color: red">%(error2)s</span>
</label>
<br>
<label>
Password
<input  type="text" name="password" value="%(password)s">
<span style="color: red">%(error4)s</span>
</label>
<br>
<label>
Verify Password
<input  type="text" name="verify" value="%(verify)s">
<span style="color: red">%(error)s</span>
</label>
<br>
<label>
Email(optional)
<input  type="text" name="email" value="%(email)s">
<span style="color: red">%(error3)s</span>
</label>

<br>
<input type="submit">
</form>

  </body>

</html>
"""

class Handler(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)
		
	def render_str(self,template,**params):
		t=jinja_env.get_template(template)
		return t.render(params)
	
	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))

class MainHandler(Handler):
	def get(self):
		#self.response.out.write(startHtml)
		self.render("index.html")
				
class BirthdayHandler(webapp2.RequestHandler):
	def write_form(self, error="",month="",day="",year=""):
		self.response.out.write(form %{"error": error,"month": escape_html(month),"day": escape_html(day),"year": escape_html(year)})
	def get(self):
		self.write_form()
		
	def post(self):
		user_month = self.request.get('month')
		user_year = self.request.get('year')
		user_day = self.request.get('day')
		
		month = valid_month(user_month)
		day = valid_day(user_day)
		year = valid_year(user_year)
		
		
		if not (month and day and year):
			self.write_form("That doesn't look valid to me, friend.",user_month,user_day,user_year)
		else:
			self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thanks!")
	def post(self):
		text = self.request.get('text')
		
class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		text = self.request.get('username')
		self.response.out.write(welcome %{"username": text})

class ProblemSet2Handler(webapp2.RequestHandler):
	def write_form(self, text=""):
		self.response.out.write(form2 % {"text": escape_html(text)})
	def get(self):
		self.write_form()
	def post(self):
		text = self.request.get('text')
		rot = rot13(text)
		self.write_form(rot)	
		
class ProblemSet2bHandler(webapp2.RequestHandler):
	def write_form(self,error="",error2="",error3="",error4="",username="",password="",verify="",email=""):
		self.response.out.write(signupForm % {"error": error,"error2": error2,"error3": error3,"error4": error4,"username": escape_html(username),"password": escape_html(password),"verify": escape_html(verify),"email": escape_html(email)})
	def get(self):
		self.write_form()
	def post(self):
		user_username = self.request.get('username')
		user_password = self.request.get('password')
		user_verify = self.request.get('verify')
		user_email = self.request.get('email')
		err1 = ""
		err2 = ""
		err3 = ""
		err4 = ""
		
		if checkPassword(user_password,user_verify) == None:
			err1 = "Your passwords didn't match."
		if checkUsername(user_username) == False:
			err2 = "That's not a valid username."
		if not checkEmail(user_email):
			err3 = "That's not a valid email."
		if checkPassIs(user_password) == False:
			err4 = "Thats not a valid password."
		if err1 =="" and err2 =="" and err3 =="" and err4 =="":
			self.redirect("/problem-set-2/welcome?username=%s" % user_username)
		else:
			self.write_form(err1,err2,err3,err4,user_username)

app = webapp2.WSGIApplication([
    ('/', MainHandler), 
	('/thanks',ThanksHandler), 
	('/birthday',BirthdayHandler),
	('/problem-set-2',ProblemSet2Handler),
	('/problem-set-2/signup',ProblemSet2bHandler),
	('/problem-set-2/welcome',WelcomeHandler),
	('/blog', problemset3.BlogFront),
	(r'/blog/(\d+)', problemset3.PermaHandler),
	(r'/blog/(\d+).json', problemset5.PermaHandler),
	('/blog/newpost', problemset3.NewPost),
	('/blog/signup', problemset4.MainHandler),
	('/blog/welcome', problemset4.WelcomeHandler),
	('/blog/login', problemset4.LoginHandler),
	('/blog/logout', problemset4.LogoutHandler),
	('/blog/.json', problemset5.ProblemSet5Handler)
], debug=True)

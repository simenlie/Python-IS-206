# -*- coding: utf-8 -*-
import webapp2
import os
import hmac
import jinja2
import entities
import common
from google.appengine.ext import db

#----SIGNUP----#

# The SignupHandler
# Its an extension of the singup from problem set 2
# New in this class is the use of database and cookies
# The get function checks if there is a cookie and if this cookie is secure
# If there is a cookie and the cookie is secure, it returns welcome page, 
# if not it returns the signup page
# The post function uses the same validating checker ass problem set 2 signup
# In addition if the registration/signup data passes the validating
# the users data is stored in the database and a new cookie is made of the user id, 
# wrapped in a secure function that returns a hash of the userid and the user is redirct 
# to a welcome page
class SignupHandler(common.Handler):
	def get(self):
		user_id = self.request.cookies.get('user_id')
		if user_id:
			secure = common.check_secure_val(user_id) #checks that the cookie is secure, hashed
			if secure:
				self.redirect("/blog/welcome")
		else:
			self.render("Registration.html")
		#self.render("Registration.html",username=b.username,password=b.password,email=b.email)
	def post(self):
		user_username = self.request.get('username')
		user_password = self.request.get('password')
		user_verify = self.request.get('verify')
		user_email = self.request.get('email')
		
		errors = common.check_signup(user_username, user_password, user_verify, user_email)
		if errors:
			self.render("Registration.html",error = errors[0],error2 = errors[1],error3 = errors[2],error4 = errors[3],username = user_username)
		else:
			u = entities.User(username = user_username, password = common.make_pw_hash(user_username,user_password), email = user_email) #the password is made up of a combination of username, password and a secret value
			u.put()
			user_id = u.key().id()
			new_cookie_val = common.make_secure_val(str(user_id))#passes the user id into this function to get a hash of the user id
			self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % new_cookie_val)
			self.redirect("/blog/welcome")

#----WELCOME----#
# The welcome handler checks that a secure cookie exists, and if it does it extracts the 
# User by this id and pass it along with the html to the user
class WelcomeHandler(common.Handler):
	def get(self):
		user_id = self.request.cookies.get('user_id')
		secure = common.check_secure_val(user_id)
		if secure:
			b = entities.User.get_by_id (int(secure))
			self.render("welcome.html", b=b)
		else:
			self.redirect("/blog/signup")

#----LOGIN----#
# Checks if a cookies exists, if it does - redirects to welcome
# if not it returns the login page
# The post function extracts all the users from the database
# it goes trought all the users and checks if the hashing of the 
# username and password typed in matches the password in the database
# If it does this user is stored in a variable and a new cookie is made
# If not the login page is returned with an error	
class LoginHandler(common.Handler):
	def get(self):
		user_id = self.request.cookies.get('user_id')
		if user_id:
			secure = common.check_secure_val(user_id)
			if secure:
				self.redirect("/blog/welcome")
		else:	
			self.render("login.html")
	def post(self):
		user_username = self.request.get('username')
		user_password = self.request.get('password')
		err1 = ""
		users = db.GqlQuery("SELECT * FROM User")
		user_exist = None
		for user in users:
			if common.valid_pw(user_username,user_password,user.password):
				user_exist = user
		if user_exist:
			user_id = user_exist.key().id()
			new_cookie_val = common.make_secure_val(str(user_id))
			self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % new_cookie_val)
			self.redirect("/blog/welcome")
		else:
			err1 = "Invalid login"
			self.render("login.html",error = err1)

#----LOGOUT----#
# The LogoutHandler logs a user out of the system
# This is done by setting a variable to an empty string 
# and setting the vaue of the cookie to this string
# the user is redirected to login after logout
class LogoutHandler(common.Handler):
	def get(self):
			user_id = self.request.cookies.get('user_id')
			user_id = ""
			new_cookie_val = str(user_id)
			self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' %new_cookie_val)
			self.redirect("/blog/login")

		

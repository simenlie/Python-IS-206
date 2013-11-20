# -*- coding: utf-8 -*-
import webapp2
import cgi
import string
import re
import jinja2
import os
import common
	
#----ROT13----#

#Checks the case of the char, and based on that returns a character at index position(in upper/lowercase format)
def case_checker(char,index):
	if char.islower():
		return string.lowercase[index]
	else:
		return string.uppercase[index]

#Sjekker først om bokstaven finnes i alfabetet, deretter prøver den å finne posisjonen til bokstaven i alfabetet, 
#hvis det ikke finnes noen posisjon for den(ikke bokstav i engelsk alfabet) returnerer den False, hvis ikke True
#Denne blir brukt i rot13 funksjonen
def check_utf8_alpha(str):
	if str.isalpha():
		if str.islower():
			try:
				string.lowercase.index(str)
				return True
			except:
				return False
		else:
			try:
				string.uppercase.index(str)
				return True
			except:
				return False
	return False
# The rot13 main function
# This function takes a string as parameter and returns the rot13 of the string
# It uses the check_utf8_alpha and case_checker functions
def rot13(s):
	rotated_text = ""
	for i in range(len(s)):
		if check_utf8_alpha(s[i]):
			if s[i].islower():
				current = string.lowercase.index(s[i])
			else:
				current = string.uppercase.index(s[i])
			changer = int(current) + 13
			if changer >= 26:
				newVal = changer - 26
				stris = case_checker(s[i],newVal)
				rotated_text += stris
				#s=s.replace(letter,stris,1)
			else:
				stris2 = case_checker(s[i],changer)
				rotated_text += stris2
				#s=s.replace(letter,stris2,1)
		else:
			rotated_text += s[i]

	return rotated_text

# The handler for rot13. it is a subclass of the common.Handler class
# It contains three functions; write_form, get and post
# The get function uses the write_form function to render the page for the user
# The post function takes the post data from the user and runs the rot13 function on it
# And writes the html with result of the rot13
class Rot13Handler(common.Handler):
	def write_form(self, text=""):
		self.render("rot13.html",text=text)
	def get(self):
		self.write_form()
	def post(self):
		text = self.request.get('text')
		rot = rot13(text)
		self.write_form(rot)

#----SIGNUP----#

# The SignupHandler
# It uses the resoruces.check_signup function 
# that validates the user data. This method is located in common
# because it is used by several modules and by doing so, we prevents duplicated code
# This handler have three functions; get and post, and a helper function: write_form that renders the page for the user
# The get function renders the html for the user(using write_form)
# The post function takes the post data from the user, 
# runs validating/error checking on it and based on this either redirects to 
# a welcome page or back to the html with error messages
class SignupHandler(common.Handler):
	def write_form(self,error="",error2="",error3="",error4="",username="",email="",password="",verify=""):
		self.render("Registration.html", error = error, error2 = error2,error3 = error3,error4= error4,username=username,password = password, verify = verify, email = email)
		#self.response.out.write(signupForm % {"error": error,"error2": error2,"error3": error3,"error4": error4,"username": escape_html(username),"password": escape_html(password),"verify": escape_html(verify),"email": escape_html(email)})
	def get(self):
		self.write_form()
	def post(self):
		user_username = self.request.get('username')
		user_password = self.request.get('password')
		user_verify = self.request.get('verify')
		user_email = self.request.get('email')
		
		errors = common.check_signup(user_username, user_password, user_verify, user_email)#returns either a empty list(no errors) or a list with the errors
		if errors:
			self.write_form(errors[0],errors[1],errors[2],errors[3],user_username,user_email)
		else:
			self.redirect("/problem-set-2/welcome?username=%s" % user_username)

#----WELCOME----#
			
# html for welcome page stored in a string	
welcome = """
<h1>Welcome, %(username)s</h1>
"""
#The WelcomeHandler simply gets the username and prints it with the html
class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		text = self.request.get('username')
		self.response.out.write(welcome %{"username": text})
			
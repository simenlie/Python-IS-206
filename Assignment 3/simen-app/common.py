# -*- coding: utf-8 -*-
import webapp2
import cgi
import string
import re
import jinja2
import os
import random
import hashlib
import hmac

# Uses Jinja2 templating language so we can store html in separate files and escaping is done automatically
template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True) #Escaping is set to True

# A handler that renders and write out the content we pass into the functions
# This classes functions let us pass in an arbitrary number of arguments
# the render_str function takes a template and parameters, it then gets the template 
# that is passed in nad return render on this template with the arguments/parameters
# The write function takes paramaters and writes out the parameters given
# The render function takes a template and parameters and pass this into render_str 
# which is passed into the write function
class Handler(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)
		
	def render_str(self,template,**params):
		t=jinja_env.get_template(template)
		return t.render(params)
	
	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))
		


#SIGNUP FUNCTIONS/HELPERS

#Regular expressions for username, password, email
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{4,20}$")
PASS_RE = re.compile(r"^.{6,20}$")
E_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

# Checks if the password equals the verify password
# Returns: the password or None
def checkPassword(password,verify):
	if password == verify:
		return password
	else:
		return None

# Checks if the username consists of spaces
# if it does, it checks if the username match the pattern we have used(min: 4 char)
# Returns: True if the latter, False otherwise
def checkUsername(username):
	if " " in username:
		return False
	elif USER_RE.match(username):
		return True
	else:
		return False
# Checks if the password matches the pattern we have used(min:6 char)
# Returns: True if it matches, False otherwise
def checkPassIs(password):
	if PASS_RE.match(password):
		return True
	else:
		return False
# Checks if the email contains characters, if it does; matches the pattern we have used
# Returns: True if it matches or if there is no characters, False otherwise
def checkEmail(email):
	if email != "":
		return E_RE.match(email)
	else:
		return True

# A method/function that uses all the latter functions and returns a list of the errors
# if errors is present, otherwise an empty list.
def check_signup(user_username, user_password, user_verify, user_email):
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
		return []
	else:
		return [err1,err2,err3,err4]

#COOKIES for password storage

#Secret value that is used for cookies
SECRET = 'imsosecret'

# Returns a string with random characters and a length of 5 characters
def make_salt():
	return ''.join(random.choice(string.letters) for x in xrange(5))

# Creates a hash of the password, username and salt function
# returns the hash and the salt
# if a salt is not present, a new salt is created
def make_pw_hash(name,pw,salt = None):
	if not salt:
		salt = make_salt()
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s,%s' % (h,salt)

# Given a name, password and a hash
# it extracts the salt from the hash and returns the function make_pw_hash with 
# the name, password and te extracted salt
def valid_pw(name,pw,h):
	salt = h.split(',')[1]
	return h == make_pw_hash(name,pw,salt)
	
#COOKIES FOR browser id
# Given a string(id) s it creates and returns a hash of the SECRET vairable and the string s
def hash_str(s):
	return hmac.new(SECRET,s).hexdigest()

# Given a string s it returns the hash_str function with the given string s
def make_secure_val(s):
	return "%s|%s" % (s,hash_str(s))

# Given a hash h it extracts the first string(id)
# and checks if the hash equals the result of make_secure_val function with the given id
def check_secure_val(h):
	val = h.split('|')[0]
	if h == make_secure_val(val):
		return val
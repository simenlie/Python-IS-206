import webapp2
import os
import hmac
import resources
import jinja2
import entities

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

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
		self.render("Registration.html")
	def post(self):
		user_username = self.request.get('username')
		user_password = self.request.get('password')
		user_verify = self.request.get('verify')
		user_email = self.request.get('email')
		err1 = ""
		err2 = ""
		err3 = ""
		err4 = ""
		
		if resources.checkPassword(user_password,user_verify) == None:
			err1 = "Your passwords didn't match."
		if resources.checkUsername(user_username) == False:
			err2 = "That's not a valid username."
		if not resources.checkEmail(user_email):
			err3 = "That's not a valid email."
		if resources.checkPassIs(user_password) == False:
			err4 = "Thats not a valid password."
		if err1 =="" and err2 =="" and err3 =="" and err4 =="":
			u = entities.User(username = user_username, password = resources.make_pw_hash(user_username,user_password), email = user_email)
			u.put()
			user_id = u.key().id()
			new_cookie_val = resources.make_secure_val(str(user_id))
			self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % new_cookie_val)
			self.redirect("/blog/welcome")
		else:
			self.render("Registration.html",error = err1,error2 = err2,error3 = err3,error4 = err4,username = user_username)

class WelcomeHandler(Handler):
	def get(self):
		user_id = self.request.cookies.get('user_id')
		secure = resources.check_secure_val(user_id)
		if secure:
			b = entities.User.get_by_id (int(secure))
			self.render("welcome.html", b=b)
		else:
			self.redirect("/blog/signup")
			
class LoginHandler(Handler):
	def get(self):
		users = db.GqlQuery("SELECT * FROM User")
		self.render("login.html",users = users)
	def post(self):
		user_username = self.request.get('username')
		user_password = self.request.get('password')
		err1 = ""
		users = db.GqlQuery("SELECT * FROM User")
		user_exist = None
		for user in users:
			if resources.valid_pw(user_username,user_password,user.password):
				user_exist = user
		if user_exist:
			user_id = user_exist.key().id()
			new_cookie_val = resources.make_secure_val(str(user_id))
			self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % new_cookie_val)
			self.redirect("/blog/welcome")
		else:
			err1 = "Invalid login"
			self.render("login.html",error = err1)

class LogoutHandler(Handler):
	def get(self):
			user_id = self.request.cookies.get('user_id')
			user_id = ""
			new_cookie_val = str(user_id)
			self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' %new_cookie_val)
			self.redirect("/blog/signup")

		

import re
import webapp2
import random
import string
import hashlib
import hmac
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

#COOKIES for password storage
SECRET = 'imsosecret'

def make_salt():
	return ''.join(random.choice(string.letters) for x in xrange(5))
	
def make_pw_hash(name,pw,salt = None):
	if not salt:
		salt = make_salt()
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s,%s' % (h,salt)

def valid_pw(name,pw,h):
	salt = h.split(',')[1]
	return h == make_pw_hash(name,pw,salt)
	
#COOKIES FOR browser id
def make_secure_val(s):
	return "%s|%s" % (s,hash_str(s))
	
def check_secure_val(h):
	val = h.split('|')[0]
	if h == make_secure_val(val):
		return val
		
def hash_str(s):
	return hmac.new(SECRET,s).hexdigest()
		
class Helpere(webapp2.RequestHandler):
	def get(self):
		visits = 0
		visit_cookie_str = self.request.cookies.get('visits')
		if visit_cookie_str:
			cookie_val = check_secure_val(visit_cookie_str)
			if cookie_val:
				visits = int(cookie_val)
		visits+= 1
		new_cookie_val = make_secure_val(str(visits))
		self.response.headers.add_header('Set-Cookie','visits=%s' % new_cookie_val)
		if visits > 50:
			self.response.out.write("GRATTIS. du har vart her over %s ganger" %visits)
		else:
			self.response.out.write("%s" %visits)
from core import app
from flask import request,url_for, session, redirect,flash
from datetime import datetime, date, time, timedelta
from functools import wraps
# from core.model.User_details import User_details
from .. import Helper,Cryptography




# Flask View decorators
class RouteGroup:
	def duplicat_login(f):
		@wraps(f)
		def wrap(*args, **kwargs):
			# if user is not logged in, redirect to login page 
			encrypted_user_id = request.args.get('user_id') 
			if encrypted_user_id :
				user_id = Cryptography.decrypt(encrypted_user_id)
				if int(user_id)>0:
					# Get user. os name and browser name 
					ip_address   = request.remote_addr
					checkLogingByUserId = User_details().checkLogingByUserId(user_id,ip_address)
					if checkLogingByUserId :
						return f(*args, **kwargs)
					else:
						return redirect(url_for('user.Login'))
			else :
				flash("You must logged in")
				return redirect(url_for('user.Login'))
			# if session.get('backoffice'):
			# 	return f(*args, **kwargs)
			# else:
			# 	return redirect(url_for('user.Login'))
		return wrap
				
	def login_required(f):
		@wraps(f)
		def wrap(*args, **kwargs):
			# if user is not logged in, redirect to login page      
			encrypted_user_id = request.args.get('user_id')
			if encrypted_user_id:
				user_id = Cryptography.decrypt(encrypted_user_id)        
				if user_id:
					return f(*args, **kwargs)
				else:
					return redirect(url_for('user.Login'))
			else:		
				return redirect(url_for('user.Login'))		
		return wrap


	def hall_allowance(f):
		@wraps(f)
		def wrap(*args, **kwargs):
			# if user is not logged in, redirect to login page      
			encrypted_user_id = request.args.get('user_id')
			print("route filter")
			if encrypted_user_id:
				user_id = Cryptography.decrypt(encrypted_user_id)        
				user    = User_details().get_user(user_id)
				print(user.user_type)
				if user:
					if user.user_type != 'Trade':
						return f(*args, **kwargs)
					else:
						return redirect(url_for('user.Lobby_screen',user_id=encrypted_user_id))		
				else:
					return redirect(url_for('user.Lobby_screen',user_id=encrypted_user_id))
			else:		
				return redirect(url_for('user.Login'))		
		return wrap	


	# def profile_required(f):
	# 	@wraps(f)
	# 	def wrap(*args, **kwargs):
	# 		u=User()
	# 		user = session.get('user')
	# 		user_id = user.get('user_id')
	# 		user = User().get_user(user_id)
	# 		is_profile_update = user.get('is_profile_update')
	# 		print(str(is_profile_update))
	# 		# return str(is_profile_update)
	# 		if is_profile_update != 1 :
	# 			return redirect(url_for('user.UserProfile',user_id= user_id))
	# 		else :
	# 			return f(*args, **kwargs)

	# 	return wrap    

	# def payment_required(f):
	# 	@wraps(f)
	# 	def wrap(*args, **kwargs):
	# 		p = Payment()
	# 		user = session.get('user')
	# 		user_id = user.get('user_id')
	# 		checkpayment = p.checkuserinpayment(user_id)
	# 		# return len(checkpayment)
	# 		if (len(checkpayment)) == 1 :
	# 			return f(*args, **kwargs)
	# 		else:
	# 			return redirect(url_for('payupayment.payment'))
	# 	return wrap

	

# Controller Sample :
# from flask import request, Blueprint, jsonify, redirect, url_for,flash, render_template
# from core.library.route_group import RouteGroup


# @app.route('/home' , methods = ["GET"])
# @RouteGroup.login_required #check if login else automatically redirect to login page
# def home():
#       return "welcome home"

# @app.route('/payment' , methods = ["GET"])
# @RouteGroup.login_required #check if login else automatically redirect to login page
# @RouteGroup.payment_required #check if payment done else  automatically redirect to payment page
# def payment():
#       return "payment page here"
from flask import request, url_for,flash, render_template
from core import app
from flask import url_for
from datetime import datetime, date, time, timedelta
import requests,mandrill,json



class EMAIL:




	def sendMail(subject,html,to):
		# MANDRILL_API_KEY='MAoeFJshVAG4-xTyPpTgUg'
		MANDRILL_API_KEY='XEs1ytJQpEwaZSq25YgB4Q'
		mandrill_client = mandrill.Mandrill(MANDRILL_API_KEY)
		message = {'subject' : subject, 'recipients':to,'from_name': 'WACEM VIRCON 2021',
		'html': html, 'from_email' : 'support@numerotec.com', 
		'cc' : 'support@numerotec.com', 'Reply-To' : 'support@numerotec.com',
		"headers" :{"Reply-To": "support@numerotec.com"} ,'to' : [{'email':to,'name':to,'type':'to'},
		{'email':'wacem21backup@gmail.com','name':to,'type':'cc'}] }

		result = mandrill_client.messages.send(message = message,send_async=True)
		return ('success')
		
	def sendBulkMail(subject,html,to):
		# MANDRILL_API_KEY='MAoeFJshVAG4-xTyPpTgUg'
		MANDRILL_API_KEY='XEs1ytJQpEwaZSq25YgB4Q'
		mandrill_client = mandrill.Mandrill(MANDRILL_API_KEY)
		message = {'subject' : subject, 'recipients':to,'from_name': 'WACEM21',
		'html': html, 'from_email' : 'conference@wacem21.com', 
		'cc' : 'conference@wacem21.com', 'Reply-To' : 'conference@wacem21.com',
		"headers" :{"Reply-To": "conference@wacem21.com"} ,'to' : [{'email':to,'name':to,'type':'to'}] }

		result = mandrill_client.messages.send(message = message,send_async=True)
		return ('success')
		
		


	def sendHelpDeskMail(subject,html,to):
		MANDRILL_API_KEY='XEs1ytJQpEwaZSq25YgB4Q'
		# MANDRILL_API_KEY='MAoeFJshVAG4-xTyPpTgUg'
		# MANDRILL_API_KEY='XEs1ytJQpEwaZSq25YgB4Q' # IP Address restricted
		mandrill_client = mandrill.Mandrill(MANDRILL_API_KEY)
		message = {'subject' : subject, 'recipients':to,'from_name': 'WACEM VIRCON 2021 - Help desk',
		'html': html, 'from_email' : 'conference@wacem21.com', 
		'cc' : 'conference@wacem21.com', 'Reply-To' : 'conference@wacem21.com',
		"headers" :{"Reply-To": "conference@wacem21.com"} ,'to' : [{'email':to,'name':to,'type':'to'},
		{'email':'wacem21backup@gmail.com','name':to,'type':'cc'},{'email':'conference@wacem21.com','name':to,'type':'to'},] }

		result = mandrill_client.messages.send(message = message,send_async=True)
		return ('success')

   


	# def sendHelpDeskMail(subject,html,to):
	# 	# MANDRILL_API_KEY='MAoeFJshVAG4-xTyPpTgUg'
	# 	MANDRILL_API_KEY='XEs1ytJQpEwaZSq25YgB4Q'
	# 	mandrill_client = mandrill.Mandrill(MANDRILL_API_KEY)

	# 	message = { 'from_email': 'support@numerotec.com',
	# 	'from_name': 'MOS VIRCON 2021',

	# 	'to': [{
	# 			'email': 'support@numerotec.com',
	# 			'name': 'Help desk',
	# 			'type': 'to'
	# 			},
	# 			{
	# 			'email': 'mosconbackup@gmail.com',
	# 			'name': to,
	# 			'type': 'to'
	# 			},

	# 			],
	# 	'subject': subject,
	# 	'html': html,
	# 	"headers": {
 #            "Reply-To": to
 #        },
	# 	}
	# 	result = mandrill_client.messages.send(message = message,send_async=True)		
	# 	return ('success')		

	

	

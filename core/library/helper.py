from core import app
from flask import url_for
from datetime import datetime, date, time, timedelta


#settime working as global variable but commented for easy identification of this variable using class name 
# global settime
# settime = 5

class Helper:	

    

	def footer_text():
		return ""

	#set minutes for timesplitter and rowspan calc
	#settime = 10
# --------------------PROGRAM SHEET FUNCTIONS START------------------------------
	def timesplitter(starttime, endtime):
		fmt = '%H:%M'
		d1 = datetime.strptime(starttime, fmt)
		d2 = datetime.strptime(endtime, fmt)   
		# d1 = datetime.datetime(2019, 1, 1, 10, 0)
		# d2 = datetime.datetime(2019, 1, 1, 11, 0)
		delta = timedelta(minutes=15)
		times = []
		while d1 < d2:
			times.append(d1)
			d1 += delta
		times.append(d2)
		# print(times)

		new_list  =   []
		for i in range(len(times) - 1):
			result = "{} - {}".format(times[i], times[i+1])
			new_list.append(result)                
		# print(new_list)
		return new_list
		# yaxis_list = [] 
		# for i in new_list: 
		#     if i not in yaxis_list: 
		#         yaxis_list.append(i) 
		# print(yaxis_list)
		# return yaxis_list
	
	def date_diff(d1, d2):
		# fmt	= '%H:%M'
		d1		=	date(d1,'%Y, %m, %d')
		d2		=	date(d2,'%Y, %m, %d')   		
		diff	=	str(d1) - str(d2)		
		# print(diff)
		return diff

	def rowspan_calc(starttime, endtime):
		fmt = '%H:%M'
		d1 = datetime.strptime(starttime, fmt)
		d2 = datetime.strptime(endtime, fmt)   
		
		delta = timedelta(minutes=15)
		times = []
		counter = 0 
		while d1 < d2:
			times.append(d1)
			d1 += delta
			counter += 1
			times.append(d2)
		# print(counter)
		return counter

	# def endtime_calc(starttime):    
	# 	d1 = starttime       
	# 	delta = timedelta(minutes=55)    
	# 	d1 += delta            
	# 	return d1

	def isAjax(request):
		if request.headers.get("X-Requested-With") == "XMLHttpRequest":
			return True
		else:
			return False	


app.jinja_env.globals.update(Helper=Helper)	




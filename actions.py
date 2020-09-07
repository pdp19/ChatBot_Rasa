from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_sdk.forms import FormAction
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import re
import pandas as pd
import smtplib, ssl
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask
from flask_mail import Mail, Message
import requests
from email.message import EmailMessage
import sys,os
import warnings
warnings.filterwarnings("ignore")

sys.path.append(os.getcwd())
import valid_data

operating_cities = valid_data.operating_cities
valid_cusines = valid_data.valid_cusines

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		# dispatcher.utter_message("Please wait! Let me find you the best restaurent for you.")
		config={ "user_key":"378ed860b2353f35f0d8dafe1b021732"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20)
		d = json.loads(results)
		res_name = []
		res_addr = []
		res_rating = []
		res_price = []
		res_cuisine = [] 
		for restaurant in d['restaurants']:
				res_name.append(restaurant['restaurant']['name'])
				res_addr.append(restaurant['restaurant']['location']['address'])
				res_rating.append(restaurant['restaurant']['user_rating']['aggregate_rating'])
				res_price.append(restaurant['restaurant']['average_cost_for_two'])
				res_cuisine.append(restaurant['restaurant']['cuisines'])

		df=pd.DataFrame({'Name':res_name,'Address':res_addr,'Budget':res_price,'Rating':res_rating,'Cuisine':res_cuisine})
		df['Rating'] = df['Rating'].apply(pd.to_numeric)

		if price == 'Lesser_300':
			df_filtered=df[df['Budget'] < 300]
		elif price == 'In_Between_300_To_700':
			df_filtered=df[(df['Budget'] >= 300) & (df['Budget'] <= 700)]
		elif price == 'More_700':
			df_filtered=df[df['Budget'] > 700]
		else:
			df_filtered=df	

		if len(df_filtered['Name'])==0:
			response= "We are sorry, we couldn't find any restaurent in your location."
			return None
		df_sorted=df_filtered.sort_values("Rating",ascending=False)
		df_sorted['Result_Message']="---> Restaurant \""+ df_sorted['Name']+ "\" found in "+ df_sorted['Address'] +\
							   		  " has been rated " + df_sorted['Rating'].astype(str) + "*/5"
		response='\n'.join(df_sorted['Result_Message'].head(5).tolist())
		dispatcher.utter_message("Here are the top 5 restaurents what you are looking for: \n"+response+"\n")
		return "Searched Restaurent successfully!"
		

class SendEmailToUser(FormAction):
	def name(self):
		return 'action_send_email'
	def run(self, dispatcher, tracker,domain):
		email_id = tracker.get_slot("email")
		regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
		if any(email_id):
			if(re.search(regex,email_id)):
				# dispatcher.utter_message("Hold on! Let me send you an email.")
				config={ "user_key":"378ed860b2353f35f0d8dafe1b021732"}
				zomato = zomatopy.initialize_app(config)
				loc = tracker.get_slot('location')
				cuisine = tracker.get_slot('cuisine')
				price = tracker.get_slot('price')
				location_detail=zomato.get_location(loc, 1)
				d1 = json.loads(location_detail)
				lat=d1["location_suggestions"][0]["latitude"]
				lon=d1["location_suggestions"][0]["longitude"]
				cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
				results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20)
				d = json.loads(results)
				res_name = []
				res_addr = []
				res_rating = []
				res_price = []
				res_cuisine = [] 
				for restaurant in d['restaurants']:
					res_name.append(restaurant['restaurant']['name'])
					res_addr.append(restaurant['restaurant']['location']['address'])
					res_rating.append(restaurant['restaurant']['user_rating']['aggregate_rating'])
					res_price.append(restaurant['restaurant']['average_cost_for_two'])
					res_cuisine.append(restaurant['restaurant']['cuisines'])
				df=pd.DataFrame({'Name':res_name,'Address':res_addr,'Budget':res_price,'Rating':res_rating,'Cuisine':res_cuisine})
				df['Rating'] = df['Rating'].apply(pd.to_numeric)
				if price == 'Lesser_300':
					df_filtered=df[df['Budget'] < 300]
				elif price == 'In_Between_300_To_700':
					df_filtered=df[(df['Budget'] >= 300) & (df['Budget'] <= 700)]
				elif price == 'More_700':
					df_filtered=df[df['Budget'] > 700]
				else:
					df_filtered=df	
				if len(df_filtered['Name'])==0:
					response= "We are sorry, we couldn't find any restaurent in your location."
					return None
				df_sorted=df_filtered.sort_values("Rating",ascending=False)
				df_sorted['Result_Message']="---> Restaurant \""+ df_sorted['Name']+ "\" found in "+ df_sorted['Address'] +\
							   		  " has been rated " + df_sorted['Rating'].astype(str) + "*/5" + " can cost you average " + df_sorted['Budget'].astype(str) + " RS. for 2 person."
				response='\n'.join(df_sorted['Result_Message'].head(10).tolist())
				# validate slot
				sender_email = "gargi.pdp@gmail.com"
				receiver_email = email_id
				password = "Donotknow@1"
				message = MIMEMultipart("alternative")
				message["Subject"] = "Gargi sent you best restaurent near you! Happy Meal..."
				message["From"] = sender_email
				message["To"] = receiver_email
				text = """\
				Hey Foodie, 
				
				I hope you are doing good!
				Below are the top 10 restaurents that I have found in your location. 
				"""
				html = """\
				<html>
				    <body>
					    <p> Hey Foodie, <br>
							<br> I hope you are doing good!<br>
							<br> Below are the top 10 restaurents that I have found in your location.<br> 
							<br>
							""" + response + """ <br> 
							<br> For more details kindely contact us.<br>
							Happy to help you. :) <br>
							<br> Thanks,
							<br> Gargi
							<br> <a href="https://www.zomato.com/">Visit Foodie App Here</a>
						</p>
					</body>
				</html>
				"""
				# Turning these into plain/html MIMEText objects
				part1 = MIMEText(text, "plain")
				part2 = MIMEText(html, "html")
				message.attach(part1)
				message.attach(part2)
				# Creating secure connection with server and send email
				context = ssl.create_default_context()
				with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
					server.login(sender_email, password)
					server.sendmail(
						sender_email, receiver_email, message.as_string()
					)
				dispatcher.utter_message("An email has been sent to your email-Id, Have a great meal!")
				return "Mail Sent!"
			else:
				dispatcher.utter_message("Please provide valid mail-id to proceed!")
				return {"email": None}
		else:
			# no entity was picked up, we want to ask again
			dispatcher.utter_message("Please provide valid mail-id to proceed!")
			return {"email": None}
		
class CheckCity(Action):
	def name(self):
		return 'action_check_location'
		
	def run(self, dispatcher, tracker, domain):
		if (tracker.get_slot('location')):
			#dispatcher.utter_message(tracker.get_slot('location'))
			loc = tracker.get_slot('location')
			if (loc.lower() not in [l.lower() for l in operating_cities]):
				dispatcher.utter_message("Currently we are not operating in your city, We are sorry for that. Can you please check for other location.")
				return [SlotSet("location", None)]

			return [SlotSet('location',loc)]

class CheckEmail(Action):
	def name(self):
		return 'action_valid_email_id'
		
	def run(self, dispatcher, tracker, domain):
		if tracker.get_slot('email'):
			#dispatcher.utter_message(tracker.get_slot('email'))
			email = tracker.get_slot('email')
			if (re.search('[A-z0-9]+@[A-z0-9]+[.][A-z]+[.]?[A-z]*',email)):
				return [SlotSet("email", email)]
			else:
				dispatcher.utter_message("Please re-enter your valid E-mail ID to proceed!")
				return [SlotSet("email", None)]
		else:
			dispatcher.utter_message("Please re-enter your valid E-mail ID to proceed!")
			return [SlotSet("email", None)]

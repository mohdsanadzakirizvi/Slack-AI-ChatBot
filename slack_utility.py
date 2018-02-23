"""
file: slack_utility.py
author: sanad(https://github.com/mohdsanadzakirizvi)
desc: contains utility functions for the project
license: MIT
"""
from slackclient import SlackClient
from os import environ
from time import sleep

def connect():
	"""
	Initiate a connection to Slack API
	"""
	API_KEY = get_slack_token()
	slack_api_client = SlackClient(API_KEY)
	return slack_api_client

def get_users():
	"""
	Fetch a dictionary of username and their IDs from Slack
	"""
	slack_api_client = connect()
	api_call = slack_api_client.api_call('users.list')
	if api_call.get('ok'):
		user_list = dict([(x['name'], x['id']) for x in api_call['members']])
		return user_list
	else:
		print 'Error Fetching Users'
		return None

def get_bot_id(botname=''):
	"""
	Get BOT_ID using botname and set in the env variable BOT_ID
	"""
	if environ.get('BOTNAME'):
		botname = environ.get('BOTNAME')
	else:
		print 'BOTNAME not set in the environment'
		return None

	if environ.get('SLACK_BOT_ID'):
		return environ.get('SLACK_BOT_ID')
	else:
		user_list = get_users()
		if user_list:
			BOT_ID = user_list[botname]
			environ.update({'SLACK_BOT_ID': BOT_ID})
			return BOT_ID
		else:
			print 'BOTNAME not present in user list'
			return None

def get_slack_token():
	"""
	Get SLACK_TOKEN from environment variable
	"""
	if environ.get('SLACK_TOKEN'):
		return environ.get('SLACK_TOKEN')
	else:
		print 'SLACK_TOKEN not set in the environment'
		return None

def parse_slack_response(rtm_output):
	"""
	Parse slack responses that are aimed at the bot else return None
	"""
	AT_BOT = '<@'+get_bot_id()+'>'
	if rtm_output and len(rtm_output):
		for output in rtm_output:
			if output and 'text' in output:
				if AT_BOT.lower() in output['text'].lower():
					return output['text'].split(AT_BOT)[1].strip(), output['channel']
	return None, None 


"""
file: mainbot.py
author: sanad(https://github.com/mohdsanadzakirizvi)
desc: contains primary code of the bot
license: MIT
"""
import slack_utility
import time

def handle_command(slack_api, command, channel):
	"""
	Recieves commands directed for the bot, if they are valid perform action 
	else resends clarification
	"""
	EXAMPLE_COMMAND = 'do'
	if command.lower().startswith(EXAMPLE_COMMAND) or command.lower().startswith('what'):
		slack_api.rtm_send_message(channel, 'Yes, code me further to do that!')
	elif command.lower().startswith('hi') or command.lower().startswith('hello') or command.lower().startswith('who are you'):
		slack_api.rtm_send_message(channel, 'Hey, I\'m your slack bot, how may I help you?')
	else:
		print 'Invalid Command: Not Understood'
		slack_api.rtm_send_message(channel, 'Invalid Command: Not Understood')
	
def main():
	"""
	Initiate the bot and call appropriate handler functions
	"""
	READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
	slack_api = slack_utility.connect()
	if slack_api.rtm_connect():
		print 'SLACK_BOT connected and running'
		while True:
			command, channel = slack_utility.parse_slack_response(slack_api.rtm_read())
			if command and channel:
				handle_command(slack_api, command, channel)
			time.sleep(READ_WEBSOCKET_DELAY)
	else:
		print 'Connection failed. Invalid Slack token or bot ID?' 

if __name__ == '__main__':
	main()
# Slack-AI-ChatBot


A simple rule based chatbot to connect to slack using python.

## Project Structure
The following is the project structure:

 - mainbot.py : main code of the slackbot
 - slack_utility.py : contains utility functions for the slackbot

## Start Project
 
 1. Set the SLACK_TOKEN and BOTNAME environment variable with your token and bot's name respectively 
 ```
 $ export SLACK_TOKEN=<your_token_here>
 $ export BOTNAME=<your_botname_here>
 ```
 2. Start the slackbot 
 ```python
 python mainbot.py
 ```
 3. Join the Slack Workplace
 ```
 https://<your_workspace_here>.slack.com/
 ```
 4. Try chatting with your bot. Start by saying "Hi"!
 :D
## Dependencies
The project depends upon the following packages:

 - python2.7
 - [slackclient](https://github.com/slackapi/python-slackclient)

## License

MIT
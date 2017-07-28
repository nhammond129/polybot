import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

HELP="""\
`ext.core`
```bash
help $EXTENSION
	Get the help message for $EXTENSION
invite
	Post the link for inviting the bot to a server.
github
	Post the link for the Github repo of this bot.
whois $NAME
	See info about user, strict matching.
whoami
	See info about bot user.
ping
	pong
uptime
	Get bot uptime
extensions|ext
	Get a list of loaded extensions
```
"""

async def digest(message,bot):
	if message.content[0] in bot.commandPrefix:
		tokens=tokenize(message)
		tokens[0]=tokens[0][1:]
		if isMatch(tokens[0],"help") | isMatch(tokens[0],"helb"):
			if len(tokens)==1:
				await bot.send_message(
						message.channel,
						"Try passing an extension to see the **help** message for it.\n"
						"_Example:_ `!help channel`\n"
						"You can use `!extensions` to get a list of loaded extensions."
						)
			else:
				if not tokens[1][:4]=="ext.":
					tokens[1]="ext."+tokens[1]
				try:
					hlpmsg=bot.extensions[tokens[1]].HELP
				except:
					hlpmsg="Could not parse extension `%s`."%tokens[1]
				await bot.send_message(
						message.channel,
						hlpmsg
						)
		elif isMatch(tokens[0],"invite"):
			await bot.send_message(
				message.channel,
				"https://discordapp.com/oauth2/authorize?&client_id=233829317245796352&scope=bot&permissions=0"
				)
		elif isMatch(tokens[0],"github"):
			await bot.send_message(
				message.channel,
				"https://github.com/Nullspeaker/polybot/"
				)
		elif isMatch(tokens[0],"whois"):
			target = message.server.get_member_named(tokens[1])
			await bot.send_message(
				message.channel,
				"%s,\n"
				"Their ID is `%s` \n"
				"Their discriminator is `%s` \n"
				"Joined at `%s` \n"
				"Is %sa bot."%(
					target.name,
					target.id,
					target.discriminator,
					str(target.joined_at),
					"not "*(1-target.bot)
					)
				)
		elif isMatch(tokens[0],"whoami"):
			await bot.send_message(
				message.channel,
				"%s,\n"
				"Your ID is `%s` \n"
				"Your discriminator is `%s` \n"
				"Joined at `%s` \n"
				"You are %sa bot."%(
					message.author.name,
					message.author.id,
					message.author.discriminator,
					str(message.author.joined_at),
					"not "*(1-message.author.bot)
					)
				)
		elif isMatch(tokens[0],"ping"):
			await bot.send_message(
				message.channel,
				"pong"
				)
		elif isMatch(tokens[0],"uptime"):
			await bot.send_message(
				message.channel,
				"I've been up for %s"%bot.getUptime()
				)
		elif isMatch(tokens[0],('extensions','ext')):
			await bot.send_message(
				message.channel,
				"```%s```"%("\n".join(bot.extensions.keys()))
				)
	else:
		pass

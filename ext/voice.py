import sys
import asyncio
import discord
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

HELP="""\
`ext.voice`
```bash
voice $FILE
    Plays the appropriate voice file.
voice help
voice list
    List the possible voice files.
```
"""
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')
VOX={
    "gonnafun": "/home/nullspeaker/python/polybot/gonnafun.mp3",
    "same": "/home/nullspeaker/python/polybot/same.mp3",
    "simplememer": "/home/nullspeaker/python/polybot/simplememer.mp3",
    "whatsinthebox": "/home/nullspeaker/python/polybot/WHATSINTHEBOX.mp3",
    "samecanyousee": "/home/nullspeaker/python/polybot/ohsamecanyousee.mp3",
    "moardots": "/home/nullspeaker/python/polybot/moredots.mp3"
    }

async def digest(message,bot):
    if message.content[0] in bot.commandPrefix:
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
        print(tokens)
        if isMatch(tokens[0],"voice"):
            if isMatch(tokens[1],"help") or isMatch(tokens[1],"list"):
                await bot.send_message(
                        message.channel,
                        " | ".join(VOX.keys())
                        )
            elif isMatch(tokens[1],"stop"):
                try:
                    player = bot.voice_client_in(
                            message.channel.server
                            ).player
                    player.stop()
                except:
                    pass
            elif tokens[1].lower() in VOX.keys():
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    if not bot.voice_channel == message.author.voice_channel:
                        await bot.join_voice_channel(
                                message.author.voice_channel
                                )
                else:
                    await bot.join_voice_channel(
                            message.author.voice_channel
                            )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = vc.create_ffmpeg_player(VOX[tokens[1].lower()])
                player.start()
            else:
                pass
        else:
            pass
    else:
        pass

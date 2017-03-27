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
    "gonnafun": "/home/ec2-user/python/polybot/gonnafun.mp3",
    "same": "/home/ec2-user/python/polybot/same.mp3",
    "simplememer": "/home/ec2-user/python/polybot/simplememer.mp3",
    "whatsinthebox": "/home/ec2-user/python/polybot/WHATSINTHEBOX.mp3",
    "samecanyousee": "/home/ec2-user/python/polybot/ohsamecanyousee.mp3",
    "moardots": "/home/ec2-user/python/polybot/moredots.mp3"
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
                        "jc rr2 mycube gems pain bustin kurisutina mybrand bees?\n"
                        "donttouchthat tutturu~ succ stop snout\n"
                        "tellmeaboutthoseconquerorshouldersagain\n"
                        "YOUFACEJARRAXUS gameoverman whatsinthebox\n"
                        "same gonnafun simplememer samecanyousee\n"
                        "moarDOTs"
                        )
            elif isMatch(tokens[1],"gameoverman"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=u2ycDWywGls"
                        )
                player.start()
            elif tokens[1].lower() in VOX.keys():
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                            message.author.voice_channel
                            )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = vc.create_ffmpeg_player(VOX[tokens[1].lower()])
                player.start()
            elif isMatch(tokens[1],"YOUFACEJARRAXUS"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=TJs5_s0Fsbs"
                        )
                player.start()
            elif isMatch(tokens[1],"tellmeaboutthoseconquerorshouldersagain"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=gKqoZkp9bMU"
                        )
                player.start()
            elif isMatch(tokens[1],"stop"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=2k0SmqbBIpQ"
                        )
                player.start()
            elif isMatch(tokens[1],"succ"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=fPNdWnwuBDI"
                        )
                player.start()
            elif isMatch(tokens[1],"jc"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=ggKeB9OOkRY"
                        )
                player.start()
            elif isMatch(tokens[1],"tutturu~"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=HkGNeN0LGOE"
                        )
                player.start()
            elif isMatch(tokens[1],"donttouchthat"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=7_h0uAdFBYc"
                        )
                player.start()
            elif isMatch(tokens[1],"bees?"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=-1GadTfGFvU"
                        )
                player.start()
            elif isMatch(tokens[1],"mybrand"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=V-fRuoMIfpw"
                        )
                player.start()
            elif isMatch(tokens[1],"kurisutina"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=a-GqSWsISVs"
                        )
                player.start()
            elif isMatch(tokens[1],"rr2"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=0NlfQdH5MSg"
                        )
                player.start()
            elif isMatch(tokens[1],"mycube"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=Uf-5l2nebRE"
                        )
                player.start()
            elif isMatch(tokens[1],"pain"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=KSI03_RPVTU"
                        )
                player.start()
            elif isMatch(tokens[1],"bustin"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=ybcS7CP4Om0"
                        )
                player.start()
            elif isMatch(tokens[1],"snout"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=dCO8fj_DQQo"
                        )
                player.start()
            elif isMatch(tokens[1],"gems"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=34f6RZDDBI4"
                        )
                player.start()
            else:
                pass
        else:
            pass
    else:
        pass

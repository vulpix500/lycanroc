import nextcord
import os
import time
from keep_alive import keep_alive
import nextcord.ext
from nextcord.utils import get
from nextcord.ext import commands, tasks
from nextcord.ext.commands import has_permissions, CheckFailure, check
import asyncpraw
import random
import asyncio
import json
import aiohttp
from aiohttp import *
import sys
from PIL import Image
from io import BytesIO


client = nextcord.Client()



os.system("clear")
print("hello world")

prefix = ["piplup!","Piplup!", "p!", "P!"]

reddit = ["memes","dankmemes","meme","pokemon"]

ball = ["yes","no","not 100% sure","https://media.discordapp.net/attachments/903023125158047845/926926969138995230/IMG_1448.png","https://media.discordapp.net/attachments/925905190073270322/926941827884519445/IMG_1451.png","to busy to say rn","idk","ask joe"]

Ruffs = ["812779224183209985", "849695984086286347"]

client = commands.Bot(command_prefix=prefix,help_command=None)

@client.listen("on_command_completion")
async def command_listener(ctx: commands.Context):
  channel = client.get_channel(925843393660211281)
  await channel.send(f"{ctx.author} used {ctx.command.name} in {ctx.guild.name} {ctx.guild.id}")


@client.event
async def on_ready():
    print("ok")
    await client.change_presence(activity=nextcord.Game(f"im in {len(client.guilds)} servers | https://twitter.com/DiscordPiplup"))

@client.command()
async def help(ctx):
 embed=nextcord.Embed(title="my commands", color=0x066aff)
 embed.add_field(name="avatar", value="shows your avatar", inline=False)
 embed.add_field(name="ban", value="bans mentioned user", inline=False)
 embed.add_field(name="kick", value="kicks mentioned user", inline=False)
 embed.add_field(name="invite", value="sends a embed containing my invite", inline=False)
 embed.add_field(name="purge ", value="deletes any amount of messages", inline=False)
 embed.add_field(name="snipe", value="shows last deleted message", inline=False)
 embed.add_field(name="screenshot", value="shows a screenshot of any website", inline=False)
 embed.add_field(name="dm", value="dm's mentioned user with any message", inline=False)
 embed.add_field(name="support", value="sends link to my support server", inline=False)
 embed.add_field(name="pokedex", value="shows the pokedex entery for any pokemon (dub names only)", inline=False)
 embed.add_field(name="mcfind",  value="shows the account with the name you entered (java only)",inline=False)
 embed.add_field(name="emoji",  value="show a enlarged version of any custom emoji",inline=False)
 embed.set_footer(text="did you know i have a twitter do v!twitter for more information")
 embed.add_field(name="8ball", value="ask the 8 ball any question... it will awnser correctly", inline=False)
 embed.add_field(name="createinvite (ci for short)", value="this will create a temporery invite for the server you enter the id off", inline=False)
 embed.set_image(url="https://images-ext-2.discordapp.net/external/eOYiZfD0TsK57SoBdmvZqfI45MjgYRKmslwOIlJ0DcU/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/926892516895256636/f6ce035d2ec124721e5d62e2334001fd.png")
 await ctx.send(embed=embed)
  


@client.command(aliases= ["av"])
async def avatar(ctx, *, member: nextcord.Member=None): # set the member object to None
 if not member: # if member is no mentioned or stuff
  member = ctx.message.author # set member as the author
 userAvatar = member.avatar.url
 embed = nextcord.Embed(title= f"nice avatar {member} ඞ",color=0x066aff)
 embed.set_image(url=userAvatar)
 
 await ctx.reply(embed=embed)

@client.command() 
async def say (ctx,*,message):
  #if "@everyone" or "@here" in message:
  #await ctx.reply("no")
 #else:
  await ctx.send(f"{message}")
  await ctx.message.delete()

@client.command(aliases=["inv"])
async def invite(ctx):
 embed = nextcord.Embed(title="invite me",description="[click here](https://discord.com/api/oauth2/authorize?client_id=926892516895256636&permissions=8&scope=bot)", color=0x066aff)
 await ctx.reply(embed=embed)



@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True) 
async def purge(ctx, limit: int): 
  await ctx.channel.purge(limit=limit) 
  await ctx.reply('purged by {}'.format(ctx.author.mention)) 
  await ctx.message.delete()


@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : nextcord.Member=None, reason=None):
    if member == None or member == ctx.message.author:
        embed1 = nextcord.Embed(title="ERROR:", description="You can not ban yourself.", color=0x066aff)
        await ctx.reply(embed=embed1)
        return
    if reason == None: 
        reason = 'Reason not given.'
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.reply(f"{ctx.message.author} banned {member} from server. Reason:{reason}")

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : nextcord.Member=None, reason=None):
    if member == None or member == ctx.message.author:
        embed1 = nextcord.Embed(title="ERROR:", description="You can not kick yourself.", color=0x066aff)
        await ctx.reply(embed=embed1)
        return
    if reason == None: 
        reason = 'Reason not given.'
        await ctx.guild.kick(member, reason=reason)
        await ctx.channel.reply(f"{ctx.message.author} kicked {member} from server. Reason:{reason}")


snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content

@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try:
        em = nextcord.Embed(description = f"`{snipe_message_content[channel.id]}`\nMessage sent by {snipe_message_author[channel.id]}!", color = 0x00c230)
        em.set_author(name = f"Last deleted message in #{channel.name}")
        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/352793093105254402/8a2018de21ad29973696bfbf92fc31cd.png?size=4096")
        em.set_footer(text = f"Snipe requested by {ctx.message.author}")
        await ctx.reply(embed = em)
    except:
     embed = nextcord.Embed(colour = 0x00c230)
     embed.set_author(name=f"There are no deleted messages in #{ctx.channel}!")
     embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/352793093105254402/8a2018de21ad29973696bfbf92fc31cd.png?size=4096")
     embed.set_footer(text=f"Snipe requested by {ctx.message.author}")
     await ctx.channel.reply(embed=embed)

@client.command()
async def twitter(ctx):
 embed = nextcord.Embed(title="my twitter", description="[click here](https://twitter.com/DiscordPiplup)")
 await ctx.reply(embed=embed)

@client.command()
async def ss(ctx, site):
    embed=nextcord.Embed(colour = 0x066aff, timestamp=ctx.message.created_at)
    embed.set_image(url=(f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/https://{site}"))
    await ctx.reply(embed=embed)

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command(aliases= ["rs"])
@commands.is_owner()
async def restart(ctx):
      await ctx.send("Restarting bot...")
      restart_bot()

@client.command()
async def id(ctx, member: nextcord.Member=None):
 if not member:
  member = ctx.message.author
  await ctx.reply(ctx.author.id)

@client.command()
async def dm(ctx, user: nextcord.User, *, message=None):
    user = ctx.author
    if message == None:
      message = f"well.... {user} forgot to tell me what to say"
    await ctx.reply("no messaage? try telling me what to say")
    embed = nextcord.Embed(title="you have got a message", description=message, color=0x066aff)
    await user.send(embed=embed)
    await ctx.reply("Message sent!")

@client.command()
async def support(ctx):
  embed = nextcord.Embed(title="my support server",
  description="[click here](https://discord.gg/QCkcSXBQ)")
  embed.add_field(name="also follow my twitter", value="[click here](https://twitter.com/lilliebot_)", inline=False)
  await ctx.reply(embed=embed)

@client.command()
async def vcid(ctx):
 embed = nextcord.Embed(description=ctx.author.voice)
 await ctx.reply(embed=embed)


  
@client.command()
async def emoji(ctx, emoji: nextcord.Emoji):
  embed=nextcord.Embed(title="here is your emoji")
  embed.set_image(url=emoji.url)
  await ctx.reply(embed=embed)

@client.command()
async def serverid(ctx):
 await ctx.reply(ctx.message.guild.id)


  
#https://www.pokemon.com/uk/pokedex/{message}

@client.command(aliases= ["pokèdex"])
async def pokedex(ctx,message=None):
  if message == None:
    await ctx.send("choose a pokemon")
  else:
    embed=nextcord.Embed(title=f"pokedex entry for {message}",description = f"want the full pokedex entry [click here](https://pokemondb.net/pokedex/{message})" ,colour = 0x066aff)
    embed.set_image(url=(f"https://play.pokemonshowdown.com/sprites/xyani/{message}.gif"))
    embed.set_footer(text="if you want a regional variant of a pokemon its v!pokedex <pokemon name>-<regon> for example v!pokedex vulpix-alola")
    await ctx.reply(embed=embed)


@client.command()
async def lillie(ctx):
    id = str(ctx.author.id)
    if id == '896792834387112026':
     embed=nextcord.Embed(title="Hello miss lillie", color=0xff00f8)
     embed.set_image(url="https://media.discordapp.net/attachments/914985889145421825/918907284749447178/B6E1330B-0FE9-492D-A3FE-CE17B649BC82.jpg")
     await ctx.reply(embed=embed)


@client.command(aliases=["findmc"])
async def mcfind(ctx,message=None):
 if message == None:
   await ctx.send("tell me what minecraft account you want to see")
 else:
    embed = nextcord.Embed(title=f"here is the minecraft account you requested", description=f"[{message}](https://namemc.com/profile/{message}.1)", color=0x066aff)
    embed.set_image(url=f"https://minecraftskinstealer.com/api/v1/skin/render/fullbody/{message}/700")
    embed.set_footer(text="the image above this text is the skin the user is currently wearing")
    await ctx.reply(embed=embed)
 #if arg1 == None:
  # await ctx.send("please choose a minecraft account to view")
 

@client.command()
async def embed(ctx, *,message):
 embed = nextcord.Embed(description=message)
 await ctx.reply(embed=embed)

#https://minecraftskinstealer.com/api/v1/skin/render/fullbody/danTDM/700

@client.command(pass_context=True)
async def meme(ctx):
    embed = nextcord.Embed(title=f"here is your meme {ctx.author.mention}", description="",colour=0x066aff)

    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://www.reddit.com/r/{random.choice(reddit)}/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.reply(embed=embed)



@client.command()
async def move(ctx,message=None):
 if message == None:
   await ctx.send("please enter a channel id")
 else:
  embed = nextcord.Embed(title="move to a diffrent channel", description=f"staff member {ctx.author.name} has requested you continue this conversation in <#{message}> this is so we can keep {ctx.guild.name} tidy", colour=0x066aff)
  await ctx.reply(embed=embed)


@client.command()
async def howgay(ctx):
 id = str(ctx.author.id)
 if id == '812779224183209985':
   await ctx.send("error: user is to gay for this machine")
 else:
  await ctx.reply(f"{ctx.author.mention} is {random.randint(0,100)}% gay")



@client.command(aliases= ["8ball"])
async def eightball(ctx,message=None):
 if message == None:
  await ctx.send("what question do you want me to awnser")
 else:
  await ctx.reply(random.choice(ball))

@client.command(aliases= ["ci"])
async def createinvite(ctx, guildid: int=None):
  if int == None:
   ctx.send("enter a server id")
  else:
   try:
    guild = client.get_guild(guildid)
    invitelink = ""
    i = 0
    while invitelink == "":
      channel = guild.text_channels[i]
      link = await channel.create_invite(max_age=300,max_uses=1)
      invitelink = str(link)
      i += 1
    await ctx.reply(invitelink)
   except Exception:
    await ctx.reply("please enter a vaild guild id | btw i need to be in the sever for this command to work")

@client.command()
async def spam(ctx,message):

  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send(message)
  await ctx.send ("LOL")

@client.command()
async def gwen(ctx, user: nextcord.Member = None):
 if user == None:
   user = ctx.author
   gwened = image.open("gwen.png")
   asset = ctx.author.avatar_url_as(size = 128)
   data = bytesIO(await asset.read())
   pfp = Image.open(data)
 pfp = pfp.resize((643,1250))
 gwened.paste(pfp,69,420)
 gwened.save("gwen.png") 
 await ctx.reply("gwen.png")




testingserverid = 890566405773226014

@client.slash_command(guild_ids=[testingserverid])
async def hi(interaction: nextcord.Interaction):
  await interaction.response.send_message("hi")



@client.command(name="ui")
async def userinfo(ctx, *, user: nextcord.User = None): 
    if user is None:
        user = ctx.author  
    created_at = user.created_at.strftime("%d %m, %Y")    
    embed = nextcord.Embed(title=f"info about {user}")
    embed.add_field(name=f"{user} joined discord on  ", value=f"{created_at}", inline=False)
    userAvatar = user.avatar.url
    embed.add_field(name="avatar", value=f"[click here]({userAvatar})")
    await ctx.reply(embed=embed)

  
keep_alive()  # DONT PUT ANYTHING UNDER HER1E OR U WILL GET AN ERROR

client.run(os.getenv("TOKEN"))
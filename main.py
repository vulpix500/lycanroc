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
from nextcord import Interaction, SlashOption
from time import sleep

client = nextcord.Client()



os.system("clear")
print("hello world")

prefix = ["piplup!","Piplup!", "p!", "P!"]

reddit = ["memes","dankmemes","meme","pokemon"]

ball = ["yes","no","not 100% sure","to busy to say rn","idk","ask joe"]

Ruffs = ["812779224183209985", "849695984086286347"]

ruffsserverid = 890566405773226014

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
 embed.set_image(url="https://images-ext-2.discordapp.net/external/aAxkZ9LQQnNrWaUwOMg6wAKpHEJFzxpkzgpLjlXi-9Q/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/926892516895256636/3713f22e6d0c08aa7c25bda28fc7d566.png")
 await ctx.send(embed=embed)
  


@client.command(aliases= ["av"])
async def avatar(ctx, *, member: nextcord.Member=None): # set the member object to None
 if not member: # if member is no mentioned or stuff
  member = ctx.message.author # set member as the author
 userAvatar = member.avatar.url
 embed = nextcord.Embed(title= f"nice avatar {member} ඞ",color=0x066aff)
 embed.set_image(url=userAvatar)



@client.slash_command(guild_ids=[],description="my invite command")
async def invite(interaction: Interaction):
  embed = nextcord.Embed(title="invite",description="https://discord.com/api/oauth2/authorize?client_id=926892516895256636&permissions=8&scope=bot%20applications.commands",colour=0x066aff)
  await interaction.send(embed=embed)


@client.slash_command(guild_ids=[890566405773226014],description="deletes an amount of messages")
@commands.has_permissions(manage_messages=True) 
async def purge(interaction: Interaction, purge_amount: str = SlashOption(description="command description")): 
  await interaction.channel.purge(purge_amount)


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

@client.slash_command(guild_ids=[], description="shows screenshot of any website")
async def ss(interaction: Interaction, url: str = SlashOption(description="command description")):
    embed=nextcord.Embed(title=" ",colour = 0x066aff)
    embed.set_image(url=(f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/https://{url}"))
    await interaction.send(embed=embed)

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.slash_command(guild_ids=[890566405773226014],description="dev only command nice try")
async def restart(interaction: Interaction):
  if interaction.user.id == 849695984086286347:
      await interaction.send("Restarting bot...")
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

@client.slash_command(guild_ids=[], description="shows a pokedex entery for any pokemon")
async def pokedex(interaction: Interaction,pokemon: str = SlashOption(description="enter pokemon name")):
    embed=nextcord.Embed(title=f"pokedex entry for {pokemon}",description = f"want the full pokedex entry [click here](https://pokemondb.net/pokedex/{pokemon})" ,colour = 0x066aff)
    embed.set_image(url=(f"https://play.pokemonshowdown.com/sprites/xyani/{pokemon}.gif"))
    embed.set_footer(text="if you want a regional form it would be region-pokemon")
    await interaction.send(embed=embed)


@client.slash_command(guild_ids=[], description="lets you have a pokemon battle with any pokemon vs ash kechum")
async def mcfind(interaction: Interaction,username: str = SlashOption(description="have a pokemon battle with ash")):
    embed = nextcord.Embed(title=f"here is the minecraft account you requested", description=f"[{username}](https://namemc.com/profile/{username}.1)", color=0x066aff)
    embed.set_image(url=f"https://minecraftskinstealer.com/api/v1/skin/render/fullbody/{username}/700")
    embed.set_footer(text="the image above this text is the skin the user is currently wearing")
    await interaction.send(embed=embed)

  #Interaction

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



@client.slash_command(guild_ids=[], description="ask the magic 8ball any question")
async def _8ball(interaction: Interaction, question: str = SlashOption(description="ask the magic 8ball any question")):
 await interaction.send(f"your question is **{question}** my awnser is **{random.choice(ball)}**")
  
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


@client.command(name="ui")
async def userinfo(ctx, *, user: nextcord.User = None): 
    if user is None:
        user = ctx.author  
    created_at = user.created_at.strftime("%d %m, %Y")    
    userAvatar = user.avatar.url
    embed = nextcord.Embed(title=f"info about {user}")
    embed.add_field(name=f"{user} joined discord on  ", value=f"{created_at}", inline=False)
    embed.add_field(name="avatar", value=f"[click here]({userAvatar})")
    await ctx.reply(embed=embed)

1 == 1

@client.command()
async def spam(ctx,*,message):
 if ctx.author.id == 812779224183209985:
  while 1==1:
    await ctx.send(message)
 else:
  print(f"ctx.author.name tried to use spam rip bozo")
   
@client.command()
@commands.is_owner()
async def servers(self, ctx):
        activeservers = client.guilds
        for guild in activeservers:
            await ctx.send(guild.id)
            print(guild.name)

@client.command()
@commands.is_owner()
async def plaininvite(ctx):
 await ctx.send("https://discord.com/api/oauth2/authorize?client_id=926892516895256636&permissions=8&scope=bot%20applications.commands")

trolled = ["https://tenor.com/view/troll-pilled-gif-19289988","https://media.tenor.co/videos/a4e9ad8842c178e4f24211bdc0b1f04b.gif","https://tenor.com/view/troll-stick-figure-dancing-gif-5259835"]

@client.command()
async def troll(ctx, *, user: nextcord.User = None, member: nextcord.Member ):
 if user is None:
       await member.send("dont troll youself dumbass @ someone else to troll them")
 embed = nextcord.Embed(title=f"{user} got trolled",colour=0x066aff)
 await ctx.reply(embed=embed)
 await ctx.send(random.choice(trolled))



@client.slash_command(guild_ids=[], description="Repeats your message")
async def say(interaction: Interaction, message: str = SlashOption(description="Message")):
    await interaction.response.send_message(message)

@client.slash_command(guild_ids=[], description="Repeats your message in an embed")
async def embed(interaction: Interaction,title,body: str = SlashOption(description="Message")):
  embed = nextcord.Embed(title=title,description=body,color=0x066aff)
  await interaction.send(embed=embed)


ash_pokemon = ["rowlet","lycanrock","torracat","melmetal","Naganadel","pikachu"]


@client.command(aliases=["pokebattle"])
async def pokemonbattle(ctx, *, message=None):
  user = ctx.author
  pokewinner = [f"{user}","ash Ketchum",f"{user}"]
  if message == None:
    await ctx.send(f"{ctx.author.mention} please send out a pokemon")
  else:
   embed = nextcord.Embed(title=f"battle between ash ketchum and {user} is ready to start", description=f"{user} has chosen {message} and ash has chosen {random.choice(ash_pokemon)}",colour=0x066aff)
  await ctx.reply(embed=embed)   
  sleep(5)
  await ctx.send(f"the battle has ended with {random.choice(pokewinner)} being the winner")

#interaction: Interaction, string: str = SlashOption(description="command description")):

@client.slash_command(guild_ids=[890566405773226014], description="lets you have a pokemon battle with any pokemon vs ash kechum")
async def slashpoke(interaction: Interaction,pokèmon: str = SlashOption(description="have a pokemon battle with ash")):
  user = interaction.user
  pokewwinner = [f"{user}","ash Ketchum",f"{user}"]
  embed = nextcord.Embed(title=f"battle between ash ketchum and {user} is ready to start", description=f"{user} has chosen {pokèmon} and ash has chosen {random.choice(ash_pokemon)}",colour=0x066aff)
  await interaction.response.send_message(embed=embed)   
  sleep(5)
  winnerembed = nextcord.Embed(title="we have a winner",description=f"the battle has ended with {random.choice(pokewwinner)} being the winner",colour=0x066aff)


scorbunnygifs = ["https://tenor.com/view/scorbunny-pokemon-cute-smile-excited-gif-16467394","https://tenor.com/bq7jg.gif","https://tenor.com/view/pok%C3%A9mon-pokemon-scorbunny-flambino-cute-gif-18817016","https://tenor.com/view/pokemon-anime-cinderace-soccer-football-gif-21196259”,”https://tenor.com/view/dance-scorbunny-happy-celebrate-jumping-gif-17224759","https://tenor.com/view/scorbunny-pikachu-eating-hungry-pokemon-gif-16467383","https://tenor.com/view/happy-scorbunny-cute-pokemon-gif-19455153"]

@client.slash_command(guild_ids=[], description="daily does of scorbunny")
async def scorbunny(interaction: Interaction):
 await interaction.send(random.choice(scorbunnygifs))

@client.command(guild_ids=876519923055198208)
async def test(interaction: Interaction, pokemon: str = SlashOption(description="command description")):
  async with aiohttp.ClientSession() as cs:
        async with cs.get("https://some-random-api.ml/pokedex?pokemon=pokemon") as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await interaction.send(embed=embed)

keep_alive()  # DONT PUT ANYTHING UNDER HER1E OR U WILL GET AN ERROR

client.run(os.getenv("TOKEN"))
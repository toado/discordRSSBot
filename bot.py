from discord.ext.commands import Bot
from discord.ext.tasks import loop
import discord
import random
import time
import feedparser
import botToken

BOT_PREFIX = '~'
TOKEN = botToken.token()
post_list = []

client = Bot(command_prefix=BOT_PREFIX)

# -------------------- clear function to purge x amount of messages -------------------- #
@client.command()
async def clear(ctx, amount=1):
  purged = await ctx.channel.purge(limit=amount+1)  # returns lists of messages

# ----------------------- Function to Ban/Unban a specified user ---------------------- #

@client.command()
async def ban(ctx, member:discord.Member, *, reason=None):
  if (member == ctx.message.author):
    await ctx.send('You can\'t ban yourself')
    return
  await member.ban(reason=reason)
  await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, user):
  banned_list = await ctx.guild.bans()
  user_name, user_discriminator = user.split('#')

  for banned in banned_list:
    banned_user = banned.user
    if (user_name, user_discriminator) == (banned_user.name, banned_user.discriminator):
      await ctx.guild.unban(banned_user)  
      await ctx.send(f'{user} has been unbanned')

@client.command(name='banlist',
                aliases=['banned', 'banned_list'])
async def ban_list(ctx):
  bans = await ctx.guild.bans()
  for ban in bans:
    await ctx.send(f'>>> __**User & ID:**__ {ban.user.name}#{ban.user.discriminator}\n__**Reason**__: {ban[0]}\n')


# ---------------- RSS feedparser function on bapcsalescanada subreddit ---------------- #
# checks for new posts on the specified subreddit every 5 minutes for a new post
@client.command()
async def sales(ctx):
  update.start(ctx)

@loop(seconds=240)
async def update(ctx):
  d = feedparser.parse('https://www.reddit.com/r/bapcsalescanada/new/.rss')
  post = d.entries[0]['title']
  link = d.entries[0]['link']

  if (post not in post_list):
    await ctx.send(f'> :hourglass::exclamation:**{post}**\n> \n> {link}')
    if (len(post_list) >= 1):
      post_list.pop()
    post_list.append(post)
    print('Ran if')

  else:
    print('Nothing')

# ------------------------ Shows the current status of the bot ------------------------ #
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!help'))
 
client.run(TOKEN)

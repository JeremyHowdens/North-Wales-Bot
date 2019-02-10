import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import youtube_dl

TOKEN = 'NTQyMTQzMTIyMTkzNTE0NTA3.DzrkmQ.MqAPSS60Fj5-C3dJjZyeqMs7zww'

client = commands.Bot(command_prefix = '$')
status = ['For help use $displayembed', 'This bot was created by JeremyHowdens']

players = {}

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(60)

@client.event
async def on_ready():
    print('Bot is Ready.')

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def group():
    await client.say('https://www.roblox.com/groups/3810559/North-Wales#!/about')

@client.command()
async def discordlinks():
    await client.say('https://discord.gg/H6eZ3mN, https://discord.gg/uRrMkYn')

@client.command()
async def displayembed():
    embed = discord.Embed(
        title = 'North Wales Bot',
        description = 'This bot was created and managed by JeremyHowdens',
        colour = discord.Colour.blue(),
    )

    embed.set_footer(text='Made by JeremyHowdens')
    embed.set_image(url='https://cdn.discordapp.com/attachments/496038123650678796/542290244691558415/5wyf6cXMG9-4.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/496038123650678796/542290244691558415/5wyf6cXMG9-4.png')
    embed.set_author(name = 'JeremyHowdens')
    embed.add_field(name='General Commands', value='$ping, $group, $discordlinks', inline=False)
    embed.add_field(name='Music Commands', value='music', inline=True)



    await client.say(embed=embed)

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)


@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()


@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()



@client.command()
async def logout():
    await client.logout()

client.loop.create_task(change_status())
client.run(TOKEN)

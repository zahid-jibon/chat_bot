import nextcord
from nextcord import Interaction
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("The Bot is now ready to USE")

testingServerID= 3932

@client.slash_command(name = "hello", description="Replies with hello", guild_ids= {testingServerID})
async def hellocommand(interaction: Interaction):
    await interaction.response.send_message("Hello")

client.run('OTg1OTc2MTY3NDM1NzMwOTQ1.Gkjmse.r2M2sZh0JreQrESHPLCwsgvsEG2Qt-4V8Nfjyk')



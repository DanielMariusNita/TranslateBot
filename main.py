import discord
from discord.ext import commands
from googletrans import Translator, LANGUAGES

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name + '!')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

def translate(text, initialLanguage, finalLanguage):

    # Check if the provided languages are valid
    if initialLanguage not in LANGUAGES or finalLanguage not in LANGUAGES:
        return "Invalid language code. Please use ISO 639-1 language codes."

    # Initialize the translator
    translator = Translator()

    # Translate the text
    translated_text = translator.translate(text, src=initialLanguage, dest=finalLanguage)

    return translated_text.text

@bot.command()
async def help(ctx):
    await ctx.send('> `$t li lf text` \n `li` = the abbreviation of the language of the text you inserted (ex: it, es, fr, fi, nl)\n`lf` = the abbreviation of the language you want to translate in (ex: en, nl ,ro) \n`text` = the text you want to translate' )

@bot.command()
async def t(ctx, ini, out, *arg):
    arguments = ', '.join(arg)
    translated=translate(arguments, ini, out)
    await ctx.send(f'{translated}')

bot.run('MTE1NjcwNTI3MzU4MzUxNzc0OQ.G2qajo.9KGCJod3tT4hVikvZr4SF1leHnPUcP7Gzbj7JQ')


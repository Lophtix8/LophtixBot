import discord
from discord.ext import commands
import aiohttp
import os

bot = commands.Bot(command_prefix="!!!", description="etymology bot")

@bot.command(aliases=["etym"])
async def etymology(ctx, lang, *, term):
    async with aiohttp.request("GET", f"https://en.wiktionary.org/wiki/{term.replace(' ', '_')}") as r:
        html = str(await r.read())

    output = ""
    headers = html.split("<h2>")
    for header in headers:
        if f"id=\"{lang}\"" in header:
            output=header.split("<h3>")
            for sub_header in output:
                if "id=\"Etymology" in sub_header:wwwwwwwwwwwwwwwwwwwwwwwwww
                    output=sub_header
                    break
                else:
                    output = "Etymology can't be found"
            break
    # filter etymology from website
    await ctx.send(os.getenv("TOKEN"))

bot.run()
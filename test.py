from ButtonPaginator import Paginator
from discord.ext.commands import Bot
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
import discord

bot = Bot("!!")


@bot.event
async def on_ready():
    DiscordComponents(bot)
    print(f"Logged in as {bot.user}!")


@bot.command()
async def button(ctx):
    embeds = [discord.Embed(title="1 page"), discord.Embed(title="2 page"), discord.Embed(title="3 page"), discord.Embed(title="4 page"), discord.Embed(title="5 page")]
    e = Paginator(bot=bot,
                  ctx=ctx,
                  embeds=embeds,
                  left_button_style=ButtonStyle.green,
                  right_button_style=ButtonStyle.green,
                  use_extend=True,
                  basic_buttons=["⬅️", "➡️"],
                  extended_buttons=["⏪", "⏩"],
                  only=ctx.author,
                  )
    await e.start()




bot.run("ODQ2Nzc4OTgyNDYzOTYzMTQ4.YK0eYQ.OmHveehBvpITehECgxpXlpQzE0M")
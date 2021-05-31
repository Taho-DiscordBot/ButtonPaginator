<div align="center">
    <div>
        <h1>Button Paginator</h1>
        <span> <a href="https://pypi.org/project/discord-components"><img src="https://raw.githubusercontent.com/kiki7000/discord.py-components/master/.github/logo.png" alt="discord-components logo" height="10" style="border-radius: 50%"></a>With discord-components</span>
    </div>
    <div>
    </div>
    <div>
        <h3>Button paginator using discord_components</h3>
    </div>
</div>

## Welcome!
It's a paginator for discord-componets! Thanks to the original creator khk4912 (khk4912 /EZPaginator)!

This project is open source ⭐.

[official discord server](https://discord.gg/pKM6stqPxS), so if you have a question, feel free to ask it on this server.
## Install
```
pip install --upgrade ButtonPaginator
```

## Example
```py
from ButtonPaginator import Paginator
from discord.ext.commands import Bot
from discord_components import DiscordComponents
import discord

bot = Bot("your prefix")

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
                  only=ctx.author)
    await e.start()

bot.run("your token")
```

## License
This project is under the MIT License.

## Contribute
Anyone can contribute to this by forking the repository, making a change, and create a pull request!

But you have to follow these to PR.
+ Use the black formatter.
+ Use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).
+ Test.

## Thanks to
+ [khk4912](https://github.com/khk4912/EZPaginator) - Original Paginator
+ [kiki7000](https://github.com/kiki7000/discord.py-components) - componets lib developer

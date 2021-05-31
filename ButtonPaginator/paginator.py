import discord
from discord.ext import commands

from typing import List, Optional, Union

from discord_components import (
    Button,
    ButtonStyle,
    InteractionType,
    Context,
)


class Paginator:
    def __init__(
        self,
        bot: Union[
            discord.Client,
            discord.AutoShardedClient,
            commands.Bot,
            commands.AutoShardedBot,
        ],
        ctx: Context,
        contents: Optional[List[str]] = None,
        embeds: Optional[List[discord.Embed]] = None,
        timeout: int = 30,
        use_extend: bool = False,
        only: Optional[discord.abc.User] = None,
        basic_buttons: Optional[List[str]] = None,
        extended_buttons: Optional[List[str]] = None,
        left_button_style: ButtonStyle = ButtonStyle.green,
        right_button_style: ButtonStyle = ButtonStyle.green,
        auto_delete: bool = False,
    ) -> None:
        self.bot = bot
        self.context = ctx
        self.contents = contents
        self.embeds = embeds
        self.timeout = timeout
        self.use_extend = use_extend
        self.only = only
        self.basic_buttons = ["⬅️", "➡️"]
        self.extened_buttons = ["⏪", "⬅️", "➡️", "⏩"]
        self.left_button_style = left_button_style
        self.right_button_style = right_button_style
        self.auto_delete = auto_delete
        self.page = 1

        if (
                isinstance(bot, discord.Client)
                or isinstance(bot, discord.AutoShardedClient)
                or isinstance(bot, commands.Bot)
                or isinstance(bot, commands.AutoShardedBot)
        ):
            pass
        elif (
                issubclass(bot, discord.Client)
                or issubclass(bot, discord.AutoShardedClient)
                or issubclass(bot, commands.Bot)
                or issubclass(bot, commands.AutoShardedBot)
        ):
            pass
        else:
            raise TypeError("This is not a discord.py related bot class.(only <discord.Client, <discord.AutoShardedClient>, <discord.ext.commands.Bot>, <discord.ext.commands.AutoShardedBot>)")





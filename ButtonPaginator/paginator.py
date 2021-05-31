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
        self.basic_buttons: basic_buttons
        self.extened_buttons = extended_buttons
        self.left_button_style = left_button_style
        self.right_button_style = right_button_style
        self.auto_delete = auto_delete
        self.page = 1
        pass

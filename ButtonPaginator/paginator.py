import discord
from discord.ext import commands

from typing import List, Optional, Union

from discord_components import (
    Button,
    ButtonStyle,
    InteractionType,
    Context,
)


from .errors import MissingAttributeException, InvaildArgumentException


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
        left_button_style: ButtonStyle = None,
        right_button_style: ButtonStyle = None,
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
        self.left_button_style = ButtonStyle.green
        self.right_button_style = ButtonStyle.green
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

        if contents is None and embeds is None:
            raise MissingAttributeException(
                "Both contents and embeds are None."
            )

        if not isinstance(timeout, int):
            raise TypeError("timeout must be int.")

        if basic_buttons is not None:
            if self.use_extend:
                raise InvaildArgumentException("use_extend should be False.")

            if len(set(self.basic_emojis)) != 2:
                raise InvaildArgumentException(
                    "There should be 2 elements in basic_emojis."
                )
            self.basic_emojis = basic_buttons

        if extended_buttons is not None:
            if not self.use_extend:
                raise InvaildArgumentException("use_extend should be True.")

            if len(set(self.extended_emojis)) != 4:
                raise InvaildArgumentException(
                    "There should be 4 elements in extended_emojis"
                )
            self.extended_emojis = extended_buttons

        if (
            isinstance(left_button_style, ButtonStyle.URL)
            or isinstance(right_button_style, ButtonStyle.URL)
        ):
            raise TypeError("Can't use <discord_component.ButtonStyle.URL> type for button style.")





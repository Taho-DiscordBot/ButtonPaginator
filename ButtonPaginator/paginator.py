import discord
from discord import InvalidArgument, PartialEmoji, Emoji
from discord.ext import commands

import asyncio
from typing import List, Optional, Union

from discord_components import (
    Button,
    ButtonStyle,
    InteractionType,
    Context,
)

from .errors import MissingAttributeException, InvaildArgumentException

EmojiType = List[Union[discord.Emoji, discord.Reaction, discord.PartialEmoji, str]]


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
        basic_buttons: Optional[EmojiType] = None,
        extended_buttons: Optional[EmojiType] = None,
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
        self.extened_buttons = ["⏪", "⏩"]
        self.left_button_style = left_button_style
        self.right_button_style = right_button_style
        self.auto_delete = auto_delete
        self.page = 1
        self._left_button = None
        self._right_button = None
        self._left2_button = None
        self._right2_button = None
        self._left_label = str()
        self._right_label = str()
        self._left2_label = str()
        self._right2_label = str()
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
            raise TypeError(
                "This is not a discord.py related bot class.(only <discord.Client, <discord.AutoShardedClient>, <discord.ext.commands.Bot>, <discord.ext.commands.AutoShardedBot>)"
            )

        if contents is None and embeds is None:
            raise MissingAttributeException("Both contents and embeds are None.")

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
            if isinstance(self.basic_emojis[0], Emoji):
                self._left_button = PartialEmoji(
                    name=self.basic_emojis[0].name,
                    animated=self.basic_emojis[0].animated,
                    id=self.basic_emojis[0].id,
                )
            elif isinstance(self.basic_emojis[0], PartialEmoji):
                self._left_button = self.basic_emojis[0]
            elif isinstance(self.basic_emojis[0], str):
                self._left_button = PartialEmoji(self.basic_emojis[0])
            else:
                self._left_label = str(self.basic_emojis[0])

            if isinstance(self.basic_emojis[1], Emoji):
                self._right_button = PartialEmoji(
                    name=self.basic_emojis[1].name,
                    animated=self.basic_emojis[1].animated,
                    id=self.basic_emojis[1].id,
                )
            elif isinstance(self.basic_emojis[1], PartialEmoji):
                self._right_button = self.basic_emojis[0]
            elif isinstance(self.basic_emojis[1], str):
                self._right_button = PartialEmoji(self.basic_emojis[1])
            else:
                self._right_label = str(self.basic_emojis[1])

        if extended_buttons is not None:
            if not self.use_extend:
                raise InvaildArgumentException("use_extend should be True.")

            if len(set(self.extended_emojis)) != 2:
                raise InvaildArgumentException(
                    "There should be 2 elements in extended_emojis"
                )
            self.extended_emojis = extended_buttons

            if isinstance(self.extended_emojis[0], Emoji):
                self._left2_button = PartialEmoji(
                    name=self.extended_emojis[0].name,
                    animated=self.extended_emojis[0].animated,
                    id=self.extended_emojis[0].id,
                )
            elif isinstance(self.extended_emojis[0], PartialEmoji):
                self._left2_button = self.extended_emojis[0]
            elif isinstance(self.extended_emojis[0], str):
                self._left2_button = PartialEmoji(self.extended_emojis[0])
            else:
                self._left2_label = str(self.extended_emojis[0])

            if isinstance(self.extended_emojis[1], Emoji):
                self._right2_button = PartialEmoji(
                    name=self.extended_emojis[1].name,
                    animated=self.extended_emojis[1].animated,
                    id=self.extended_emojis[1].id,
                )
            elif isinstance(self.extended_emojis[1], PartialEmoji):
                self._right2_button = self.extended_emojis[0]
            elif isinstance(self.extended_emojis[1], str):
                self._right2_button = PartialEmoji(self.extended_emojis[1])
            else:
                self._right2_label = str(self.extended_emojis[1])

        if isinstance(left_button_style, ButtonStyle.URL) or isinstance(
            right_button_style, ButtonStyle.URL
        ):
            raise TypeError(
                "Can't use <discord_component.ButtonStyle.URL> type for button style."
            )

    async def go_previous(self, payload: Context) -> None:
        if self.page == 0:
            return
        self.page -= 1
        if self.contents is None:
            await payload.respond(
                type=InteractionType.UpdateMessage,
                embed=self.embeds[self.page - 1],
                components=(await self.create_button()),
            )
        else:
            await payload.respond(
                type=InteractionType.UpdateMessage,
                content=self.contents[self.page - 1],
                components=(await self.create_button()),
            )

    async def go_next(self, payload: Context) -> None:
        if self.embeds is None:
            if self.page != len(self.embeds):
                self.page += 1
                await payload.respond(
                    type=InteractionType.UpdateMessage,
                    embed=self.embeds[self.page - 1],
                    components=(await self.create_button()),
                )
            elif self.contents is not None:
                if self.page != len(self.contents):
                    self.page += 1
                    await payload.respond(
                        type=InteractionType.UpdateMessage,
                        content=self.contents[self.page - 1],
                        components=(await self.create_button()),
                    )

    async def go_first(self, payload: Context) -> None:
        if self.page == 0:
            return
        self.page = 1

        if self.contents is None:
            await payload.respond(
                type=InteractionType.UpdateMessage,
                embed=self.embeds[self.page - 1],
                components=(await self.create_button()),
            )
        else:
            await payload.respond(
                type=InteractionType.UpdateMessage,
                content=self.contents[self.page - 1],
                components=(await self.create_button()),
            )

    async def go_last(self, payload: Context) -> None:
        if self.embeds is not None:
            if self.page != len(self.embeds) - 1:
                self.page = len(self.embeds) - 1
                await payload.respond(
                    type=InteractionType.UpdateMessage,
                    embed=self.embeds[self.page - 1],
                    components=(await self.create_button()),
                )
        elif self.contents is not None:
            if self.page != len(self.contents) - 1:
                self.page = len(self.contents) - 1
                await payload.respond(
                    type=InteractionType.UpdateMessage,
                    content=self.contents[self.page - 1],
                    components=(await self.create_button()),
                )

    def button_check(self, payload: Context) -> bool:
        if payload.user.id == self.bot.user.id:
            return False

        if payload.message.id != self.context.message.id:
            return False

        if self.only is not None:
            if payload.user.id != self.only.id:
                return False

        if not self.component.id.endswith("_click"):
            return False
        return True

    async def start(self) -> None:
        if self.contents is None:
            await self.context.send(
                embed=self.embeds[self.page - 1],
                components=(await self.create_button()),
            )
        else:
            await self.context.send(
                content=self.contents[self.page - 1],
                components=(await self.create_button()),
            )
        while True:
            try:
                _task = asyncio.ensure_future(self.bot.wait_for("button_click"))
                done, pending = await asyncio.wait(
                    [_task], return_when=asyncio.FIRST_COMPLETED, timeout=self.timeout
                )
                for i in pending:
                    i.cancel()

                if len(done) == 0:
                    raise asyncio.TimeoutError

                payload = done.pop().result()
                await self.handle_paginaion(payload=payload)

            except asyncio.TimeoutError:
                pass

    async def handle_paginaion(self, payload: Context):
        if self.use_extend:
            if payload.component.id == "_extend_left_click":
                await self.go_first()
            elif payload.component.id == "_left_click":
                await self.go_previous()
            elif payload.component.id == "_right_click":
                await self.go_next()
            elif payload.component.id == "_extend_right_click":
                await self.go_last()
        else:
            if payload.component.id == "_left_click":
                await self.go_previous()
            elif payload.component.id == "_right_click":
                await self.go_next()

    async def disable_check(self) -> None:
        if self.page == 1 and (len(self.embeds)) == 1:
            right_disable = True
            left_disable = True
        elif self.page == 1 and not (len(self.embeds)) == 1:
            right_disable = False
            left_disable = True
        elif self.page == (len(self.embeds)):
            right_disable = True
            left_disable = False
        else:
            right_disable = False
            left_disable = False

        return right_disable, left_disable

    async def create_button(self) -> list:
        right_disable, left_disable = await self.disable_check()
        if self.use_extend:
            buttons = [
                [
                    Button(
                        style=self.left_button_style,
                        label=self._left2_button,
                        id="_extend_left_click",
                        disabled=left_disable,
                    ),
                    Button(
                        style=self.left_button_style,
                        label=self._left_button,
                        id="_left_click",
                        disabled=left_disable,
                    ),
                    Button(
                        style=ButtonStyle.gray,
                        label=f"Page {str(self.page)} / {str(len(self.embeds))}",
                        id="_show_page",
                        disabled=True,
                    ),
                    Button(
                        style=self.right_button_style,
                        label=self._right_label,
                        id="_right_click",
                        disabled=right_disable,
                    ),
                    Button(
                        style=self.right_button_style,
                        label=self._right2_label,
                        id="_extend_right_click",
                        disabled=right_disable,
                    ),
                ]
            ]
        else:
            buttons = [
                [
                    Button(
                        style=self.left_button_style,
                        label=self._left_button,
                        id="_left_click",
                        disabled=left_disable,
                    ),
                    Button(
                        style=ButtonStyle.gray,
                        label=f"Page {str(self.page)} / {str(len(self.embeds))}",
                        id="_show_page",
                        disabled=True,
                    ),
                    Button(
                        style=self.right_button_style,
                        label=self._right_label,
                        id="_right_click",
                        disabled=right_disable,
                    ),
                ]
            ]
        return buttons

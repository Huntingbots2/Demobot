import time
from telegram import MessageEntity, ParseMode
from telegram.error import BadRequest
from telegram.ext import Filters, MessageHandler
from AsunaRobot import dispatcher
from AsunaRobot.modules.disable import DisableAbleCommandHandler
from AsunaRobot.modules.sql import afk_sql as sql
from AsunaRobot.modules.users import get_user_id
from AsunaRobot.modules.helper_funcs.readable_time import get_readable_time

AFK_GROUP = 7
AFK_REPLY_GROUP = 8

def afk(update, context):
    user = update.effective_user
    message = update.effective_message
    args = message.text.split(None, 1)
    reason = args[1] if len(args) > 1 else "No reason provided."
    afk_time = int(time.time())

    # Handle media reply
    media_msg_id = None
    if message.reply_to_message and (
        message.reply_to_message.photo or message.reply_to_message.sticker or
        message.reply_to_message.video or message.reply_to_message.document or
        message.reply_to_message.animation or message.reply_to_message.voice
    ):
        media_msg_id = message.reply_to_message.message_id

    sql.set_afk(user.id, reason, afk_time)
    context.chat_data[f"afk_media_{user.id}"] = media_msg_id

    text = f"{user.first_name} is now AFK!\nReason: {reason}"
    message.reply_text(text)

def no_longer_afk(update, context):
    user = update.effective_user
    if not sql.is_afk(user.id):
        return

    afk_time = sql.get_afk_time(user.id)
    duration = get_readable_time(time.time() - afk_time) if afk_time else "a while"
    if sql.remove_afk(user.id):
        update.message.reply_text(
            f"{user.first_name} is no longer AFK!\nAFK Duration: {duration}"
        )
        context.chat_data.pop(f"afk_media_{user.id}", None)

def reply_afk(update, context):
    message = update.effective_message
    userc_id = update.effective_user.id
    replied = message.reply_to_message
    mentioned_users = []

    if message.entities:
        for ent in message.entities:
            if ent.type in [MessageEntity.MENTION, MessageEntity.TEXT_MENTION]:
                if ent.type == MessageEntity.TEXT_MENTION:
                    mentioned_users.append((ent.user.id, ent.user.first_name))
                elif ent.type == MessageEntity.MENTION:
                    username = message.text[ent.offset: ent.offset + ent.length]
                    user_id = get_user_id(username)
                    if user_id:
                        try:
                            user_obj = context.bot.get_chat(user_id)
                            mentioned_users.append((user_id, user_obj.first_name))
                        except BadRequest:
                            pass

    if replied:
        user_id = replied.from_user.id
        fname = replied.from_user.first_name
        mentioned_users.append((user_id, fname))

    for user_id, fname in mentioned_users:
        if user_id == userc_id:
            continue
        if sql.is_afk(user_id):
            reason = sql.get_afk_reason(user_id)
            afk_time = sql.get_afk_time(user_id)
            since = get_readable_time(time.time() - afk_time) if afk_time else "a while"
            caption = f"{fname} is AFK!\nReason: {reason}\nSince: {since}"

            media_id = context.chat_data.get(f"afk_media_{user_id}")
            if media_id:
                try:
                    context.bot.forward_message(
                        chat_id=message.chat.id,
                        from_chat_id=message.chat.id,
                        message_id=media_id,
                    )
                except BadRequest:
                    pass

            update.message.reply_text(caption, parse_mode=ParseMode.HTML)

def __user_info__(user_id):
    if sql.is_afk(user_id):
        since = get_readable_time(time.time() - sql.get_afk_time(user_id))
        return f"<i>This user is currently AFK.</i>\n<i>Since: {since}</i>"
    return "<i>This user is not AFK.</i>"

def __gdpr__(user_id):
    sql.clear_afk(user_id)



__mod_name__ = "AFK"



AFK_HANDLER = DisableAbleCommandHandler("afk", afk, run_async=True)
AFK_REGEX_HANDLER = MessageHandler(Filters.regex("(?i)^(brb|afk)$"), afk, run_async=True)
NO_AFK_HANDLER = MessageHandler(Filters.all & Filters.chat_type.groups, no_longer_afk, run_async=True)
AFK_REPLY_HANDLER = MessageHandler(Filters.all & Filters.chat_type.groups, reply_afk, run_async=True)

dispatcher.add_handler(AFK_HANDLER, AFK_GROUP)
dispatcher.add_handler(AFK_REGEX_HANDLER, AFK_GROUP)
dispatcher.add_handler(NO_AFK_HANDLER, AFK_GROUP)
dispatcher.add_handler(AFK_REPLY_HANDLER, AFK_REPLY_GROUP)

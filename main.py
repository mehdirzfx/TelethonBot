from telethon import TelegramClient, events, sync

# تنظیم مشخصات API و نام جلسه
api_id = 123456
api_hash = 'abcdefghijklmnopqrstuvwxyz123456'
session_name = 'my_session'

# ساخت نمونه Telegram client
client = TelegramClient(session_name, api_id, api_hash)

# تعریف یک دستگیره پیام
@client.on(events.NewMessage(pattern='/start'))
async def send_message(event):
    # ارسال پیام به یک کاربر یا گروه
    await event.respond('Hello, world!')

# تعریف دستگیره‌های ویرایش، حذف، و فوروارد پیام
@client.on(events.NewMessage(pattern='/edit'))
async def edit_message(event):
    # ویرایش متن پیام
    new_text = 'This message has been edited!'
    await event.edit(new_text)

@client.on(events.NewMessage(pattern='/delete'))
async def delete_message(event):
    # حذف پیام
    await event.delete()

@client.on(events.NewMessage(pattern='/forward'))
async def forward_message(event):
    # فوروارد پیام
    target_chat = 'username_or_group_id'
    await event.forward_to(target_chat)

@client.on(events.NewMessage(pattern='/info'))
async def user_info(event):
    # دریافت مشخصات کاربری
    sender = await event.get_sender()
    await event.respond(f"User information:\n\nUsername: {sender.username}\nFirst name: {sender.first_name}\nLast name: {sender.last_name}\nID: {sender.id}")

# شروع عملیات
with client:
    # منتظر رخدادها بمانید
    client.run_until_disconnected()

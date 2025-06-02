import requests
import json
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

TOKEN = '8049956611:AAEh5eRS5ofPmUjlZ-dyZpuSUzd_B61BH1M'

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("قسم البحث 🔎", callback_data='search'),
         InlineKeyboardButton("قسم الافلام 🎬", callback_data='movies')],
        [InlineKeyboardButton("حساب المطور ⚙", url='https://t.me/Almortagel_12')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://graph.org/file/8267fe8a828dbfa144528.jpg',
                           caption="👋🏼 مرحبا 🎟️ في حالة وجود مشاكل اخبر المطور 📚 تجربة مميزة بدون اعلانات مزعجة 📮 نتمنى لك تجربة رائعه في البوت 💡",
                           reply_markup=reply_markup)

def movies(update, context):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("افلام وثائقssية", callback_data='v     
         InlineKeyboardButton("افلام موسيقية", callback_data='#0'),
         InlineKeyboardButton("افلام موسيقية", callback_data='v#1')],
        [InlineKeyboardButton("افلام مغامرة", callback_data='v     
         InlineKeyboardButton("افلام كوميديا", callback_data='#2'),
         InlineKeyboardButton("افلام كوميديا", callback_data='v#3')],
        [InlineKeyboardButton("القائمة الرئيسية", callback_data="back1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_caption(caption="*📂 حسنًا يرجى الاختيار من القائمة التالية:*",
                               reply_markup=reply_markup, parse_mode='Markdown')

def get_movies(update, context):
    query = update.callback_query
    data = query.data.split('   
    url = f"https://sherifbots.serv00.net/Api/fushaar.php?s=https://www.fushaar.live/gerne/{['#')
    url = f"https://sherifbots.serv00.net/Api/fushaar.php?s=https://www.fushaar.live/gerne/{['documentary', 'music', 'adventure', 'comedy'][int(data[1])]}/"
    response = requests.get(url).json()
    keyboard = []
    for movie in response:
        keyboard.append([InlineKeyboardButton(movie['name'], callback_data=f"l                                      
    keyboard.append([InlineKeyboardButton("التالي", callback_data=f"next                
    keyboard.append([InlineKeyboardButton("الغاء", callback_data="back1")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_caption(caption="*🗃 حدد الفيلم الذي تريد مشاهدته الان:*",
                               reply_markup=reply_markup, parse_mode='#{data[1]}#{response.index(movie)}")])
    keyboard.append([InlineKeyboardButton("التالي", callback_data=f"next#{data[1]}#1")])
    keyboard.append([InlineKeyboardButton("الغاء", callback_data="back1")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_caption(caption="*🗃 حدد الفيلم الذي تريد مشاهدته الان:*",
                               reply_markup=reply_markup, parse_mode='Markdown')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(movies, pattern='^movies$'))
    dp.add_handler(CallbackQueryHandler(get_movies, pattern='^v#'))
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()

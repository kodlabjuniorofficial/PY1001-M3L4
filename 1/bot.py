## "pip install python-dotenv" ile env kütüphanesini yükleyin. 

import os
from dotenv import load_dotenv # Yeni kütüphane
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from assistant import Assistant

# 1. ADIM: .env dosyasındaki verileri yükle
load_dotenv()

# 2. ADIM: Token'ı sistem değişkenlerinden çek (Kodun içinde şifre kalmadı!)
TOKEN = os.getenv("BOT_TOKEN")

bot_brain = Assistant("ZeyBot")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(bot_brain.greet())

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(bot_brain.show_status())

async def charge_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(bot_brain.charge())

async def add_note_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = " ".join(context.args)
    if user_text:
        await update.message.reply_text(bot_brain.add_note(user_text))
    else:
        await update.message.reply_text("❌ Not yazmadın!")

# NEDİR KOMUTU (Görsel ve Bilgi)
async def say_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)
    
    if query:
        # Asistandan bilgi paketini iste
        result = bot_brain.search_info(query)
        
        if result["status"] == "ok":
            # EĞER GÖRSEL VARSA
            if result["image"]:
                await update.message.reply_photo(
                    photo=result["image"],
                    caption=f"🔍 **{result['topic']}**\n\n{result['text']}",
                    parse_mode='Markdown'
                )
            # EĞER GÖRSEL YOKSA
            else:
                await update.message.reply_text(
                    f"🔍 **{result['topic']}**\n\n{result['text']}",
                    parse_mode='Markdown'
                )
        else:
            await update.message.reply_text(result["message"])
    else:
        await update.message.reply_text("❓ Lütfen öğrenmek istediğiniz şeyi yazın. Örn: /nedir Mars")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Komut Kayıtları
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('durum', status))
    app.add_handler(CommandHandler('sarj', charge_bot))
    app.add_handler(CommandHandler('not_al', add_note_cmd))
    app.add_handler(CommandHandler('nedir', say_info)) 
    
    print("M3L3: Bilge Asistan Görsel Desteğiyle Yayında! 🧠🖼️")
    app.run_polling()
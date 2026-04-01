import telebot

TOKEN = 8723574388:AAExkmznuwV3upqP5nbUtU2FxAGfA2jay-s
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 
    "🎉 Bienvenue !\n\n"
    "💰 Gagne de l'argent avec moi !\n\n"
    "👉 Inscris-toi ici : https://1xbet.cg?bf=6a45e998e64c4_14032371103\n\n"
    "📌 Commandes :\n"
    "/profil - Voir ton profil\n"
    "/retrait - Comment retirer")

@bot.message_handler(commands=['profil'])
def profil(message):
    bot.send_message(message.chat.id, "👤 Ton profil sera bientôt disponible")

@bot.message_handler(commands=['retrait'])
def retrait(message):
    bot.send_message(message.chat.id, 
    "💳 Pour retirer :\n"
    "1. Inscris-toi avec le lien\n"
    "2. Dépose et joue\n"
    "3. Contacte l’admin")

bot.infinity_polling()
import telebot
from logic import Text2ImageAPI
from config import API_KEY, SEKET_KEY, TOKEN

API_TOKEN = TOKEN

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = message.text

    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API_KEY, SEKET_KEY)
    model_id = api.get_model()
    uuid = api.generate(prompt, model_id)
    images = api.check_generation(uuid)[0]

    file_path = "GeneratedImg.jpg"
    api.save_image(images, file_path)

    with open(file_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo)


bot.infinity_polling()

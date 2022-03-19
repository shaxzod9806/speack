import logging
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
from oxfordLookUp import oxfordLookUp

API_TOKEN = '5260449495:AAEb13FTErfPWxV64xw67JPCGzq7SEKN0_w'
translator = Translator()
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("salom wiki botga xush kelibsiz")


@dispatcher.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    print(lang)
    if len(message.text.split()) > 1:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text
            print(word_id)
        lookup = oxfordLookUp(word_id)
        if lookup:
            print(lookup)
            await message.reply(lookup[0])
            if lookup.count() > 1:
                await message.reply_voice(lookup[1])

        else:
            await message.reply("bunday so'z topilmadi")


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)

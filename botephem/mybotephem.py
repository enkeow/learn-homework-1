import logging
import ephem 
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='bot.log, level=logging.INFO - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}
def main():
     mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)
     logger.info("Вызван/start")
     mybot.start_polling()
     mybot.idle

def greet_user(update, context):
    text_hello = 'Вызван /start'
    print(text_hello)
    update.message.reply_text("Привет, ты вызвал астрономического бота! Введите название /planet <planet> на английском языке и узнаете кое-что интересное!")
    
"""def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)"""

def info_planet(update, context):
    planet = {
        'Mars': ephem.Mars(),
        'Pluto': ephem.Pluto(),
        'Venus': ephem.Venus(),
        'Neptune': ephem.Neptune(),
        'Uranus': ephem.Uranus(),
        'Saturn': ephem.Saturn(),
        'Mercury': ephem.Mercury()
    }
    user_text = update.message.text.split()
    
    planet_name = input().capitalize()
    if planet_name not in planet:
        return "Такой планеты нет"
    
    planet = planet[planet_name]
    planet.compute()
    constellation = ephem.constellation(planet)[1]
    update.message.reply_text(f'Планета {planet_name} сегодня в созвездии {constellation}')
    
if __name__ == "__main__":
    main()


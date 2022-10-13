from json import loads
import requests
import telebot



def readJsonFile() -> str:
    return loads(open("kurBotu/token.json", mode="r").read())["token"]

def getData(data: str = ...) -> str:
    url = "https://api.genelpara.com/embed/para-birimleri.json"
    r = requests.get(url=url).json()
    jsonAlis = r[data]["alis"]
    jsonDegisim = r[data]["degisim"]
    jsonSatis = r[data]["satis"]
    return f"〣〣〣〣 ─────── {data} ─────── 〣〣〣〣\n\nAlış : {jsonAlis}\n\nSatış : {jsonSatis}\n\nDeğişim : {jsonDegisim}\n"

bot = telebot.TeleBot(token=readJsonFile())


@bot.message_handler(commands=["usd", "USD"])
def usd(message):
    bot.send_message(message.from_user.id, getData(data="USD"))

@bot.message_handler(commands=["eur", "EUR"])
def eur(message):
    bot.send_message(message.from_user.id, getData(data="EUR"))

@bot.message_handler(commands=["gbp", "GBP"])
def gbp(message):
    bot.send_message(message.from_user.id, getData(data="GBP"))

@bot.message_handler(commands=["btc", "BTC"])
def btc(message):
    bot.send_message(message.from_user.id, getData(data="BTC"))

@bot.message_handler(commands=["eth", "ETH"])
def eth(message):
    bot.send_message(message.from_user.id, getData(data="ETH"))

@bot.message_handler(commands=["ga", "GA"])
def ga(message):
    bot.send_message(message.from_user.id, getData(data="GA"))

@bot.message_handler(commands=["c", "C"])
def c(message):
    bot.send_message(message.from_user.id, getData(data="C"))

@bot.message_handler(commands=["gag", "GAG"])
def gag(message):
    bot.send_message(message.from_user.id, getData(data="GAG"))

@bot.message_handler(commands=["xu100", "XU1100"])
def xu100(message):
    bot.send_message(message.from_user.id, getData(data="XU100"))


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.from_user.id, """
    
*Bot hakkında* : Genelpara apisi üzerinden Usd, Eur, Gbp, Btc, Eth, Ga, C, Gag, Xu100 alış , satış ve değişim bilgilerini almanızı sağlar.\n 
Kullanımı : /USD, /EUR, /GBP ...\n
*Geliştirici* : *Coderx37*

""", parse_mode="MARKDOWN")



bot.polling()
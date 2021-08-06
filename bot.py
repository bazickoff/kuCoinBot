from os import name, system
if (name == 'nt'):
    from ctypes import windll
    windll.kernel32.SetConsoleTitleW("Kucoin Bot V 0.0.2 | facade1337")
else:
    system('clear')
from sys import argv
from sys import exit
from kucoin.client import Trade
from kucoin.client import Market
marketApi = Market(url='https://api.kucoin.com')
from datetime import datetime
from time import strftime
from time import sleep
from json import load
import discord
from math import floor
from re import search
from expand import expand
from time import mktime
from datetime import timezone
helpMePls = marketApi.get_symbol_list()
nowlol = datetime.now()
lolelrl = nowlol.strftime('%H:%M:%S.%f')
print(lolelrl[:-3] + ' >>> ' + 'Kucoin bot developed by facade1337 on github <3. Join one of the best kucoin pump groups here: discord.gg/m7VzPeeA7A')
f = open('config.json',)
data = load(f)
f.close()
api_key = str(data["api_key"])
api_secret = str(data["api_secret"])
api_password = str(data["api_password"])
basecurrency = str(data["basecurrency"])
amount = str(data["amount"])
channelOne = data["channelOne"]
channelTwo = data["channelTwo"]
channelThree = data["channelThree"]
waitTimeRealSeconds = float(data["waitTime"])
decimal = 0
pairing = ''
startedOnce = False
client = Trade(key=api_key, secret=api_secret, passphrase=api_password, is_sandbox=False, url='')
base = basecurrency.upper()
nowlole = datetime.now()
lolelrel = nowlole.strftime('%H:%M:%S.%f')
print(lolelrel[:-3] + ' >>> ' + "Trading with " + amount + " " + base + '.')
clientw = discord.Client()
@clientw.event
async def on_ready():
    ending_time = datetime.now()
    ping = ending_time - starting_time
    ping = int(ping.microseconds)
    watchingChannelOne = clientw.get_channel(channelOne)
    watchingChannelTwo= clientw.get_channel(channelTwo)
    watchingChannelThree = clientw.get_channel(channelThree)
    nowlol = datetime.now()
    lolelrl = nowlol.strftime('%H:%M:%S.%f')
    print(lolelrl[:-3] + ' >>> '  + 'Ready and watching channels [' + str(watchingChannelOne) + '], ' + '[' + str(watchingChannelTwo) + '], ['+ str(watchingChannelThree) + '] for pump signal.')
@clientw.event
async def on_message(message):
    global startedOnce
    global helpMePls
    global decimal
    if (message.channel.id != channelOne & message.channel.id != channelTwo & message.channel.id != channelThree) == False:
        print(message.channel.id != channelOne & message.channel.id != channelTwo & message.channel.id != channelThree)
        print(message.channel.id != channelThree & message.channel.id != channelOne)
        print(message.channel.id != channelTwo)
        return
    content = message.content
    if base in content and "kucoin.com" in content and startedOnce == False:
        startedOnce = True
        discord_starting_time = message.created_at
        tz_info = discord_starting_time.tzinfo
        content = search("(?P<url>https?://[^\s]+)",  content).group("url")
        content = content.replace("-", "")
        content = content.replace(base, "")
        content = content.replace("coin", "")
        if "ku.com/" in content:
            content = content.replace("https://ku.com/", "")
            content = content.replace("https://ku.com/", "")
            content = content.replace("http://trade.ku.com/", "")
            content = content.replace("https://trade.ku.com/", "")
        content = content.replace(")", "")
        content = content.replace("(", "")
        content = content.replace("[", "")
        content = content.replace("]", "")
        content = content.replace("/", "")
        content = content.replace(".", "")
        content = content.replace("!", "")
        content = content.replace("<", "")
        content = content.replace(">", "")
        pairing = content
        pairingf = pairing.upper()
        pairing = pairingf + '-' + base
        sleep(waitTimeRealSeconds)
        starting_time = datetime.now(tz_info)
        order_id = client.create_market_order(pairing, 'buy', funds=amount)
        ending_time = datetime.now(tz_info)
        startedOnce = True
        ping = ending_time - starting_time
        ping = int(ping.microseconds)
        lol = str(order_id["orderId"])
        sleep(0.200)
        xd = client.get_order_details(lol)
        amount_of_coin = float(xd["dealSize"])
        lolelrl = ending_time.strftime('%H:%M:%S.%f')
        tz_info = discord_starting_time.tzinfo
        totalTime = ((ending_time - discord_starting_time).microseconds)
        totalTimeMs = str(round(totalTime / 1000))
        print(lolelrl[:-3] + ' >>> ' + 'Executed trade with ' + amount + ' ' + base +' being sold in the pairing ' + pairing + ' in ' + str(round(ping / 1000)) + ' ms. Bought ' + str(expand(amount_of_coin)) + ' ' + pairingf + '.' + ' Total delay was ' + totalTimeMs + ' ms.')
        for i in helpMePls:
            if (i["symbol"] == pairing):
                baseIncrement = i["baseIncrement"]
                loler = marketApi.get_currency_detail(content.upper())
                precision = loler["precision"]
                break
            else:
                donothing = 0
        lolerxd = expand(float(amount_of_coin) % float(baseIncrement))
        newAmount = expand(float(amount_of_coin) - float(lolerxd))
        amount_of_coin = newAmount
        decimalPlaces = len(str(amount_of_coin).split(".")[1])
        decimalPlacesInBase = len(str(baseIncrement).split(".")[1])
        baseIncrement = float(baseIncrement)
        if (decimalPlaces > precision):
            newAmount = str(newAmount)[:-(decimalPlaces - precision)]
        if (float(expand(float(newAmount) % float(baseIncrement))) < baseIncrement):
            pass
        else:   
            multiplier = pow(10, decimalPlaces)
            maxNewAmount = newAmount * (multiplier)
            lol = (floor(maxNewAmount)) / multiplier
            lol1 = (floor(lol * multiplier)) / multiplier
            decimalPlaces = len(str(lol1).split(".")[1])
            rounded = decimalPlaces - decimalPlacesInBase
            newAmount = str(lol1)[:-(rounded)]
        waitTime = datetime.now(tz_info)
        waitTime = ending_time - waitTime
        waitTimeMicro = waitTime.microseconds
        waitTimeMilli = waitTimeMicro / 1000
        waitTimeSeconds = waitTimeMilli / 1000
        sleep(waitTimeRealSeconds - waitTimeSeconds)
        starting_time = datetime.now()
        order_id = client.create_market_order(pairing, 'sell', size=newAmount)
        ending_time = datetime.now()
        ping = ending_time - starting_time
        ping = int(ping.microseconds)
        lol = str(order_id["orderId"])
        sleep(0.200)
        xd = client.get_order_details(lol)
        amount_of_coin = float(xd["dealSize"])
        lolelrl = ending_time.strftime('%H:%M:%S.%f')
        print(lolelrl[:-3] + ' >>> ' + 'Executed trade with ' + amount + ' ' + base +' being bought in the pairing ' + pairing + ' in ' + str(round(ping / 1000)) + ' ms. Sold ' + str(expand(amount_of_coin)) + ' ' + pairingf + '.')
        lol = input(lolelrl[:-3] + ' >>> ' + "Upon acknowledgment and screenshot, Please press enter to close the bot.")
        exit()
starting_time = datetime.now()        
clientw.run(token)






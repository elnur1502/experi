﻿import vk_api
import random
import requests
import Gamebot.Steps as steps
import Gamebot.Market as Market
from bs4 import BeautifulSoup
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

token = "e615070ecbd0a9642205948dbe49728785555494f701852aabe742313bc7eee4dbdd7447ffeca14003479" #token

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
botlongpoll = VkLongPoll(vk)

search_link = "https://www.microsoft.com/ru-ru/search?q="

gameNameTag = "c-subheading-6"
gamePriceTag = "c-price"
gameLink = "m-channel-placement-item"
gamePrice = "pi-price-text"

maximumGames = 5 # максимальное кол-во игр выводимых в сообщении
dob = 2 # множитель (заменимый)

dollar = 79
peco = 1.23

market = Market.Market()
shop = []

def getShortLink(link):
    return vk.method('utils.getShortLink', {'url': link, 'private': 0})['short_url']
def write_msg(user_id, message):
    vk.method('messages.send',
              {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 9999999), 'peer_id': user_id})
def findElement(reqw, el, thingOfFind):
    header = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'dnt': '1',
        'pragma': 'no-cache',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}  # Обеспечивает доступ к сайту

    # Test
    # reqw = "Metro Exodus - Sam's story"
    source_url = "https://www.microsoft.com/ru-ru/search/shop/games?q=" + str(reqw).replace(" ", "_").replace("'", "%27")

    respw = requests.get(source_url, timeout=10, headers=header)
    soup = BeautifulSoup(respw.text, 'html.parser')

    #print(respw.text + ("/n" * 3))  # output the html of the page
    #print(soup.find_all("href", class_=gameLink)[0:maximumGames].text)

    return soup.find_all(el, class_=thingOfFind)


def findElementAF(reqw, el, thingOfFind):
    header = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'dnt': '1',
        'pragma': 'no-cache',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}  # Обеспечивает доступ к сайту

    # Test
    # soup.find_all("href", class_=gameLink)[0:maximumGames].text = "/ru-ru/p/battlefield-1/bwttw53m5b98"
    source_url = "https://www.microsoft.com" + str(soup.find_all("href", class_=gameLink)[0:maximumGames].text).replace(" ", "_").replace("'", "%27")

    respw = requests.get(source_url, timeout=10, headers=header)
    soup = BeautifulSoup(respw.text, 'html.parser')

    #print(respw.text + ("/n" * 3))  # output the html of the page
    #print(soup.find_all("h1", class_=thingOfFind)[0:maximumGames].text)

    return soup.find_all(el, class_=thingOfFind)


def findElementAU(reqw, el, thingOfFind):
    header = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'dnt': '1',
        'pragma': 'no-cache',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}  # Обеспечивает доступ к сайту

    # Test
    # reqw = "Metro Exodus - Sam's story"
    source_url = "https://www.microsoft.com/es-ar/search/shop/games?q=" + str(reqw).replace(" ", "_").replace("'", "%27")

    respw = requests.get(source_url, timeout=10, headers=header)
    soup = BeautifulSoup(respw.text, 'html.parser')

    #print(respw.text + ("/n" * 3))  # output the html of the page
    #print(soup.find_all("h3", class_=thingOfFind)[0:maximumGames].text)

    return soup.find_all(el, class_=thingOfFind)

def gamesInfoPage(userID, req):
    text = "Выберите одну игру из предложенных вариантов (Напишите ее номер): \n"
    for i in range(len(findElement(req, "h3", gameNameTag))):
        if i == maximumGames:
            break
        text += "{})".format(i+1) + " " + findElement(req, "h3", gameNameTag)[i].text + "\n"

        zz = findElement(req, "div", gameLink)[i]
        root_childs = [e.text for e in zz.children if e.name is not None]
        aa = findElementAF(req, "div", gamePrice)[i]
        root_childs = [e.text for e in aa.children if e.name is not None]
        bb = findElementAU(req, "div", gamePriceTag)[i]
        root_childsAU = [e.text for e in bb.children if e.name is not None]
        z = 0
        a = 0
        b = 0
        if len(root_childs) < 4:
            z = 0
        else:
            z = 4
        if len(root_childsRU) < 4:
            a = 0
        else:
            a = 4
        if len(root_childsAU) < 4:
            b = 0
        else:
            b = 4
        if (str(root_childsAU[b]).find("Ahora") != -1):
            root_childsAU[b] = str(root_childsAU[b]).split("Ahora")[1].split("\n")[0]
        if (str(root_childsRU[b]).find("Сейчас") != -1):
            root_childsRU[a] = str(root_childsRU[a]).split("Текущая цена")[1].split("\n")[0]
        print("AA: {} BB: {} LEN: {}/{}".format(root_childsRU, root_childsAU, len(root_childsRU), len(root_childsAU)))
        #print(root_childs[0])
        #print(str(findElement(req, "div", gamePriceTag)[i].text).replace("\n", "").replace("", "").replace("  ","").replace("\r", "").replace("USD$", "").replace("+", "").replace("Бесплатно", "0").replace(",","."))
        try:
            w = str(root_childsRU[a].replace("\n", "").replace(" ", "").replace("  ","").replace("\r", "").replace("USD$", "").replace("+", "").replace("Бесплатно", "0"))
            if str(root_childsRU[a].replace("\n", "").replace(" ", "").replace("  ","").replace("\r", "").replace("USD$", "").replace("+", "").replace("Бесплатно", "0")).find(",") != -1:
                w = str(root_childsRU[a].replace("\n", "").replace(" ", "").replace("  ","").replace("\r", "").replace("USD$", "").replace("+", "").replace("Бесплатно", "0")).split(",")[0]
            priceRU = (float(float(w) * dollar))
        except:
            priceRU = 0
        try:
            s = str(root_childsAU[b].replace("\n", "").replace(" ", "").replace("  ", "").replace("\r", "").replace("$",
                                                                                                                    "").replace(
                ".", "").replace(",00", "").replace("+", "").replace("Gratis", "0"))
            if str(root_childsAU[b].replace("\n", "").replace(" ", "").replace("  ", "").replace("\r", "").replace("$",
                                                                                                                   "").replace(
                    ".", "").replace(",00", "").replace("+", "").replace("Gratis", "0")).find(",") != -1:
                s = str(
                    root_childsAU[b].replace("\n", "").replace(" ", "").replace("  ", "").replace("\r", "").replace("$",
                                                                                                                    "").replace(
                        ".", "").replace(",00", "").replace("+", "").replace("Gratis", "0")).split(",")[0]
            priceAU = (float(float(s) * 1))
        except:
           priceAU = 0

        shop.append(findElement(req, "h3", gameNameTag)[i].text + "|" + str(priceRU) + "|" + str(priceAU)  + "|" + str(getShortLink("https://www.microsoft.com/ru-ru/search/shop/games?q=" +str(findElement(req, "div", "m-channel-placement-item")[i].findChildren()[0].get('href')))).replace("https://", "") + "|" + str(getShortLink("https://www.microsoft.com/es-ar/search/shop/games?q=" + str(findElementAU(req, "div", "m-channel-placement-item")[i].findChildren()[0].get('href')))).replace("https://", "")) # ['name|priceRU|priceAU|linkRU|linkAU', ...]
    print(shop) #  + "|" + findElement(req, "div", "m-channel-placement-item")[i].findChildren("div")[0].get('href')
    #market.addUser(userID=userID, shop=shop)
    text += "\n 0) Выбрать другую игру."
    print(req)
    return text


def main():
    stepsController = steps.Steps()

    for event in botlongpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                print(request)
                #print(stepsController.isExistsUser(userID=event.user_id))
                #print(stepsController.getUser(userID=event.user_id))
                #print(stepsController.getStep(userID=event.user_id))

                if stepsController.isExistsUser(userID=event.user_id) == False:
                    stepsController.addUser(userID=event.user_id)

                #if stepsController.getStep(userID=event.user_id) > 1:
                #   stepsController.setStep(userID=event.user_id, step=0)
                if stepsController.getStep(userID=event.user_id) == 1:
                    if stepsController.getStep(userID=event.user_id) == 1:
                        if str(request).isdigit():
                            if int(request) == 1 or int(request) == 2 or int(request) == 3 or int(request) == 4 or int(request) == 5 or int(request) == 6 or int(request) == 7 or int(request) == 8 or int(request) == 9 or int(request) == 10:
                                if int(request) > maximumGames:
                                    write_msg(event.user_id, "Выберите существующие число !")
                                if float(str(shop[int(request)-1]).split("|")[1]) > float(str(shop[int(request)-1]).split("|")[2]):
                                    print(str(float(str(shop[int(request)-1]).split("|")[2])) + "|" + str(float(str(shop[int(request)-1]).split("|")[1])))
                                    write_msg(event.user_id, "Игра: {} \n Цена: {} руб. \n Напишите сюда чтобы купить - {}".format(str(shop[int(request)-1]).split("|")[0], str(round(float(str(shop[int(request)-1]).split("|")[1]))), str(getShortLink("https://vk.com/elnursh15"))))
                                    stepsController.setStep(userID=event.user_id, step=0)
                                    shop .clear()
                                else:
                                    write_msg(event.user_id, "Игра: {} \n Цена: {} руб. \n Напишите сюда чтобы купить - {}".format(str(shop[int(request)-1]).split("|")[0], str(round(float(str(shop[int(request)-1]).split("|")[1]))), str(getShortLink("https://vk.com/elnursh15"))))
                                    stepsController.setStep(userID=event.user_id, step=0)
                                    shop .clear()
                            if request == "0":
                                write_msg(event.user_id, "Вы вернулись назад !")
                                shop.clear()
                                #market.delUser(userID=event.user_id)
                                stepsController.setStep(userID=event.user_id, step=0)
                        else:
                            write_msg(event.user_id, "Выберите игру")
                else:

                    if stepsController.getStep(userID=event.user_id) == 0:
                        print(request)
                        write_msg(event.user_id, "Выполняется поиск...")
                        write_msg(event.user_id, gamesInfoPage(event.user_id, request))
                        stepsController.setStep(userID=event.user_id, step=1)
                        #print(market.getUser(userID=event.user_id))

                        #print(event.user_id, findElement(request, gameNameTag)[0].text)


    print("End.")


if __name__ == '__main__':
    main()

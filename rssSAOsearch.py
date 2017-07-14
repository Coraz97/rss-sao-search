import time
import feedparser
import smtplib


def alert(title, link, site):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("meddosayentisto99@gmail.com", "ffggarc28")
    msg = "|| Trovato un elemento su " + site + ". \n|| Nome del file: " + title + "\n|| Trovato all'indirizzo: " + link
    server.sendmail("meddosayentisto99@gmail.com", "theframpa@gmail.com", msg)


def parse(feed, nyaa, animetosho, minglong, kw):
    rss = feedparser.parse(feed)
    if rss['feed']['title'] == "Nyaa Torrent File RSS":
        search_nyaa(rss, nyaa, kw)
    elif rss['feed']['title'] == "Tokyo Toshokan":
        search_animetosho(rss, animetosho, kw)
    elif rss['feed']['title'] == "minglong BitTorrent Tracker":
        search_minglong(rss, minglong, kw)


def search_nyaa(rss, last_title, kws):
    if rss['entries'][0]['title'] == last_title:
        return
    else:
        last_title = rss['entries'][0]['title']
    for item in rss['entries']:
        for keyword in kws:
            if keyword in item['title']:
                if item['nyaa:categoryId'] == "1_2":
                    alert(item['title'], item['id'],"nyaa")
    return


def search_animetosho(rss, last_title, kws):
    if rss['entries'][0]['title'] == last_title:
        return
    else:
        last_title = rss['entries'][0]['title']
    for item in rss['entries']:
        for keyword in kws:
            if keyword in item['title']:
                alert(item['title'], item['link'], "animetosho")
    return


def search_minglong(rss, last_title, kws):
    if rss['entries'][0]['title'] == last_title:
        return
    else:
        last_title = rss['entries'][0]['title']
    for item in rss['entries']:
        for keyword in kws:
            if keyword in item['title']:
                alert(item['title'], "Nessun link trovato", "minglong")
    return


def start(f, n, a, m, k):
    k = 0
    while k < 12:
        for coso in f:
            parse(coso, n, a, m, k)
        time.sleep(3500)


nyaa_last_title = "qazwsx"
animetosho_last_title = "qazwsx"
minglong_last_title = "qazwsx"
feeds = ["https://nyaa.si/?page=rss", "https://animetosho.org/feed/rss2?only_tor=1", "http://tracker.minglong.org/rss.xml"]
keywords = ["SAO", "Sword Art Online", "Ordinal Scale"]
for b in feeds:
    parse(b, nyaa_last_title, animetosho_last_title, minglong_last_title, keywords)
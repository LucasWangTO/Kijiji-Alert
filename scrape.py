import feedparser
import time
from sendEmails import sendEmail

free1List = []
free2List = []

while (True):
    free1 = feedparser.parse('https://www.kijiji.ca/rss-srp-free-stuff/gta-greater-toronto-area/c17220001l1700272')
    free2 = feedparser.parse('https://www.kijiji.ca/rss-srp-gta-greater-toronto-area/l1700272?ad=offering&price-type=free')
    change1 = 0
    change2 = 0
    for entry in free1.entries:
        if (entry.link in free1List):
            break
        else:
            change1 += 1
            str = entry.title.lower()
            if ("table" in str or "ping pong" in str or "table tennis" in str):
                if ("pool" in str or "ping" in str or "pong" in str or "tennis" in str):
                    sendEmail(entry.title, entry.link)
            if ("laptop" in str or "computer" in str or "thinkpad" in str or "keyboard" in str or "pc" in str or "desktop" in str or "drill" in str or "press" in str or "billiard" in str or "snooker" in str):
                sendEmail(entry.title, entry.link)

    for entry in free2.entries:
        if (entry.link in free2List):
            break
        else:
            change2 += 1
            str = entry.title.lower()
            if ("table" in str or "ping pong" in str or "table tennis" in str):
                if ("pool" in str or "ping" in str or "pong" in str or "tennis" in str):
                    sendEmail(entry.title, entry.link)
            if ("laptop" in str or "computer" in str or "thinkpad" in str or "keyboard" in str or "pc" in str or "desktop" in str or "drill" in str or "press" in str or "billiard" in str or "snooker" in str):
                sendEmail(entry.title, entry.link)
    
    if change1 > 0:
        free1List = []
        for entry in free1.entries:
            free1List.append(entry.link)

    if change2 > 0:
        free2List = []
        for entry in free2.entries:
            free2List.append(entry.link)

    time.sleep(300)

    print("Finished cycle")

import feedparser
import time
from sendEmails import sendEmail

freeList = []

while (True):
    free = feedparser.parse('The RSS link of the Kijiji Website')
    change = 0
    for entry in free.entries:
        if (entry.link in freeList):
            break
        else:
            change += 1
            str = entry.title.lower()
            if ("keyword" in str):
                sendEmail(entry.title, entry.link)
    
    if change > 0:
        freeList = []
        for entry in free.entries:
            freeList.append(entry.link)

    time.sleep(300)

    print("Finished cycle")

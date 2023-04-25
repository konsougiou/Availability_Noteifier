import requests
import utils
import re
import time
from collections import defaultdict
from bs4 import BeautifulSoup
from email_api import send_alerts


ebuyer_url = "https://www.ebuyer.com/search"


item_cooldowns = defaultdict(lambda: 0)


while True:
    items = utils.get_items()

    urls = []

    for item, price_cap in items.items():

        ########## ebuyer scraping ##########

        if item_cooldowns[item] <= 0:
            page = requests.get(ebuyer_url + f"?q={item}")
            soup = BeautifulSoup(page.text, "html.parser")
            list_div = soup.find("div", {"id": "list-view"})
            listings = list_div.find_all("div")

            for listing in listings:    

                price = None
                try:
                    price_list = re.findall(r'\d+', listing.find("div", {"class": "inc-vat"}).find("p", {"class": "price"}).text.strip())
                    if len(price_list) == 2:
                        price = float(price_list[0]) + (0.01 * float(price_list[1]))
                    else:
                        price = float(price_list[1]) + (0.01 * float(price_list[2])) + (1000 * float(price_list[0]))
                except:
                    pass
                
                if price != None:
                    if price <= price_cap:

                        try:
                            url = listing.find("h3", {"class": "listing-product-title"}).find("a").get("href")
                            urls.append((item, "https://www.ebuyer.com" + url, price))
                            item_cooldowns[item] = 1800
                        except:
                            pass

        else:
            item_cooldowns[item] -= 300

    
    if urls:
        send_alerts(urls)

    time.sleep(300)
    
    

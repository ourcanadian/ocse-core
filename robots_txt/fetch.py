import asyncio
import aiohttp
import time
import re

async def fetch(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                resp = await response.read()
                data = resp.decode('utf-8')
                is_shopify = re.search("shopify", data, re.IGNORECASE) != None
                print(url, is_shopify)

    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))


async def fetchAll(urls, amount):
    ret = await asyncio.gather(*[fetch(url) for url in urls])

def main():
    urls = [i.strip() for i in open("robot_list.txt").readlines()]
    amount = len(urls)

    start = time.time()
    asyncio.run(fetchAll(urls, amount))
    end = time.time()

    print("Took {} seconds to pull {} websites.".format(end - start, amount))

if __name__ == "__main__":
    main()
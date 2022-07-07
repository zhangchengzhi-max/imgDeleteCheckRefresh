import concurrent.futures
import requests
from multiprocessing.pool import Pool
import asyncio
import aiohttp
import time

import Config.Configuration

file = open(Config.Configuration.Config.checkfile)
exist = open(Config.Configuration.Config.existfile)
noexist = open(Config.Configuration.Config.notexist)

urls = file.readlines()
#
# def head(url):
#     response = requests.head(url)
#     return response.status_code



async def head2(url):
    connector = aiohttp.TCPConnector(force_close=True)
    async with aiohttp.ClientSession(connector=connector)  as session:
            async with session.head(url)as resp:
                status_code = resp.status
                result = await resp.text()
                if status_code ==200:
                    print(url,status_code)
                    exist.write(url)
                else:
                    # print(url,status_code)
                    noexist.write(url)



loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(head2(url))
    for url in urls]






if __name__ == '__main__':
    start = time.time()
    # print(urls)
    loop.run_until_complete(asyncio.wait(tasks))


    end = time.time()
    print(end-start)
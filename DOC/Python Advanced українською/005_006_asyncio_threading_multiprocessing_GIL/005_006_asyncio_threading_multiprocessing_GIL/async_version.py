import asyncio
import time
import aiohttp
import functools


def get_duration(func):
    @functools.wraps(func)
    def wraper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        duration = time.time() - start_time
        print(f"Duration = {duration}")
        return res

    return wraper


async def download_site(session, url, num):
    async with session.get(url) as response:
        print(
            f"Read -{num}- {response.content_length} from {url}, status code is {response.status}"
        )


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(download_site(session, url, num)) for num, url in enumerate(sites)
        ]
        await asyncio.gather(*tasks)


sites = [
            "http://www.testingmcafeesites.com/index.html",
            "https://www.jython.org"
        ] * 200


@get_duration
def main():
    asyncio.run(download_all_sites(sites))


if __name__ == "__main__":
    main()

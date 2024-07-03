import requests
import multiprocessing
import functools
import time

session = None


def get_duration(func):
    @functools.wraps(func)
    def wraper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        duration = time.time() - start_time
        print(f"Duration = {duration}")
        return res

    return wraper


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = [
                "https://github.com/",
                "https://www.jython.org"
            ] * 200
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")

import aiohttp
import asyncio

class AsyncWebScraper:
    def __init__(self, urls):
        self.urls = urls

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.close()

    async def fetch_url(self, url):
        async with self.session.get(url) as response:
            return await response.text()

    async def scrape(self):
        tasks = [self.fetch_url(url) for url in self.urls]
        return await asyncio.gather(*tasks)

async def main():
    try:
        file_path = "urls.txt"  
        with open(file_path, "r") as file:
            urls = [line.strip() for line in file]

        async with AsyncWebScraper(urls) as scraper:
            results = await scraper.scrape()

        for url, content in zip(urls, results):
            print(f"Контент из {url}:\n{content}\n")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass

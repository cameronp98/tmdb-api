import aiohttp
from urllib.parse import urlencode, urlunsplit, urljoin


class Api:
    def __init__(self, loc: str, method: str = "https", prepath: str = "", **kwargs):
        self.loc = loc
        self.method = method
        self.config = kwargs
        self.prepath = prepath

    def url(self, path: str, options: dict = {}) -> str:
        # thanks to https://pakstech.com/blog/python-build-urls/
        query = urlencode(self.config | options)
        path = urljoin(self.prepath, path)
        return urlunsplit((self.method, self.loc, path, query, ""))

    async def get(self, path: str, **kwargs) -> dict:
        """Get an api path, passing kwargs to self.url when creating the url"""
        async with aiohttp.ClientSession() as session:
            url = self.url(path, **kwargs)
            async with session.get(url) as response:
                json = await response.json()
                return json

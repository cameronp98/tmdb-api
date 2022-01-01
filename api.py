import aiohttp
from urllib.parse import urlencode, urlunsplit, urljoin


class Api:
    def __init__(self, loc: str, method: str = "https", prepath: str = "", **kwargs):
        self.loc = loc
        self.method = method
        self.config = kwargs
        self.prepath = prepath

    def url(self, path: str, options: dict = {}) -> str:
        query = urlencode(self.config | options)
        path = urljoin(self.prepath, path)
        return urlunsplit((self.method, self.loc, path, query, ""))

    # get an api path, passing kwargs to self.url when creating the url
    async def get(self, path: str, **kwargs) -> dict:
        async with aiohttp.ClientSession() as session:
            url = self.url(path, **kwargs)
            async with session.get(url) as response:
                json = await response.json()
                return json

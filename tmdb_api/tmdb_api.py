from .api import Api


class TmdbApi(Api):
    def __init__(self, api_key: str, language: str = "en-GB"):
        super().__init__("api.themoviedb.org", api_key=api_key, prepath="3/", language="en-GB")

    async def movie(self, movie_id: int) -> dict:
        return await self.get(f"movie/{movie_id}")

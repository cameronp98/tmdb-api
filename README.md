## TheMovieDB API python client

Example usage:

```powershell
# set your api key (PowerShell example)
$Env:API_KEY = "<your api key goes here>"
```


```python
import asyncio
from tmdb_api import TmdbApi
import os


async def print_movie(api: TmdbApi, movie_id: int):
    movie = await api.movie(movie_id)
    print(f"{movie['title']:30s} {movie['tagline']}")


async def main():
    api = TmdbApi(os.environ["API_KEY"])
    movie_ids = [500, 234, 600]
    await asyncio.gather(*[print_movie(api, movie_id) for movie_id in movie_ids])


if __name__ == "__main__":
    # avoids windows specific issue, see https://stackoverflow.com/a/66772242
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
```
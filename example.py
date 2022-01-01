import asyncio
from tmdb_api import TmdbApi
import os


async def get_m(api: TmdbApi, movie_id: int):
    movie = await api.movie(movie_id)


async def main():
    api = TmdbApi(os.environ["API_KEY"])

    movie_ids = [500, 234, 600]

    movies = await asyncio.gather(*map(api.movie, movie_ids))

    for i, movie in enumerate(movies):
        print(f"{i+1:2} | {movie['title']:30} ({movie['tagline']})")


if __name__ == "__main__":
    # avoids windows specific issue, see https://stackoverflow.com/a/66772242
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())

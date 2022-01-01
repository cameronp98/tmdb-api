import asyncio
from tmdb_api import TmdbApi


async def print_movie(api: TmdbApi, movie_id: int):
    movie = await api.movie(movie_id)
    print(f"{movie['title']:30s} {movie['tagline']}")


async def main():
    api = TmdbApi("9d06230e3f4da8449e1cc130c656be68")
    movie_ids = [500, 234, 600]
    await asyncio.gather(*[print_movie(api, movie_id) for movie_id in movie_ids])


if __name__ == "__main__":
    # avoids windows specific issue, see https://stackoverflow.com/a/66772242
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())

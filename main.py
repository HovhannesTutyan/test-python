from time import sleep, perf_counter

def task():
    print('Starting task ...')
    sleep(1)
    print('done')

start_time = perf_counter()

task()
task()

end_time = perf_counter()

print(f'It took {end_time - start_time: 0.2f} seconds to complete')




import aiohttp
import asyncio
import requests
import time

# start_time = time.time()


# pokemon_url = "https://pokeapi.co/api/v2/pokemon/25"
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(pokemon_url) as resp:
#             pokemon = await resp.json()
#             print(pokemon["name"])
# asyncio.run(main())


# pokemon = requests.get(pokemon_url)
# print(pokemon.json())


# async def main():
#     async with aiohttp.ClientSession() as session:
#         for number in range(1,151):
#             pokemon_uri = f'https://pokeapi.co/api/v2/pokemon/{number}'
#             async with session.get(pokemon_uri) as resp:
#                 pokemon = await resp.json()
#                 print(pokemon["name"])
# asyncio.run(main())
# print("---%s seconds ---" % (time.time() - start_time))


# for number in range(1,151):
#     pokemon_uri = f'https://pokeapi.co/api/v2/pokemon/{number}'
#     pokemon = requests.get(pokemon_uri)
#     print(pokemon.json()["name"])
# print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon["name"]
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1,151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))
        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))



import asyncio
import aiohttp
import asyncpg
import json

WEB_SERVER_URL = "https://rnacentral.org/api/v1/rna/"
DB_CONNECTION_STRING = "postgres://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs"

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def query_database(connection_string, query):
    connection = await asyncpg.connect(connection_string)
    try:
        return await connection.fetch(query)
    finally:
        await connection.close()

async def main():
    url_task = fetch_data(WEB_SERVER_URL)
    db_task = query_database(DB_CONNECTION_STRING, "SELECT * FROM Rna LIMIT 5")  

    url_result, db_result = await asyncio.gather(url_task, db_task)

    # Работа с результатами
    print("Result from URL:", json.dumps(url_result, indent=2))
    print("Result from Database:")
    for row in db_result:
        print(row)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass

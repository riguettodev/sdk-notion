import sys, os, asyncio
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..', '..', '..', '..', '..', '..', '..'
        )
    )
)
from src.utils.pprint import pprint
from src.integrations.notion.orm.repositories.pages.GetPage import GetPage

async def main():
    instance = GetPage()
    search = await instance\
        .set_database(name="accounts")\
        .set_pageid("0db2806f-b365-4327-919d-afbd1943f2ad")\
        .select("Name")
        #.call(True)
    return search

test = await main()
pprint(test)

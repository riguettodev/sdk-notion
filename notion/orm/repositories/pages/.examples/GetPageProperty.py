import sys, os, asyncio
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..', '..', '..', '..', '..', '..', '..'
        )
    )
)
from src.utils.pprint import pprint
from src.integrations.notion.orm.repositories.pages.GetPageProperty import GetPageProperty

async def main():
    instance = GetPageProperty()
    search = await instance\
        .set_pageid("0db2806f-b365-4327-919d-afbd1943f2ad")\
        .set_propname("Movements")\
        .call()
    return search

test = await main()
pprint(test)

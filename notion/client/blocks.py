import httpx
from typing import Dict

class Blocks:

    "Reference: https://developers.notion.com/reference/retrieve-a-block"

    def __init__(self, headers : Dict[str, str]):
        self._headers = headers

    async def get(self, block_id : str):

        "Busca detalhes de um bloco"

        async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:

            response = await client.get(
                f'https://api.notion.com/v1/blocks/{block_id}',
                headers = self._headers
            )

            return response.json()

    async def get_children(self, block_id : str):

        "Busca pelos blocos de um bloco ou página"

        async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:

            response = await client.get(
                f'https://api.notion.com/v1/blocks/{block_id}/children',
                headers = self._headers
            )

            return response.json()

__all__ = ["Blocks"]
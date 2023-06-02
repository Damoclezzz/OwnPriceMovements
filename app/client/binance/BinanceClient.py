import asyncio
from typing import List
import aiohttp
from app.client.AbstractClient import AbstractClient


class BinanceClient(AbstractClient):
    GET_KLINES_API = {
        'path': '/api/v3/klines',
        'method': 'GET',
        'params': {
            'interval': '1m',
            'limit': 60,
        },
    }

    def __init__(self, base_url: str):
        super().__init__(base_url)

    async def get_last_hour_klines(self, pair: str) -> List[List]:
        async with aiohttp.ClientSession() as session:
            params = BinanceClient.GET_KLINES_API['params']
            params['symbol'] = pair

            response = await session.request(
                    method=BinanceClient.GET_KLINES_API['method'],
                    url=self.base_url + BinanceClient.GET_KLINES_API['path'],
                    params=params,
            )

            if response.status == 200:
                return await response.json()
            else:
                return await self.get_last_hour_klines(pair)


if __name__ == '__main__':
    from config import BINANCE_PUBLIC_BASE_URL
    import pprint

    client = BinanceClient(BINANCE_PUBLIC_BASE_URL)

    async def main():
        pprint.pprint(await client.get_last_hour_klines('BTCUSDT'))


    asyncio.run(main())

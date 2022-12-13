import aiohttp


class Request:
    def __init__(self, url, data, headers):
        self.url = url
        self.data = data
        self.headers = headers

    async def request(self):
        async with aiohttp.ClientSession as session:
            async with session.post(self.url,
                                    headers=self.headers,
                                    data=self.data) as response:
                return response.json()

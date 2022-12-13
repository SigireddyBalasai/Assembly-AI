import aiofiles
import aiohttp
from Base.BaseRequest import Request


async def _upload_file(filepath: str):
    async with aiofiles.open(filepath, "rb") as file:
        while True:
            data = await file.read(5242880)
            if not data:
                break
            yield data


class Requests:
    def __init__(self, authorization: str):
        self.headers = {"authorization": authorization}

    async def upload_file(self, filepath):
        data = await _upload_file(filepath)
        request = Request(url='https://api.assemblyai.com/v2/upload', data=data, headers=self.headers)
        ok = await request.request()
        print(ok.__dict__)

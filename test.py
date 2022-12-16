import time

import asyncio

from AssembleAI import File_upload

request = File_upload.Requests("fbba59e571c74f05a80505312ff29917")
loop = asyncio.get_event_loop()
url = loop.run_until_complete(request.upload_file('WhatsApp Audio 2022-12-15 at 16.13.36.waptt.opus'))
id = loop.run_until_complete(request.get_transcription(url))
while(True):
    ok = loop.run_until_complete(request.get_result(id))
    time.sleep(2)

import aiohttp
import asyncio
import json

async def transcribe_audio(file_path):
    url = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize"
    headers = {
        "Authorization": "Bearer YOUR_OAUTH_TOKEN"
    }

    with open(file_path, "rb") as audio_file:
        data = audio_file.read()

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as resp:
            return await resp.json()

def save_to_txt(result, file_path):
    with open(file_path, "w") as txt_file:
        txt_file.write(json.dumps(result))

async def main():
    result = await transcribe_audio("path_to_your_audio_file.wav")
    save_to_txt(result, "result.txt")
    print("Result saved to result.txt")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

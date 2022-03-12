import os
import asyncio
import discii

from dotenv import load_dotenv

client = discii.Client()


@client.on("READY")
async def bot_ready(e) -> None:
    print(f"The client is ready. The client's latency is {round(client.latency * 1000)}s")


@client.error
async def error_handler(coro, error) -> None:
    print(coro, error)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(client.start(os.environ["BOT_TOKEN"]))

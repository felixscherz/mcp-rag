from mcp.client.sse import sse_client
from mcp.client.session import ClientSession
import asyncio
import logging
logger = logging.getLogger()

logging.basicConfig(level=logging.INFO)


async def connect(endpoint: str):
    async with sse_client(f"{endpoint}/sse") as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await session.initialize()

            while True:
                what = input("what to do? ")
                if what == "list":
                    res = await session.list_prompts()
                    print(res)
                elif what == "tools":
                    res = await session.list_tools()
                    print(res)

                else:
                    res = await session.call_tool(what, {"message": "abc"})
                    print(res)



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--host")
    parser.add_argument("--port", type=int)

    options = parser.parse_args()

    endpoint = f"http://{options.host}:{options.port}"
    asyncio.run(connect(endpoint))


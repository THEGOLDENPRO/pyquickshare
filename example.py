import asyncio
import contextlib
import sys
from logging import DEBUG, basicConfig

import pyquickshare

basicConfig(level=DEBUG)


async def send(file: str) -> None:
    first = await anext(pyquickshare.discover_services())

    return await pyquickshare.send_to(first, file=file)


async def main(argv: list[str]) -> None:
    if len(argv) < 2:
        print("Usage: example.py <mode> [args...]")
        return

    if argv[1] == "send":
        if len(argv) < 3:
            print("Usage: example.py send <file>")
            return
        await send(argv[2])
    elif argv[1] == "receive":
        async for request in pyquickshare.receive():
            results = await request.accept()
            print(results)

    else:
        print("Unknown mode:", argv[1])


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main(sys.argv))

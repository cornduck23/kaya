import asyncio
import logging

from shared.logging.config import setup_logging

from src.bot import start_bot


setup_logging(service_name="bot")
logger = logging.getLogger(__name__)


async def main():
    await start_bot()


if __name__ == "__main__":
    asyncio.run(main())

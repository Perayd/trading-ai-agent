import asyncio
import config
from exchange import BasePerpExchange
from agent import TradingAgent

async def main():
    exchange = BasePerpExchange(
        config.API_KEY,
        config.API_SECRET
    )

    agent = TradingAgent(exchange, config)

    while True:
        await agent.run()
        await asyncio.sleep(60)

asyncio.run(main())

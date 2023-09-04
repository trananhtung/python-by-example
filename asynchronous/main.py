import asyncio
import time

import aiohttp


async def get_rates(session: aiohttp.ClientSession, base: str = "USD"):
    """Get rates."""
    async with session.get(f"https://api.vatcomply.com/rates?base={base}") as response:
        rates = (await response.json())["rates"]
        rates[base] = 1
        
        return base, rates
      

SYMBOLS = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')
BASES = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')

def present_result(base, rates):
    """Present result."""
    rates_line = ", ".join(
        [f"{float(rates[symbol]):10.03} {symbol}" for symbol in SYMBOLS]
    )
    print(f"1 {base} = {rates_line}")

async def main():
    """Main."""
    async with aiohttp.ClientSession() as session:
        for result in await asyncio.gather(*[
            get_rates(session, base)
            for base in BASES
        ]):
            present_result(*result)
        


if __name__ == "__main__":
    started = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    elapsed = time.time() - started
    print()
    print("time elapsed: {:.2f}s".format(elapsed))

import asyncio
import ccxt
import time

async def cctx_prices():
    deribit = ccxt.deribit()
    while True:
        localtime = time.strftime("20%y-%m-%d %H:%M:%S", time.localtime())
        ticker = deribit.fetch_ticker('BTC-PERPETUAL')
        #print(ticker)
        
        symbol = ticker['symbol']
        datetime = ticker['datetime']
        last = ticker['last']
        #change = ticker['info']['stats']['price_change']
        print( localtime, symbol, last )
        
        # pause asyncio for 1 second
        await asyncio.sleep(1) 

loop = asyncio.get_event_loop()
asyncio.ensure_future(cctx_prices())
loop.run_forever()

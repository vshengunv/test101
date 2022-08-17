

import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth

async def main():
    browser = await  launch(headless=True)
    page = await  browser.newPage()

    await stealth(page)

    await page.goto("https://bot.sannysoft.com/")
    await browser.close()





if __name__ == '__main__':
    # TestMylog.print_log(webdriver.Chrome())
    asyncio.get_event_loop().run_until_complete(main())
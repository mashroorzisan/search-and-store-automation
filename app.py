from playwright.sync_api import sync_playwright
parsed = []# database

def search_google(query):
    with sync_playwright() as playwright:
        # making a browser
        # create a new browser context
        # create a new page
        # goto a link
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        
        context = browser.new_context()
        
        page = context.new_page()
        
        page.goto('https://google.com/')

        # locate search box
        # fill in the box with the search term after 100ms
        search_box = page.locator('textarea[title="Search"]')
        
        search_box.type(query, delay=100)
        
        search_box.press('Enter')

        # scrape new page for all the link with attribute 'jsname="UWckNb"
        
        item_list = page.locator('a[jsname="UWckNb"]').all()
        
        # iterate over the scraped item to get the link from the href attribute
        # after getting the link store it into a database or in this case store it into a list
        for item in item_list:
            link = item.get_attribute('href')
            parsed.append(link) # database

        browser.close()

query = input("What do you want to search?")
search_google(query)
print(parsed)
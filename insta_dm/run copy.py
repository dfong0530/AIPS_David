import asyncio
from pyppeteer import launch

#Function to login to instagram. Username and password removed.

async def login(page, username, password):


    await page.goto('https://www.instagram.com/accounts/login/?next=https%3A%2F%2Fwww.instagram.com%2Fdirect%2Ft%2F17844557712007222%2F%3F__coig_login%3D1')

    username_selector = 'input[name="username"]'
    password_selector = 'input[name=password]'

    await page.waitForSelector(username_selector)
    await page.waitForSelector(password_selector)

    await page.type(username_selector, username)
    await page.type(password_selector, password)


    await asyncio.sleep(3)

    submit_button_selector = 'button[type="submit"]'
    await page.waitForSelector(submit_button_selector)
    await page.click(submit_button_selector)


#Functionality to navigate to user instagram page, direct message

async def send_message(page, username, msg):

    #Navigate to instagram page
    await page.goto(f"https://www.instagram.com/{username}/")

    await asyncio.sleep(3)

    #Click DM Button

    message_button_xpath = "//div[@role='button' and contains(text(), 'Message')]"

    await page.waitForXPath(message_button_xpath, {'timeout': 5000})
    message_button = await page.xpath(message_button_xpath)
    await message_button[0].click()


    await asyncio.sleep(5)


    #Check if there's a popup

    button_xpath = "//button[text()='Not Now']"

    button = await page.xpath(button_xpath)


    if button:
        await button[0].click()

    await asyncio.sleep(3)


    #Type message in message box

    message_box_selector = 'div[aria-label="Message"][contenteditable="true"]'

    await page.waitForSelector(message_box_selector)
    await page.focus(message_box_selector)
    await page.keyboard.type(msg)


    #Send Message

    send_button_xpath = "//div[@role='button' and contains(text(), 'Send')]"

    await page.waitForXPath(send_button_xpath)
    send_button = await page.xpath(send_button_xpath)
    await send_button[0].click()

    await asyncio.sleep(3)




async def read_usernames(old, new):

    ret = []
    seen = set([])

    with open(old, "r") as f:

        for username in f:
            seen.add(username.replace("\n", ""))

    with open(new, "r") as f:
        for username in f:
           username = username.replace("\n", "")
           if username not in seen:
 
               ret.append(username)

    return ret


#Logins, reads in file with usernames and sends dm's

async def main():

    try:


        username = "Enter Username HERE"
        password = "Enter Password HERE"

        msg = "Chepaer Amazon Products Found Here: "


        #Get usernames to write into
        usernames = await read_usernames("seen.txt", "read.txt")
        seen = open("seen.txt", "a")


        browser = await launch(headless=False)
        page = await browser.newPage()

        await login(page, username, password)


        

        for i in range(len(usernames)):

            await asyncio.sleep(5)

            try:
            
                await send_message(page, usernames[i], msg)
                

            except:
                print("Error")

            finally:
                seen.write(usernames[i] + "\n")


    finally:

        seen.close()
        await browser.close()

asyncio.get_event_loop().run_until_complete(main())
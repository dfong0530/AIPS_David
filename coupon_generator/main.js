

//Website that gives us free coupons.
//Using pupeteer to simulate human and populate coupons.

const puppeteer = require('puppeteer');

// Utility function for waiting
async function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function generateRandomString(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const charactersLength = characters.length;
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

console.log(generateRandomString(26));


async function getCoupon() {
    const browser = await puppeteer.launch({ headless: false }); // Consider headless mode for production
    for (let j = 0; j < 1000; j++) {
        const beg = generateRandomString(26);
        for (let i = 0; i < 10; i++) {
            //const context = await browser.createIncognitoBrowserContext();
            const page = await browser.newPage();
            try {
                const email = `${beg}${i}@dfong0530.com`;
                await page.goto('https://vizervelocity.com/3b1dc453-4278-41d7-97be-9d60ad50471f');
                await wait(500);
                await page.type('#auth', email);
                await wait(500);
                await page.click('#root > div > section > div.auth-container > div.form > div > button');
                await wait(1000);

            } catch (error) {
                console.error(`Error in iteration ${i}:`, error);
            } finally {
                await page.close();
                await wait(1000);
            }
        }
    }
    await browser.close();
}

// Define the main function that calls performAction
async function main() {
    await getCoupon();
}

// Call the main function
main();
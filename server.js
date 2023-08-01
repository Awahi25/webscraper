const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio');

const app = express();
const port = process.env.PORT || 3000;

app.get('/scrape', async (req, res) => {
    const url = req.query.url;
    let data = {};

    try {
        const response = await axios.get(url);
        const $ = cheerio.load(response.data);

        // Define the selectors to find the elements containing the business data
        // The actual selectors depend on the structure of the website you're scraping
        const nameSelector = 'h1';
        const addressSelector = 'p';
        const phoneSelector = 'a';
        const emailSelector = 'a';
        const websiteSelector = 'a';

        data = {
            name: $(nameSelector).text(),
            address: $(addressSelector).text(),
            phone: $(phoneSelector).text(),
            email: $(emailSelector).text(),
            website: $(websiteSelector).text()
        };
    } catch (error) {
        console.log(error);
    }

    res.json(data);
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});

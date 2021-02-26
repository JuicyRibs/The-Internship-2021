const puppeteer = require("puppeteer");
const express = require("express");
const app = express();

const data = async () => {
  const companyList = [];
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto("https://theinternship.io/");

  try {
    await page.waitForSelector(".partner");
    const companyElementList = await page.$$(".partner");
    for (const company of companyElementList) {
      const companyObj = await {
        logo: await company.$eval(".logo-box a img", (img) =>
          img.getAttribute("src")
        ),
        text: await company.$eval(
          ".box-textbox .list-company",
          (text) => text.innerHTML
        ),
      };
      companyList.push(companyObj);
    }
    browser.close();
    companyList.sort((a, b) => {
      return a.text.length - b.text.length;
    });
    return companyList;
  } catch (err) {
    console.log(err);
  }
};

app.get("/companies", async (req, res, next) => {
  data().then((data) => {
    const companyWrapper = {
      companies: [],
    };
    data.forEach((company) => {
      companyWrapper.companies.push({
        logo: "https://theinternship.io/" + company.logo,
      });
    });
    return res.json(companyWrapper);
  });
});

app.listen(3001, () => {
  console.log("Server is up on http://localhost:3001");
});
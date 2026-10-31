import { ApifyClient } from "apify-client";

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor("swissalpinedata/eu-ats-jobs").call({
  "companies": [
    "https://ottonova.jobs.personio.de",
    "https://apply.workable.com/blueground",
    "https://bunq.recruitee.com",
    "https://jobs.smartrecruiters.com/BoschGroup",
    "https://polestar.teamtailor.com"
  ],
  "includeDescription": true,
  "maxItems": 20
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(JSON.stringify(items, null, 2));
console.log(`${items.length} records`);

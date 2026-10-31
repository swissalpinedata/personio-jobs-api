# Personio, Workable, Recruitee, SmartRecruiters and Teamtailor jobs API in Python and Node

Get every open job from company career sites on **Personio, Workable, Recruitee, SmartRecruiters and Teamtailor** in one flat JSON format. The [EU ATS Jobs Scraper](https://apify.com/swissalpinedata/eu-ats-jobs) on Apify detects the ATS from the careers URL and reads its public job feed (Personio XML, Teamtailor RSS, the others JSON).

Pay per result, no subscription, no login and no proxy setup. New Apify accounts get free monthly credit, which covers a few thousand results.

## Quick start

1. Create a free account on [Apify](https://apify.com) and copy your API token from Settings, Integrations.
2. `export APIFY_TOKEN=your_token`
3. Run one of the examples below.

### Python

```bash
pip install apify-client
python example.py
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("swissalpinedata/eu-ats-jobs").call(run_input={
    "companies": [
        "https://ottonova.jobs.personio.de",
        "https://apply.workable.com/blueground",
        "https://bunq.recruitee.com",
        "https://jobs.smartrecruiters.com/BoschGroup",
        "https://polestar.teamtailor.com"
    ],
    "includeDescription": true,
    "maxItems": 20
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item)
```

### Node.js

```bash
npm install apify-client
node example.mjs
```

```js
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
console.log(items);
```

### curl

```bash
curl -X POST "https://api.apify.com/v2/acts/swissalpinedata~eu-ats-jobs/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"companies": ["https://ottonova.jobs.personio.de", "https://apply.workable.com/blueground", "https://bunq.recruitee.com", "https://jobs.smartrecruiters.com/BoschGroup", "https://polestar.teamtailor.com"], "includeDescription": true, "maxItems": 20}'
```

## Example output

One record looks like this:

```json
{
  "source": "recruitee",
  "company_slug": "bunq",
  "company_name": "bunq",
  "job_id": "2800490",
  "title": "Data Scientist Marketing",
  "department": "Growth",
  "location": "Amsterdam, Noord-Holland, Netherlands",
  "city": "Amsterdam",
  "region": "Noord-Holland",
  "country": "Netherlands",
  "remote": "hybrid",
  "employment_type": "fulltime_permanent",
  "seniority": "experienced",
  "published_at": "2026-10-28T13:21:58+00:00",
  "url": "https://careers.bunq.com/o/data-scientist-marketing-3",
  "apply_url": "https://careers.bunq.com/o/data-scientist-marketing-3/c/new",
  "description": "At bunq, we're on a mission to Make Life Easy for our users by creating the most user-centric banking experience out there. ...",
  "scraped_at": "2026-10-30T23:15:28.145188+00:00"
}
```

## What you can build

* Hiring signals for sales: "company X is hiring 5 engineers"
* Competitor and target account monitoring
* Job board aggregation from career sites
* Recruiting agency lead lists

## Schedules and integrations

On Apify you can save this input as a task, run it on a schedule (for example every morning) and send new results to Google Sheets, Slack, a webhook, Make, n8n or Zapier without writing code. All input fields are documented on the [actor page](https://apify.com/swissalpinedata/eu-ats-jobs).

## More Swiss and DACH data APIs

* [swiss-jobs-api](https://github.com/swissalpinedata/swiss-jobs-api): Swiss Jobs API
* [arbeitsagentur-jobs-api](https://github.com/swissalpinedata/arbeitsagentur-jobs-api): Arbeitsagentur Jobsuche API
* [zefix-api-python](https://github.com/swissalpinedata/zefix-api-python): Zefix API in Python
* [austria-jobs-api](https://github.com/swissalpinedata/austria-jobs-api): Austria Jobs API
* [flatfox-api-python](https://github.com/swissalpinedata/flatfox-api-python): Flatfox API

## License

The example code in this repo is MIT licensed. The data comes from public sources; you are responsible for using it in line with the GDPR and the terms of the source sites.

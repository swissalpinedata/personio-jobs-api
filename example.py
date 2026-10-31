import json
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

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(json.dumps(items, ensure_ascii=False, indent=2))
print(f"{len(items)} records", flush=True)

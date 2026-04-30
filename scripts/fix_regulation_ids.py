import json

mapping = {
    "gdpr": "ee6a8d6b-7f25-4ee7-85c0-f4367ebfffe3",
    "dora": "957ab6ae-2a0a-4264-b2b4-2b1b74991095",
    "eu_ai_act": "24a681a4-cd40-45e8-b802-03f5c79283e6",
    "amld6": "e4127b7c-c1f9-48b7-bf54-1d55eb722994"
}

with open("/Users/mehreenhimani/Portfolio/RegCopilot/chunks/ingest_payload.json") as f:
    data = json.load(f)

for group in data:
    slug = group["regulation_id"]
    group["regulation_id"] = mapping.get(slug, slug)

with open("/Users/mehreenhimani/Portfolio/RegCopilot/chunks/ingest_payload.json", "w") as f:
    json.dump(data, f)

print("Done — UUIDs replaced")

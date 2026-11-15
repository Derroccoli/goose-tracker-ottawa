"""Bake every geotagged Canada Goose Sighting in the City of Ottawa into data/geese.json."""
import json, time, urllib.request
from pathlib import Path

PLACE_ID = 27599  # iNaturalist "Ottawa, ON, CA" (City of Ottawa)
TAXON_ID = 7089   # Branta canadensis
OUT = Path(__file__).resolve().parent.parent / "data"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "goose-hackathon/0.1"})
    return json.load(urllib.request.urlopen(req, timeout=30))

sightings, id_above = [], 0
while True:
    page = get("https://api.inaturalist.org/v1/observations?"
               f"taxon_id={TAXON_ID}&place_id={PLACE_ID}&geo=true&per_page=200"
               f"&order_by=id&order=asc&id_above={id_above}")
    rows = page["results"]
    if not rows:
        break
    for r in rows:
        lng, lat = r["geojson"]["coordinates"]
        sightings.append({"id": r["id"], "lat": round(lat, 5), "lng": round(lng, 5),
                          "t": r.get("time_observed_at") or r.get("observed_on"),
                          "where": r.get("place_guess") or "", "by": r["user"]["login"]})
    id_above = rows[-1]["id"]
    print(len(sightings), end=" ", flush=True)
    time.sleep(1)

(OUT / "geese.json").write_text(json.dumps(sightings, separators=(",", ":")))

place = get(f"https://api.inaturalist.org/v1/places/{PLACE_ID}")["results"][0]
(OUT / "ottawa.json").write_text(json.dumps(place["geometry_geojson"], separators=(",", ":")))
print(f"\n{len(sightings)} sightings saved")

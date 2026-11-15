# Where Da Goose At — Ottawa Edition

A heatmap of every recorded Canada Goose sighting in the City of Ottawa, with a live readout of the nearest goose and our own recorded voice lines on a loop.

- Heatmap of ~6,500 iNaturalist sightings across Ottawa, plus live refresh of the newest ones
- Nearest-goose distance and compass direction, colour-coded as you get closer
- Three recorded voice lines, played in turn every 20 seconds with subtitles
- HONK button to report your own goose (stored locally on your device)
- Ottawa only: map bounded to the city

**Live:** https://derroccoli.github.io/goose-tracker-ottawa/

## Run it

```sh
python3 -m http.server 8765
# open http://localhost:8765
```

Location requires a secure context, so on a phone it must be served over HTTPS (e.g. GitHub Pages).

## Refresh the data

```sh
python3 scripts/fetch_geese.py   # rewrites data/geese.json and data/ottawa.json
```

## Credits

Sightings: [iNaturalist](https://www.inaturalist.org) contributors (taxon 7089, place 27599). Individual observations are licensed by their observers, mostly CC BY-NC. Basemap © Esri, HERE, Garmin, © OpenStreetMap contributors. Goose honk: "Low flyover by five Canadian Geese" by Extemporalist, recorded in the Okanagan, BC ([Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Low_flyover_by_five_Canadian_Geese.flac), CC0). Voice: our own recordings.

Built at a stupid hackathon.

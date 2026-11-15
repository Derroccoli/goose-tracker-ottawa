# Goose Tracker (Ottawa)

A heatmap of Canada Goose sightings across the City of Ottawa, narrated by G.O.O.S.E., a butler-AI that nags you about the nearest goose every 10 seconds.

## Glossary

- **Sighting** — one recorded goose observation: location, time, observer. From iNaturalist (taxon 7089, place 27599) or a HONK.
- **Nearest Goose** — the closest Sighting from the last 365 days to the user's position. All Sightings feed the heatmap; only recent ones can be the Nearest Goose.
- **HONK** — a Sighting the user reports at their own position. Stored on the device only (localStorage), no backend.
- **Hotspot** — informal: a dense area on the heatmap. Not tracked or announced.
- **Nag** — one spoken + subtitled line from G.O.O.S.E. Fired every 10 s, and immediately when the Urgency tier changes.
- **Urgency** — tier from distance to the Nearest Goose: far (>3 km), mid (1–3 km), near (250 m–1 km), danger (<250 m).
- **Direction** — compass word from user to goose: N, S, E, W and the diagonals (NE, NW, SE, SW). No degrees.
- **G.O.O.S.E.** — Geospatial Ornithological Observation & Surveillance Engine. Original persona: dry butler, "sir" by default (sir / ma'am / commander).

## Rules

- Ottawa only: map is bounded to the city; outside the boundary G.O.O.S.E. still reports the nearest Ottawa goose and remarks that you've left.
- Location denied: assume Parliament Hill and be passive-aggressive about it.
- Quips are generated in code (templates × openers × closers, no repeats). No LLM — 10 s cadence makes an API too slow/costly and fragile for a demo.

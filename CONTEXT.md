# Goose Tracker (Ottawa)

A heatmap of Canada Goose sightings across the City of Ottawa, with our own recorded voice lines playing on a loop.

## Glossary

- **Sighting** — one recorded goose observation: location, time, observer. From iNaturalist (taxon 7089, place 27599) or a HONK.
- **Nearest Goose** — the closest Sighting from the last 365 days to the user's position. All Sightings feed the heatmap; only recent ones can be the Nearest Goose.
- **HONK** — a Sighting the user reports at their own position. Stored on the device only (localStorage), no backend.
- **Hotspot** — informal: a dense area on the heatmap. Not tracked or announced.
- **Voice Line** — one of three recorded clips, played in turn every 20 s with its words in the speech bubble.
- **Urgency** — tier from distance to the Nearest Goose: far (>3 km), mid (1–3 km), near (250 m–1 km), danger (<250 m).
- **Direction** — compass word from user to goose: N, S, E, W and the diagonals (NE, NW, SE, SW). No degrees.

## Rules

- Ottawa only: map is bounded to the city; outside the boundary the readout still shows the nearest Ottawa goose.
- Location denied: assume Parliament Hill.
- Voice lines are fixed recordings, not generated. Distance and direction live in the readout, not the speech.

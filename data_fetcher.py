import json
import time

import requests


REGION = "Chicago metropolitan area, Illinois, USA"

PLACES = {
    "Chicago": "Chicago, Illinois, USA",
    "Evanston": "Evanston, Illinois, USA",
    "Skokie": "Skokie, Illinois, USA",
    "Morton Grove": "Morton Grove, Illinois, USA",
    "Niles": "Niles, Illinois, USA",
    "Wilmette": "Wilmette, Illinois, USA",
    "Glenview": "Glenview, Illinois, USA",
    "Northbrook": "Northbrook, Illinois, USA",
    "Park Ridge": "Park Ridge, Illinois, USA",
    "Des Plaines": "Des Plaines, Illinois, USA",
    "Rosemont": "Rosemont, Illinois, USA",
    "Schiller Park": "Schiller Park, Illinois, USA",
    "Franklin Park": "Franklin Park, Illinois, USA",
    "Melrose Park": "Melrose Park, Illinois, USA",
    "River Forest": "River Forest, Illinois, USA",
    "Oak Park": "Oak Park, Illinois, USA",
    "Forest Park": "Forest Park, Illinois, USA",
    "Berwyn": "Berwyn, Illinois, USA",
    "Cicero": "Cicero, Illinois, USA",
    "Elmwood Park": "Elmwood Park, Illinois, USA",
}

CONNECTIONS = [
    ("Chicago", "Evanston"),
    ("Evanston", "Skokie"),
    ("Skokie", "Morton Grove"),
    ("Morton Grove", "Niles"),
    ("Evanston", "Wilmette"),
    ("Wilmette", "Glenview"),
    ("Glenview", "Northbrook"),
    ("Niles", "Park Ridge"),
    ("Park Ridge", "Des Plaines"),
    ("Des Plaines", "Rosemont"),
    ("Rosemont", "Schiller Park"),
    ("Schiller Park", "Franklin Park"),
    ("Franklin Park", "Melrose Park"),
    ("Melrose Park", "River Forest"),
    ("River Forest", "Oak Park"),
    ("Oak Park", "Forest Park"),
    ("Forest Park", "Berwyn"),
    ("Berwyn", "Cicero"),
    ("Franklin Park", "Elmwood Park"),
    ("Chicago", "Oak Park"),
    ("Chicago", "Cicero"),
    ("Skokie", "Glenview"),
    ("Niles", "Glenview"),
    ("Park Ridge", "Rosemont"),
    ("Oak Park", "Berwyn"),
]

HEADERS = {
    "User-Agent": "Shrau-Chicago-Search-Visualizer/1.0"
}


def get_coordinates(place_query):
    response = requests.get(
        "https://nominatim.openstreetmap.org/search",
        params={"q": place_query, "format": "json", "limit": 1},
        headers=HEADERS,
        timeout=20,
    )
    response.raise_for_status()
    results = response.json()

    if not results:
        raise ValueError(f"Could not find {place_query}")

    return {
        "lat": float(results[0]["lat"]),
        "lon": float(results[0]["lon"]),
    }


def get_road_distance(start, end):
    # OSRM uses longitude first, then latitude.
    url = (
        "https://router.project-osrm.org/route/v1/driving/"
        f"{start['lon']},{start['lat']};{end['lon']},{end['lat']}"
    )

    response = requests.get(
        url,
        params={"overview": "false"},
        timeout=20,
    )
    response.raise_for_status()
    result = response.json()

    if not result.get("routes"):
        raise ValueError(f"No road route found: {result}")

    meters = result["routes"][0]["distance"]
    return round(meters / 1000, 2)


def main():
    coordinates = {}

    print("Getting place coordinates...")
    for name, query in PLACES.items():
        coordinates[name] = get_coordinates(query)
        print(f"  {name}: {coordinates[name]}")
        time.sleep(1.1)

    graph = {name: {} for name in PLACES}

    print("Getting road distances...")
    for first, second in CONNECTIONS:
        distance = get_road_distance(
            coordinates[first],
            coordinates[second],
        )

        graph[first][second] = distance
        graph[second][first] = distance

        print(f"  {first} to {second}: {distance} km")

    # Follow connections to make sure all 20 places can be reached.
    visited = set()
    places_to_check = ["Chicago"]

    while places_to_check:
        place = places_to_check.pop()
        if place not in visited:
            visited.add(place)
            places_to_check.extend(graph[place])

    if len(visited) != len(PLACES):
        raise ValueError("Some places are disconnected from the graph")

    map_data = {
        "region": REGION,
        "total_cities": len(coordinates),
        "total_edges": len(CONNECTIONS),
        "locations": coordinates,
        "graph": graph,
    }

    with open("map_data.json", "w", encoding="utf-8") as file:
        json.dump(map_data, file, indent=2)

    print(
        f"Saved map_data.json with "
        f"{len(PLACES)} places and {len(CONNECTIONS)} connections."
    )


if __name__ == "__main__":
    main()

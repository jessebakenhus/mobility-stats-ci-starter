import csv
import os
from collections import defaultdict


def load_rides(path: str) -> list[dict[str, object]]:
    """Load ride data from a CSV file."""
    x = []
    if not os.path.exists(path):
        raise FileNotFoundError(f"Could not find file: {path}")
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for col in reader:
            col_copy = col.copy()
            x.append(
                {
                    "ride_id": col_copy["ride_id"],
                    "start_station": col_copy["start_station"],
                    "end_station": col_copy["end_station"],
                    "duration_min": float(col_copy["duration_min"]),
                    "rider_type": col_copy["rider_type"],
                }
            )
    return x


def average_duration(duration):
    """Return the average ride duration in minutes."""
    if len(duration) == 0:
        return 0.0
    avg_duration = 0.0
    for dur in duration:
        avg_duration += dur["duration_min"]
    return avg_duration / len(duration)


def count_by_rider_type(rides):
    """Count rides for each rider type."""
    dictionary = defaultdict(int)
    for ride in rides:
        dictionary[ride["rider_type"]] += 1
    return dict(dictionary)


def busiest_start_station(rides):
    """Return the start station with the most rides."""
    if rides is None:
        raise ValueError("rides must not be None")
    if len(rides) == 0:
        raise ValueError("rides must not be empty")
    stations = {}
    for ride in rides:
        current_start_station = ride["start_station"]
        stations[current_start_station] = stations.get(current_start_station, 0) + 1
    return max(stations, key=stations.get)


def filter_long_rides(rides, mins=30):
    """Return all rides with duration greater than or equal to b minutes."""
    all_rides = []
    for ride in rides:
        if ride["duration_min"] >= mins:
            all_rides.append(ride)
    return all_rides

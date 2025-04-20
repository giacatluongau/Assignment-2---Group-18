import os
import csv
from collections import defaultdict

SEASONS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}

DATA_DIR = "temperature_data"

def calculate_average_temperatures():
    season_totals = defaultdict(float)
    season_counts = defaultdict(int)

    for file in os.listdir(DATA_DIR):
        if file.endswith(".csv"):
            with open(os.path.join(DATA_DIR, file), mode="r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for season, months in SEASONS.items():
                        for month in months:
                            if month in row and row[month] and row[month].replace('.', '', 1).isdigit():
                                season_totals[season] += float(row[month])
                                season_counts[season] += 1

    averages = {season: season_totals[season] / season_counts[season] for season in SEASONS}
    with open("average_temp.txt", "w") as outfile:
        for season, avg_temp in averages.items():
            outfile.write(f"{season}: {avg_temp:.2f}\n")

def find_largest_temp_range_station():
    station_ranges = {}

    for file in os.listdir(DATA_DIR):
        if file.endswith(".csv"):
            with open(os.path.join(DATA_DIR, file), mode="r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    temperatures = [float(row[month]) for month in row if month not in ["STATION_NAME", "STN_ID", "LAT", "LON"] and row[month] and row[month].replace('.', '', 1).isdigit()]
                    temp_range = max(temperatures) - min(temperatures)
                    station_ranges[row["STATION_NAME"]] = max(station_ranges.get(row["STATION_NAME"], 0), temp_range)

    max_range = max(station_ranges.values())
    largest_range_stations = [station for station, temp_range in station_ranges.items() if temp_range == max_range]

    with open("largest_temp_range_station.txt", "w") as outfile:
        outfile.write("\n".join(largest_range_stations))

def find_warmest_and_coolest_stations():
    station_avg_temps = defaultdict(list)

    for file in os.listdir(DATA_DIR):
        if file.endswith(".csv"):
            with open(os.path.join(DATA_DIR, file), mode="r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    temperatures = [float(row[month]) for month in row if month not in ["STATION_NAME", "STN_ID", "LAT", "LON"] and row[month] and row[month].replace('.', '', 1).isdigit()]
                    station_avg_temps[row["STATION_NAME"]].extend(temperatures)

    station_avg_temps = {station: sum(temps) / len(temps) for station, temps in station_avg_temps.items()}
    max_avg_temp = max(station_avg_temps.values())
    min_avg_temp = min(station_avg_temps.values())

    warmest_stations = [station for station, avg_temp in station_avg_temps.items() if avg_temp == max_avg_temp]
    coolest_stations = [station for station, avg_temp in station_avg_temps.items() if avg_temp == min_avg_temp]

    with open("warmest_and_coolest_station.txt", "w") as outfile:
        outfile.write("Warmest Stations:\n")
        outfile.write("\n".join(warmest_stations) + "\n")
        outfile.write("Coolest Stations:\n")
        outfile.write("\n".join(coolest_stations))

if __name__ == "__main__":
    calculate_average_temperatures()
    find_largest_temp_range_station()
    find_warmest_and_coolest_stations()
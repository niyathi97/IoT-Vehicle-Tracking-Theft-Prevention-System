import random
import time
import pandas as pd
from datetime import datetime
import os

# Safe zone (base location)
BASE_LAT = 17.3850
BASE_LON = 78.4867

# Create CSV if not exists
file_path = "../data/location_history.csv"

if not os.path.exists(file_path):
    df = pd.DataFrame(columns=[
        "Timestamp",
        "Latitude",
        "Longitude",
        "Status",
        "Google_Maps"
    ])
    df.to_csv(file_path, index=False)

while True:

    # Simulate movement
    lat = BASE_LAT + random.uniform(-0.003, 0.003)
    lon = BASE_LON + random.uniform(-0.003, 0.003)

    # Geofence check
    if abs(lat - BASE_LAT) > 0.002 or abs(lon - BASE_LON) > 0.002:
        status = "THEFT ALERT 🚨"
    else:
        status = "SAFE ✅"

    # Google Maps link
    maps = f"https://www.google.com/maps?q={lat},{lon}"

    print("\n===== Vehicle Tracking System =====")
    print(f"Latitude  : {lat:.6f}")
    print(f"Longitude : {lon:.6f}")
    print(f"Status    : {status}")
    print(f"Map Link  : {maps}")

    # Save data
    data = {
        "Timestamp": datetime.now(),
        "Latitude": lat,
        "Longitude": lon,
        "Status": status,
        "Google_Maps": maps
    }

    pd.DataFrame([data]).to_csv(
        file_path,
        mode="a",
        header=False,
        index=False
    )

    time.sleep(5)
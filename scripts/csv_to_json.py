import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # Adjust as needed

orders = []
csv_path = ROOT / 'data' / 'orders.csv'
with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['checked_in'] = False  # Add checked_in field to each order
        orders.append(row)

with open(ROOT / 'data' / 'orders.json', 'w') as jsonfile:
    json.dump(orders, jsonfile)
import csv
import json
import os

orders = []
csv_path = os.path.join(os.path.dirname(__file__), '../data/orders.csv')
with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        orders.append(row)

with open('orders.json', 'w') as jsonfile:
    json.dump(orders, jsonfile)
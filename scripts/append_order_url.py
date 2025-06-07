import csv
import os

GITHUB_PAGES_URL = "https://edaine.github.io/disco-order-tracker"

input_csv = os.path.join(os.path.dirname(__file__), '../data/orders.csv')
with open(input_csv, newline='') as infile:
    reader = list(csv.DictReader(infile))
    fieldnames = reader[0].keys()
    if 'order_url' not in fieldnames:
        fieldnames = list(fieldnames) + ['order_url']

output_csv = os.path.join(os.path.dirname(__file__), '../data/orders_with_url.csv')
with open(output_csv, 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        row['order_url'] = f"{GITHUB_PAGES_URL}/order-summary?orderId={row['orderId']}"
        writer.writerow(row)
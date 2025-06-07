import base64
import os
from io import BytesIO
from pathlib import Path

import pandas as pd
import qrcode
from jinja2 import Template
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent.parent  # Adjust as needed

# Ensure output folders exist
os.makedirs(ROOT / 'html/passes', exist_ok=True)
os.makedirs(ROOT / 'passes/pdf', exist_ok=True)

# Load your CSV
df = pd.read_csv(ROOT / 'data/orders_with_url.csv')

# Load HTML template
with open(ROOT / 'html/templates/passes.html') as f:
    template = Template(f.read())

# Group by orderId to get one pass per parent/order
for order_id, group in df.groupby('orderId'):
    parent_name = group.iloc[0]['parent_name']
    order_url = group.iloc[0]['order_url']

    # Generate QR code as base64
    qr = qrcode.make(order_url)
    buffered = BytesIO()
    qr.save(buffered, format="PNG")
    qr_base64 = base64.b64encode(buffered.getvalue()).decode()

    # Render HTML
    html = template.render(
        orderId=order_id,
        parent_name=parent_name,
        order_url=order_url,
        qr_base64=qr_base64
    )

    # Save HTML file
    html_path = f'html/passes/order_{order_id}.html'
    with open(html_path, 'w') as out:
        out.write(html)

    # Convert HTML to PDF
    pdf_path = f'passes/pdf/order_{order_id}.pdf'
    HTML(string=html).write_pdf(pdf_path)
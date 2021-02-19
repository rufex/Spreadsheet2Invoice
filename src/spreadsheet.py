import pathlib
import pandas as pd

from .config import root_path, invoice_dictio
from .components import client_info, invoice_info, add_product

# Paths
spreadheet_path = root_path.joinpath('spreadsheet/template.xlsx')

# Pandas DataFrame with all the invoices
invoices_df = pd.read_excel(spreadheet_path, sheet_name='Invoices')

def get_last_invoice_details():
    """Get the last invoice in the spreadsheet."""
    last_row = invoices_df.iloc[-1]
    # Client
    client_info(last_row['Client Name'],last_row['Client Address'],last_row['Client ZIP, City, Country'],last_row['Client VAT'])
    # Invoice Information
    invoice_info(last_row['Invoice Date'],last_row['Invoice Number'])
    # Product
    add_product(last_row['Product Description'],last_row['Product Unit Price'],last_row['Product Units'])
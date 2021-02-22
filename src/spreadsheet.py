import pathlib
import pandas as pd

from .config import root_path, invoice_dictio
from .components import client_info, invoice_info, add_product

# Paths
spreadsheet_path = root_path.joinpath('spreadsheet', 'template.xlsx')

# Pandas DataFrame with all the invoices
invoices_df = pd.read_excel(spreadsheet_path, sheet_name='Invoices')
# Rename DF columns names (position in the spreadsheet is important!)
invoices_df = invoices_df.rename(columns={
    invoices_df.columns[0]: 'invoice_number', 
    invoices_df.columns[1]: 'invoice_date', 
    invoices_df.columns[2]: 'client_name', 
    invoices_df.columns[3]: 'client_address', 
    invoices_df.columns[4]: 'client_city', 
    invoices_df.columns[5]: 'client_vat', 
    invoices_df.columns[6]: 'product_description', 
    invoices_df.columns[7]: 'product_units_amount', 
    invoices_df.columns[8]: 'product_unit_price'
    })

def get_invoice_details(invoice_nr = None):
    """Get the specific invoice in the spreadsheet.
    If no specific invoice nr is passed, the last one is retrieved.
    """
    if invoice_nr != None:
        try:
            invoice_indexes = invoices_df.index[invoices_df['invoice_number'] == invoice_nr]
        except:
            print(f"The invoice nr. '{invoice_nr}' was not founded in the spreadsheet.")
    else:
        try:
            # Invoice Nr. stored in the last row
            last_row = invoices_df.iloc[-1]
            last_row_invoice_nr = last_row['invoice_number']
            invoice_indexes = invoices_df.index[invoices_df['invoice_number'] == last_row_invoice_nr]
        except:
            print(f"The invoice nr. stored in the last row of the spreadsheet is invalid or can't be reached.")
    
    # First Row: Client and Invoice Information
    invoice_row = invoices_df.iloc[invoice_indexes[0]]
    client_info(invoice_row['client_name'],invoice_row['client_address'],invoice_row['client_city'],invoice_row['client_vat'])
    invoice_info(invoice_row['invoice_date'],invoice_row['invoice_number'])

    # Every Row: Products Information
    for i in invoice_indexes:
        invoice_row = invoices_df.iloc[i]
        add_product(invoice_row['product_description'],invoice_row['product_unit_price'],invoice_row['product_units_amount'])
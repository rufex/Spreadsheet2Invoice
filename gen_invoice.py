import sys

from src.config import root_path, config_yaml, invoice_dictio
from src.components import seller_info, generate_pdf, output_name_invoice_number
from src.spreadsheet import get_invoice_details

# Load Seller Information from YAML file
seller_info(config_yaml['SellerInfo']['Name'],config_yaml['SellerInfo']['Address'],config_yaml['SellerInfo']['City'],config_yaml['SellerInfo']['VAT'],config_yaml['SellerInfo']['IBAN'])

# CLI arguments
if len(sys.argv) > 1:
    cli_args_invoice_nr = sys.argv[1:]
    for cli_arg_invoice_nr in cli_args_invoice_nr:
        # Invoice data from Spreadsheet
        get_invoice_details(cli_arg_invoice_nr)
        # Use the invoice number as the PDF export name
        invoice_nr_path = output_name_invoice_number()
        # Generate PDF
        generate_pdf(invoice_nr_path)
else:
    # Invoice data from Spreadsheet
    get_invoice_details()
    # Use the invoice number as the PDF export name
    invoice_nr_path = output_name_invoice_number()
    # Generate PDF
    generate_pdf(invoice_nr_path)
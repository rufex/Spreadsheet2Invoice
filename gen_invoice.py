from src.config import root_path, output_path, config_yaml, invoice_dictio
from src.components import seller_info, generate_pdf
from src.spreadsheet import get_last_invoice_details

# Load Seller Information from YAML file
seller_info(config_yaml['SellerInfo']['Name'],config_yaml['SellerInfo']['Address'],config_yaml['SellerInfo']['City'],config_yaml['SellerInfo']['VAT'],config_yaml['SellerInfo']['IBAN'])
   
# Invoice data from Spreadsheet
get_last_invoice_details()

# Generate PDF
generate_pdf(output_path)
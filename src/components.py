import pathlib

from weasyprint import HTML, CSS
from jinja2 import Environment, FileSystemLoader

# Paths
path = pathlib.Path(__file__).parent.parent.absolute()
template_path = path.joinpath('invoice_template')
css_path = template_path.joinpath('invoice_public.css')
output_path = str(path.joinpath('output/example.pdf'))

# Create Environment where we can load the template
env = Environment(loader=FileSystemLoader(template_path))
template = env.get_template('invoice_public.html')

# Variables to include in our invoice
invoice_dictio = {
    'products': [],
    'vat_rate': 0.21,
}

def seller_info(name, address, city, vat, iban):
    invoice_dictio['seller_name'] = name
    invoice_dictio['seller_address'] = address
    invoice_dictio['seller_city'] = city
    invoice_dictio['seller_vat'] = vat
    invoice_dictio['seller_iban'] = iban

def client_info(name, address, city, vat):
    invoice_dictio['client_name'] = name
    invoice_dictio['client_address'] = address
    invoice_dictio['client_city'] = city
    invoice_dictio['client_vat'] = vat

def invoice_info(date, number):
    invoice_dictio['invoice_date'] = date
    invoice_dictio['invoice_number'] = number

def add_product(description, unit_price, unit_amount):
    product_total = round(unit_price*unit_amount, 2)
    invoice_dictio['products'].append((description,unit_price,unit_amount, product_total))

def calc_subtotal():
    subtotal = 0
    for product in invoice_dictio['products']:
        subtotal += product[3]
    invoice_dictio['subtotal'] = subtotal

def set_vat_rate(rate = 0.21):
    if rate >= 1:
        rate = round(rate/100,2)
    invoice_dictio['vat_rate'] = rate

def calc_vat():
    invoice_dictio['vat_amount'] = round(invoice_dictio['subtotal']*invoice_dictio['vat_rate'], 2)

def calc_total():
    invoice_dictio['total'] = invoice_dictio['subtotal']-invoice_dictio['vat_rate']
    
def generate_pdf(output_path):
    # Calculate subtotal, vat, total
    calc_subtotal()
    calc_vat()
    calc_total()
    # Render variables into the template
    invoice_obj = template.render(invoice_dictio)
    # Create HTML and CSS objects
    html = HTML(string=invoice_obj)
    css = CSS(css_path)
    # SAVE PDF FILE
    html.write_pdf(output_path, stylesheets=[css])
    # Clean invoice_dictio
    #invoice_dictio =  {}
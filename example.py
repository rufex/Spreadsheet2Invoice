from src.components import *

root_path = pathlib.Path(__file__).parent.absolute()
example_output_path = str(root_path.joinpath('output', 'example.pdf'))

seller_info('Carlos Seller', 'Bolivia Av. 150', 'Buenos Aires, ARG', '35120131', 'AR1230193910293')
client_info('Stuart Client','Calvin St. 123', 'Dublin, IRL', '11001100')
invoice_info('01-02-2021', '2021-00235')
add_product('First product listed', 500, 25)
add_product('Second product', 21, 12)
set_vat_rate(10)
generate_pdf(example_output_path)
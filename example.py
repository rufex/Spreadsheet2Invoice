from src.components import *


seller_info('Carlos', 'Bolivia 150', 'Buenos Aires, ARG', '35120131', 'AR1230193910293')
client_info('Stuart','Calvin St 123', 'Dublin, IRL', '11001100')
invoice_info('01-02-2021', '2021-00235')
add_product('First product listed', 500, 25)
add_product('Second product', 21, 12)
set_vat_rate(10)
generate_pdf(output_path)
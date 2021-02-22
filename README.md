# Spreadsheet2Invoice

> **NOTE: Work in progress**

## Goal

Be able to keep track of all your invoices in a simple spreadsheet. And generate any invoices you need to deliver taking the information from that same spreadsheet.

## Before you start

- Clone the repository
- Install the requirements

## Generate an invoice

There is an example spreadsheet stored in the directory called ***spreadsheet***, you can modify that one to make a quick test export.

Then, run the program:

```bash
python3 gen_invoice.py
```

This will look for the information stored in the latest row of the spreadsheet and the generated invoice is going to be stored by default in the ***output*** directory.

### Choose which invoice to export

You can also select which invoice you want to generate by passing it's number as an argument while running the script (only one invoice can be generated at the moment). Like this:

```bash
python3 gen_invoice.py 2021-000002
```

### Multiple products in the same invoice

To include several products in the same invoice, you have to include each product in a separate row in the spreadsheet. To be generated in the same invoice they just need to have the same invoice number assigned. The client information and the invoice date is going to be taken from the first product listed, so there is no need to define them again for the following products. You can have a look at the example provided in the *template.xlsx* file

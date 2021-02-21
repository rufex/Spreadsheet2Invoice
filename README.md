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

The generated invoice is going to be stored by default in the ***output*** directory.

> At the moment, it will generate an invoice with the information stored in the latest row of the spreadsheet.

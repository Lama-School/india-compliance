from india_compliance.gst_india.constants import STATE_NUMBERS

# TODO: Imporve variable naming

state_options = "\n" + "\n".join(STATE_NUMBERS)

hsn_sac_field = {
    "fieldname": "gst_hsn_code",
    "label": "HSN/SAC",
    "fieldtype": "Data",
    "fetch_from": "item_code.gst_hsn_code",
    "insert_after": "description",
    "allow_on_submit": 1,
    "print_hide": 1,
    "fetch_if_empty": 1,
}
nil_rated_exempt = {
    "fieldname": "is_nil_exempt",
    "label": "Is Nil Rated or Exempted",
    "fieldtype": "Check",
    "fetch_from": "item_code.is_nil_exempt",
    "insert_after": "gst_hsn_code",
    "print_hide": 1,
}
is_non_gst = {
    "fieldname": "is_non_gst",
    "label": "Is Non GST",
    "fieldtype": "Check",
    "fetch_from": "item_code.is_non_gst",
    "insert_after": "is_nil_exempt",
    "print_hide": 1,
}
taxable_value = {
    "fieldname": "taxable_value",
    "label": "Taxable Value",
    "fieldtype": "Currency",
    "insert_after": "base_net_amount",
    "hidden": 1,
    "options": "Company:company:default_currency",
    "print_hide": 1,
}

purchase_invoice_gst_category = [
    {
        "fieldname": "gst_section",
        "label": "GST Details",
        "fieldtype": "Section Break",
        "insert_after": "language",
        "print_hide": 1,
        "collapsible": 1,
    },
    {
        "fieldname": "gst_category",
        "label": "GST Category",
        "fieldtype": "Select",
        "insert_after": "gst_section",
        "print_hide": 1,
        "options": (
            "\nRegistered Regular\nRegistered"
            " Composition\nUnregistered\nSEZ\nOverseas\nUIN Holders"
        ),
        "fetch_from": "supplier.gst_category",
    },
    {
        "fieldname": "export_type",
        "label": "Export Type",
        "fieldtype": "Select",
        "insert_after": "gst_category",
        "print_hide": 1,
        "depends_on": 'eval:in_list(["SEZ", "Overseas"], doc.gst_category)',
        "options": "\nWith Payment of Tax\nWithout Payment of Tax",
        "fetch_from": "supplier.export_type",
        "fetch_if_empty": 1,
    },
]

sales_invoice_gst_category = [
    {
        "fieldname": "gst_section",
        "label": "GST Details",
        "fieldtype": "Section Break",
        "insert_after": "language",
        "print_hide": 1,
        "collapsible": 1,
    },
    {
        "fieldname": "gst_category",
        "label": "GST Category",
        "fieldtype": "Select",
        "insert_after": "gst_section",
        "print_hide": 1,
        "options": (
            "\nRegistered Regular\nRegistered"
            " Composition\nUnregistered\nSEZ\nOverseas\nDeemed Export\nUIN Holders"
        ),
        "fetch_from": "customer.gst_category",
        "length": 25,
    },
    {
        "fieldname": "export_type",
        "label": "Export Type",
        "fieldtype": "Select",
        "insert_after": "gst_category",
        "print_hide": 1,
        "depends_on": (
            'eval:in_list(["SEZ", "Overseas", "Deemed Export"], doc.gst_category)'
        ),
        "options": "\nWith Payment of Tax\nWithout Payment of Tax",
        "fetch_from": "customer.export_type",
        "fetch_if_empty": 1,
        "length": 25,
    },
]

delivery_note_gst_category = [
    {
        "fieldname": "gst_category",
        "label": "GST Category",
        "fieldtype": "Select",
        "insert_after": "gst_vehicle_type",
        "print_hide": 1,
        "options": (
            "\nRegistered Regular\nRegistered"
            " Composition\nUnregistered\nSEZ\nOverseas\nDeemed Export\nUIN Holders"
        ),
        "fetch_from": "customer.gst_category",
    },
]

invoice_gst_fields = [
    {
        "fieldname": "invoice_copy",
        "label": "Invoice Copy",
        "length": 30,
        "fieldtype": "Select",
        "insert_after": "export_type",
        "print_hide": 1,
        "allow_on_submit": 1,
        "options": (
            "Original for Recipient\nDuplicate for Transporter\nDuplicate for"
            " Supplier\nTriplicate for Supplier"
        ),
    },
    {
        "fieldname": "reverse_charge",
        "label": "Reverse Charge",
        "length": 2,
        "fieldtype": "Select",
        "insert_after": "invoice_copy",
        "print_hide": 1,
        "options": "Y\nN",
        "default": "N",
    },
    {
        "fieldname": "ecommerce_gstin",
        "label": "E-commerce GSTIN",
        "length": 15,
        "fieldtype": "Data",
        "insert_after": "export_type",
        "print_hide": 1,
    },
    {
        "fieldname": "gst_col_break",
        "fieldtype": "Column Break",
        "insert_after": "ecommerce_gstin",
    },
    {
        "fieldname": "reason_for_issuing_document",
        "label": "Reason For Issuing document",
        "fieldtype": "Select",
        "insert_after": "gst_col_break",
        "print_hide": 1,
        "depends_on": "eval:doc.is_return == 1",
        "length": 45,
        "options": (
            "\n01-Sales Return\n02-Post Sale Discount\n03-Deficiency in"
            " services\n04-Correction in Invoice\n05-Change in POS\n06-Finalization of"
            " Provisional assessment\n07-Others"
        ),
    },
]

purchase_invoice_gst_fields = [
    {
        "fieldname": "supplier_gstin",
        "label": "Supplier GSTIN",
        "fieldtype": "Data",
        "insert_after": "supplier_address",
        "fetch_from": "supplier_address.gstin",
        "print_hide": 1,
        "read_only": 1,
    },
    {
        "fieldname": "company_gstin",
        "label": "Company GSTIN",
        "fieldtype": "Data",
        "insert_after": "shipping_address_display",
        "fetch_from": "shipping_address.gstin",
        "print_hide": 1,
        "read_only": 1,
    },
    {
        "fieldname": "place_of_supply",
        "label": "Place of Supply",
        "fieldtype": "Data",
        "insert_after": "shipping_address",
        "print_hide": 1,
        "read_only": 1,
    },
]

purchase_invoice_itc_fields = [
    {
        "fieldname": "eligibility_for_itc",
        "label": "Eligibility For ITC",
        "fieldtype": "Select",
        "insert_after": "reason_for_issuing_document",
        "print_hide": 1,
        "options": (
            "Input Service Distributor\nImport Of Service\nImport Of Capital Goods\nITC"
            " on Reverse Charge\nIneligible As Per Section 17(5)\nIneligible"
            " Others\nAll Other ITC"
        ),
        "default": "All Other ITC",
    },
    {
        "fieldname": "itc_integrated_tax",
        "label": "Availed ITC Integrated Tax",
        "fieldtype": "Currency",
        "insert_after": "eligibility_for_itc",
        "options": "Company:company:default_currency",
        "print_hide": 1,
    },
    {
        "fieldname": "itc_central_tax",
        "label": "Availed ITC Central Tax",
        "fieldtype": "Currency",
        "insert_after": "itc_integrated_tax",
        "options": "Company:company:default_currency",
        "print_hide": 1,
    },
    {
        "fieldname": "itc_state_tax",
        "label": "Availed ITC State/UT Tax",
        "fieldtype": "Currency",
        "insert_after": "itc_central_tax",
        "options": "Company:company:default_currency",
        "print_hide": 1,
    },
    {
        "fieldname": "itc_cess_amount",
        "label": "Availed ITC Cess",
        "fieldtype": "Currency",
        "insert_after": "itc_state_tax",
        "options": "Company:company:default_currency",
        "print_hide": 1,
    },
]

sales_invoice_gst_fields = [
    {
        "fieldname": "billing_address_gstin",
        "label": "Billing Address GSTIN",
        "fieldtype": "Data",
        "insert_after": "customer_address",
        "read_only": 1,
        "fetch_from": "customer_address.gstin",
        "print_hide": 1,
        "length": 15,
    },
    {
        "fieldname": "customer_gstin",
        "label": "Customer GSTIN",
        "fieldtype": "Data",
        "insert_after": "shipping_address_name",
        "fetch_from": "shipping_address_name.gstin",
        "print_hide": 1,
        "length": 15,
    },
    {
        "fieldname": "place_of_supply",
        "label": "Place of Supply",
        "fieldtype": "Data",
        "insert_after": "customer_gstin",
        "print_hide": 1,
        "read_only": 1,
        "length": 50,
    },
    {
        "fieldname": "company_gstin",
        "label": "Company GSTIN",
        "fieldtype": "Data",
        "insert_after": "company_address",
        "fetch_from": "company_address.gstin",
        "print_hide": 1,
        "read_only": 1,
        "length": 15,
    },
]

sales_invoice_shipping_fields = [
    {
        "fieldname": "port_code",
        "label": "Port Code",
        "fieldtype": "Data",
        "insert_after": "reason_for_issuing_document",
        "print_hide": 1,
        "depends_on": "eval:doc.gst_category == 'Overseas' ",
        "length": 15,
    },
    {
        "fieldname": "shipping_bill_number",
        "label": " Shipping Bill Number",
        "fieldtype": "Data",
        "insert_after": "port_code",
        "print_hide": 1,
        "depends_on": "eval:doc.gst_category == 'Overseas' ",
        "length": 50,
    },
    {
        "fieldname": "shipping_bill_date",
        "label": "Shipping Bill Date",
        "fieldtype": "Date",
        "insert_after": "shipping_bill_number",
        "print_hide": 1,
        "depends_on": "eval:doc.gst_category == 'Overseas' ",
    },
]

journal_entry_fields = [
    {
        "fieldname": "reversal_type",
        "label": "Reversal Type",
        "fieldtype": "Select",
        "insert_after": "voucher_type",
        "print_hide": 1,
        "options": "As per rules 42 & 43 of CGST Rules\nOthers",
        "depends_on": "eval:doc.voucher_type == 'Reversal Of ITC'",
        "mandatory_depends_on": "eval:doc.voucher_type == 'Reversal Of ITC'",
    },
    {
        "fieldname": "company_address",
        "label": "Company Address",
        "fieldtype": "Link",
        "options": "Address",
        "insert_after": "reversal_type",
        "print_hide": 1,
        "depends_on": "eval:doc.voucher_type == 'Reversal Of ITC'",
        "mandatory_depends_on": "eval:doc.voucher_type == 'Reversal Of ITC'",
    },
    {
        "fieldname": "company_gstin",
        "label": "Company GSTIN",
        "fieldtype": "Data",
        "read_only": 1,
        "insert_after": "company_address",
        "print_hide": 1,
        "fetch_from": "company_address.gstin",
        "depends_on": "eval:doc.voucher_type == 'Reversal Of ITC'",
        "mandatory_depends_on": "eval:doc.voucher_type=='Reversal Of ITC'",
    },
]

inter_state_gst_field = [
    {
        "fieldname": "is_inter_state",
        "label": "Is Inter State",
        "fieldtype": "Check",
        "insert_after": "disabled",
        "print_hide": 1,
    },
    {
        "fieldname": "is_reverse_charge",
        "label": "Is Reverse Charge",
        "fieldtype": "Check",
        "insert_after": "is_inter_state",
        "print_hide": 1,
    },
    {
        "fieldname": "tax_category_column_break",
        "fieldtype": "Column Break",
        "insert_after": "is_reverse_charge",
    },
    {
        "fieldname": "gst_state",
        "label": "Source State",
        "fieldtype": "Select",
        "options": state_options,
        "insert_after": "company",
    },
]

payment_entry_fields = [
    {
        "fieldname": "gst_section",
        "label": "GST Details",
        "fieldtype": "Section Break",
        "insert_after": "deductions",
        "print_hide": 1,
        "collapsible": 1,
    },
    {
        "fieldname": "company_address",
        "label": "Company Address",
        "fieldtype": "Link",
        "insert_after": "gst_section",
        "print_hide": 1,
        "options": "Address",
    },
    {
        "fieldname": "company_gstin",
        "label": "Company GSTIN",
        "fieldtype": "Data",
        "insert_after": "company_address",
        "fetch_from": "company_address.gstin",
        "print_hide": 1,
        "read_only": 1,
    },
    {
        "fieldname": "place_of_supply",
        "label": "Place of Supply",
        "fieldtype": "Data",
        "insert_after": "company_gstin",
        "print_hide": 1,
        "read_only": 1,
    },
    {
        "fieldname": "gst_column_break",
        "fieldtype": "Column Break",
        "insert_after": "place_of_supply",
    },
    {
        "fieldname": "customer_address",
        "label": "Customer Address",
        "fieldtype": "Link",
        "insert_after": "gst_column_break",
        "print_hide": 1,
        "options": "Address",
        "depends_on": 'eval:doc.party_type == "Customer"',
    },
    {
        "fieldname": "customer_gstin",
        "label": "Customer GSTIN",
        "fieldtype": "Data",
        "insert_after": "customer_address",
        "fetch_from": "customer_address.gstin",
        "print_hide": 1,
        "read_only": 1,
    },
]

si_einvoice_fields = [
    {
        "fieldname": "irn",
        "label": "IRN",
        "fieldtype": "Data",
        "read_only": 1,
        "insert_after": "customer",
        "no_copy": 1,
        "print_hide": 1,
        "depends_on": (
            'eval:in_list(["Registered Regular", "SEZ", "Overseas", "Deemed Export"],'
            " doc.gst_category) && doc.irn_cancelled === 0"
        ),
    },
    {
        "fieldname": "irn_cancelled",
        "label": "IRN Cancelled",
        "fieldtype": "Check",
        "no_copy": 1,
        "print_hide": 1,
        "depends_on": "eval: doc.irn",
        "allow_on_submit": 1,
        "insert_after": "customer",
    },
    {
        "fieldname": "eway_bill_validity",
        "label": "e-Waybill Validity",
        "fieldtype": "Data",
        "no_copy": 1,
        "print_hide": 1,
        "depends_on": "ewaybill",
        "read_only": 1,
        "allow_on_submit": 1,
        "insert_after": "ewaybill",
    },
    {
        "fieldname": "eway_bill_cancelled",
        "label": "e-Waybill Cancelled",
        "fieldtype": "Check",
        "no_copy": 1,
        "print_hide": 1,
        "depends_on": "eval:(doc.eway_bill_cancelled === 1)",
        "read_only": 1,
        "allow_on_submit": 1,
        "insert_after": "customer",
    },
    {
        "fieldname": "einvoice_section",
        "label": "e-Invoice Fields",
        "fieldtype": "Section Break",
        "insert_after": "gst_vehicle_type",
        "print_hide": 1,
        "hidden": 1,
    },
    {
        "fieldname": "ack_no",
        "label": "Ack. No.",
        "fieldtype": "Data",
        "read_only": 1,
        "hidden": 1,
        "insert_after": "einvoice_section",
        "no_copy": 1,
        "print_hide": 1,
    },
    {
        "fieldname": "ack_date",
        "label": "Ack. Date",
        "fieldtype": "Data",
        "read_only": 1,
        "hidden": 1,
        "insert_after": "ack_no",
        "no_copy": 1,
        "print_hide": 1,
    },
    {
        "fieldname": "irn_cancel_date",
        "label": "Cancel Date",
        "fieldtype": "Data",
        "read_only": 1,
        "hidden": 1,
        "insert_after": "ack_date",
        "no_copy": 1,
        "print_hide": 1,
    },
    {
        "fieldname": "signed_einvoice",
        "label": "Signed e-Invoice",
        "fieldtype": "Code",
        "options": "JSON",
        "hidden": 1,
        "insert_after": "irn_cancel_date",
        "no_copy": 1,
        "print_hide": 1,
        "read_only": 1,
    },
    {
        "fieldname": "signed_qr_code",
        "label": "Signed QRCode",
        "fieldtype": "Code",
        "options": "JSON",
        "hidden": 1,
        "insert_after": "signed_einvoice",
        "no_copy": 1,
        "print_hide": 1,
        "read_only": 1,
    },
    {
        "fieldname": "qrcode_image",
        "label": "QRCode",
        "fieldtype": "Attach Image",
        "hidden": 1,
        "insert_after": "signed_qr_code",
        "no_copy": 1,
        "print_hide": 1,
        "read_only": 1,
    },
    {
        "fieldname": "einvoice_status",
        "label": "e-Invoice Status",
        "fieldtype": "Select",
        "insert_after": "qrcode_image",
        "options": "\nPending\nGenerated\nCancelled\nFailed",
        "default": None,
        "hidden": 1,
        "no_copy": 1,
        "print_hide": 1,
        "read_only": 1,
    },
    {
        "fieldname": "failure_description",
        "label": "e-Invoice Failure Description",
        "fieldtype": "Code",
        "options": "JSON",
        "hidden": 1,
        "insert_after": "einvoice_status",
        "no_copy": 1,
        "print_hide": 1,
        "read_only": 1,
    },
]

CUSTOM_FIELDS = {
    "Address": [
        {
            "fieldname": "gstin",
            "label": "Party GSTIN",
            "fieldtype": "Data",
            "insert_after": "fax",
        },
        {
            "fieldname": "gst_state",
            "label": "GST State",
            "fieldtype": "Select",
            "options": state_options,
            "insert_after": "gstin",
        },
        {
            "fieldname": "gst_state_number",
            "label": "GST State Number",
            "fieldtype": "Data",
            "insert_after": "gst_state",
            "read_only": 1,
        },
    ],
    "Purchase Invoice": purchase_invoice_gst_category
    + invoice_gst_fields
    + purchase_invoice_itc_fields
    + purchase_invoice_gst_fields,
    "Purchase Order": purchase_invoice_gst_fields,
    "Purchase Receipt": purchase_invoice_gst_fields,
    "Sales Invoice": sales_invoice_gst_category
    + invoice_gst_fields
    + sales_invoice_shipping_fields
    + sales_invoice_gst_fields
    + si_einvoice_fields,
    "POS Invoice": sales_invoice_gst_fields,
    "Delivery Note": sales_invoice_gst_fields
    + sales_invoice_shipping_fields
    + delivery_note_gst_category,
    "Payment Entry": payment_entry_fields,
    "Journal Entry": journal_entry_fields,
    "Sales Order": sales_invoice_gst_fields,
    "Tax Category": inter_state_gst_field,
    "Item": [
        {
            "fieldname": "gst_hsn_code",
            "label": "HSN/SAC",
            "fieldtype": "Link",
            "options": "GST HSN Code",
            "insert_after": "item_group",
        },
        {
            "fieldname": "is_nil_exempt",
            "label": "Is Nil Rated or Exempted",
            "fieldtype": "Check",
            "insert_after": "gst_hsn_code",
        },
        {
            "fieldname": "is_non_gst",
            "label": "Is Non GST ",
            "fieldtype": "Check",
            "insert_after": "is_nil_exempt",
        },
    ],
    "Quotation Item": [hsn_sac_field, nil_rated_exempt, is_non_gst],
    "Supplier Quotation Item": [hsn_sac_field, nil_rated_exempt, is_non_gst],
    "Sales Order Item": [hsn_sac_field, nil_rated_exempt, is_non_gst],
    "Delivery Note Item": [hsn_sac_field, nil_rated_exempt, is_non_gst],
    "Sales Invoice Item": [
        hsn_sac_field,
        nil_rated_exempt,
        is_non_gst,
        taxable_value,
    ],
    "POS Invoice Item": [
        hsn_sac_field,
        nil_rated_exempt,
        is_non_gst,
        taxable_value,
    ],
    "Purchase Order Item": [hsn_sac_field, nil_rated_exempt, is_non_gst],
    "Purchase Receipt Item": [hsn_sac_field, nil_rated_exempt, is_non_gst],
    "Purchase Invoice Item": [
        hsn_sac_field,
        nil_rated_exempt,
        is_non_gst,
        taxable_value,
    ],
    "Material Request Item": [hsn_sac_field, nil_rated_exempt, is_non_gst],
    "Supplier": [
        {
            "fieldname": "gst_transporter_id",
            "label": "GST Transporter ID",
            "fieldtype": "Data",
            "insert_after": "pan",
            "depends_on": "eval:doc.is_transporter",
        },
        {
            "fieldname": "gst_category",
            "label": "GST Category",
            "fieldtype": "Select",
            "insert_after": "gst_transporter_id",
            "options": (
                "Registered Regular\nRegistered"
                " Composition\nUnregistered\nSEZ\nOverseas\nUIN Holders"
            ),
            "default": "Unregistered",
        },
        {
            "fieldname": "export_type",
            "label": "Export Type",
            "fieldtype": "Select",
            "insert_after": "gst_category",
            "depends_on": 'eval:in_list(["SEZ", "Overseas"], doc.gst_category)',
            "options": "\nWith Payment of Tax\nWithout Payment of Tax",
            "mandatory_depends_on": (
                'eval:in_list(["SEZ", "Overseas"], doc.gst_category)'
            ),
        },
    ],
    "Customer": [
        {
            "fieldname": "gst_category",
            "label": "GST Category",
            "fieldtype": "Select",
            "insert_after": "pan",
            "options": (
                "Registered Regular\nRegistered"
                " Composition\nUnregistered\nSEZ\nOverseas\nDeemed Export\nUIN Holders"
            ),
            "default": "Unregistered",
        },
        {
            "fieldname": "export_type",
            "label": "Export Type",
            "fieldtype": "Select",
            "insert_after": "gst_category",
            "depends_on": (
                'eval:in_list(["SEZ", "Overseas", "Deemed Export"], doc.gst_category)'
            ),
            "options": "\nWith Payment of Tax\nWithout Payment of Tax",
            "mandatory_depends_on": (
                'eval:in_list(["SEZ", "Overseas", "Deemed Export"], doc.gst_category)'
            ),
        },
    ],
}

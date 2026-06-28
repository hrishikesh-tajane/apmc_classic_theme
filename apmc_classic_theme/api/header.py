import frappe

@frappe.whitelist(allow_guest=True)
def get_header_details():

    company = frappe.get_all(
        "Company",
        fields=["company_logo","company_name","address","phone_no","email"],
        limit=1
    )

    return company[0] if company else {}
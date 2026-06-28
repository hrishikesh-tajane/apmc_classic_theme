import frappe

@frappe.whitelist(allow_guest=True)
def get_contact_details():

    company = frappe.get_all(
        "Company",
        fields=["company_name","address","phone_no","email","location_url"],
        limit=1
    )

    return company[0] if company else {}
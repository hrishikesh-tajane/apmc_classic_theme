import frappe

def get_context(context):

    about = frappe.get_doc("About Us", "About Us")

    context.about = about

    return context
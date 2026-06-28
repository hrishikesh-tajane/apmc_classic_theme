import frappe

def get_context(context):
    context.no_cache = 1

    officers = frappe.get_all(
        "Officers And Staff",
        fields=[
            "name1",
            "designation",
            "upload_profile_picture",
            "order"
        ],
        order_by="`order` asc"
    )
    context.top_members = [
    officer for officer in officers
    if officer.get("order") in [1, 2]
    ]
    
    context.other_members = [
    officer for officer in officers
    if officer.get("order") not in [1, 2]
    ]
    return context

import frappe
def get_context(context):

    directors = frappe.get_all(
        "Board of Directors",
        fields=["name1", "designation", "upload_profile_picture","order"],
        order_by="`order` asc"
    )
    context.top_members = [
    director for director in directors
    if director.get("order") in [1, 2]
    ]
    
    context.other_members = [
    director for director in directors
    if director.get("order") not in [1, 2]
    ]
    return context
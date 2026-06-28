import frappe

@frappe.whitelist(allow_guest=True)
def get_auction_information():

    data = frappe.get_all(
        "Auction Information",
        fields=[
            "department",
            "auction_info",
            "date",
            "note"
        ],
        order_by="date desc"
    )

    return data
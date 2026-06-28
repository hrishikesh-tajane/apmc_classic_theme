import frappe

@frappe.whitelist(allow_guest=True)
def get_homepage_carousel():
    return frappe.get_all(
        "Homepage Carousel",
        fields=[
            "caption_heading",
            "caption",
            "image"
        ],
        order_by="creation desc"
    )
    
    
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
        order_by="date desc",limit=3
    )
    return data



@frappe.whitelist(allow_guest=True)
def get_gallery_images():
    return frappe.get_all(
        "gallery image",
        filters={"published": 1},
        fields=["title", "image"],
        order_by="creation desc",
        limit=6
    )
    

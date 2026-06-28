import frappe

@frappe.whitelist(allow_guest=True)
def get_gallery_images(page=1, page_length=8):

    page = int(page)
    page_length = int(page_length)

    start = (page - 1) * page_length

    images = frappe.get_all(
        "gallery image",
        fields=["image", "title"],
        start=start,
        page_length=page_length,
        order_by="creation desc"
    )

    total = frappe.db.count("gallery image")

    return {
        "images": images,
        "total": total,
        "page": page,
        "page_length": page_length
    }
import frappe
from frappe.utils import pretty_date

@frappe.whitelist(allow_guest=True)
def get_news_categories():

    return frappe.get_all(
        "Blog Category",
        fields=["title"],
        order_by="title asc"
    )
@frappe.whitelist(allow_guest=True)
def get_news_list():

    news_list = frappe.get_all(
        "Blog Post",
        filters={"published": 1},
        fields=[
            "title",
            "blog_category",
            "blogger",
            "route",
            "meta_image",
            "blog_intro",
            "content",
            "published_on",
            "creation"
        ],
        order_by="published_on desc"
    )

    for news in news_list:
        news["time_ago"] = pretty_date(news["creation"])

    return news_list


@frappe.whitelist(allow_guest=True)
def get_news_detail(route):

    news = frappe.get_value(
        "Blog Post",
        
        {"route": route},
        [
            "title",
            "blog_category",
            "blogger",
            "route",
            "meta_image",
            "blog_intro",
            "content",
            "published_on",
            "creation"
        ],
        as_dict=True
    )
    if news:
        news["time_ago"] = pretty_date(news.get("creation"))

    return news
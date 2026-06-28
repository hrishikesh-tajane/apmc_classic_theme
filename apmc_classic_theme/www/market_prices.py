from frappe.desk.query_report import run


def get_context(context):

    report = run(
        report_name="Market Price Report",
        filters={}
    )

    context.market_prices = report.get("result", [])
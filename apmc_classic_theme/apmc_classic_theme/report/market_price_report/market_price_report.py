def execute(filters=None):

    columns = [
        {
            "label": "Date",
            "fieldname": "date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": "Commodity",
            "fieldname": "commodity",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Unit",
            "fieldname": "unit",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Arrival",
            "fieldname": "arrival",
            "fieldtype": "Float",
            "width": 100
        },
        {
            "label": "Min Price",
            "fieldname": "min_price",
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "label": "Max Price",
            "fieldname": "max_price",
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "label": "Avg Price",
            "fieldname": "avg_price",
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "label": "Market",
            "fieldname": "market",
            "fieldtype": "Data",
            "width": 150
        }
    ]

    data = [
        {
            "date": "2026-06-11",
            "commodity": "काकडी",
            "unit": "गोणी",
            "arrival": 8,
            "min_price": 12,
            "max_price": 40,
            "avg_price": 27,
            "market": "चाकण"
        },
        {
            "date": "2026-06-10",
            "commodity": "कांदा",
            "unit": "गोणी",
            "arrival": 20,
            "min_price": 50,
            "max_price": 70,
            "avg_price": 60,
            "market": "पुणे"
        },
        {
            "date": "2026-06-12",
            "commodity": "कांदा",
            "unit": "गोणी",
            "arrival": 20,
            "min_price": 50,
            "max_price": 70,
            "avg_price": 60,
            "market": "पुणे"
        },
        {
            "date": "2026-06-12",
            "commodity": "काकडी",
            "unit": "गोणी",
            "arrival": 20,
            "min_price": 50,
            "max_price": 70,
            "avg_price": 60,
            "market": "पुणे"
        },
        {
            "date": "2026-06-10",
            "commodity": "कांदा",
            "unit": "गोणी",
            "arrival": 20,
            "min_price": 50,
            "max_price": 70,
            "avg_price": 60,
            "market": "पुणे"
        }
    ]

    return columns, data
document.addEventListener("DOMContentLoaded", function () {

    const marketFilter = document.getElementById("marketFilter");
    const commodityFilter = document.getElementById("commodityFilter");
    const fromDate = document.getElementById("fromDate");
    const toDate = document.getElementById("toDate");
    const searchBtn = document.getElementById("searchBtn");

    function filterTable() {

        const selectedMarket = marketFilter.value.trim();
        const selectedCommodity = commodityFilter.value.trim();
        const selectedFromDate = fromDate.value;
        const selectedToDate = toDate.value;

        const rows = document.querySelectorAll("tbody tr");

        rows.forEach(row => {

            const market = row.dataset.market;
            const commodity = row.dataset.commodity;
            const rowDate = row.dataset.date;

            // Market Filter
            const marketMatch =
                selectedMarket === "" ||
                market === selectedMarket;

            // Commodity Filter
            const commodityMatch =
                selectedCommodity === "" ||
                commodity === selectedCommodity;

            // Date Filter
            let dateMatch = true;

            if (selectedFromDate) {
                dateMatch =
                    dateMatch &&
                    rowDate >= selectedFromDate;
            }

            if (selectedToDate) {
                dateMatch =
                    dateMatch &&
                    rowDate <= selectedToDate;
            }

            row.style.display =
                (marketMatch && commodityMatch && dateMatch)
                ? ""
                : "none";

        });
    }

    searchBtn.addEventListener("click", filterTable);

});
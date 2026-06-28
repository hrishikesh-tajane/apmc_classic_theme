const filterButtons = document.querySelectorAll(".filter-btn");
const cards = document.querySelectorAll(".news-item");
const noDataMessage = document.getElementById("noDataMessage");

filterButtons.forEach(button => {

    button.addEventListener("click", function () {

        filterButtons.forEach(btn =>
            btn.classList.remove("active")
        );

        this.classList.add("active");

        const selected = this.dataset.category;

        let visibleCount = 0;

        cards.forEach(card => {

            if (
                selected === "all" ||
                card.dataset.category === selected
            ) {
                card.style.display = "block";
                visibleCount++;
            } else {
                card.style.display = "none";
            }

        });

        noDataMessage.style.display =
            visibleCount === 0 ? "block" : "none";
    });

});
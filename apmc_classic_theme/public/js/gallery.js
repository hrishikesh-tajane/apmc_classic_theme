let currentPage = 1;
const pageLength = 8;
let totalImages = 0;

loadImages(1);

function loadImages(page) {

    fetch(
        `/api/method/apmc_classic_theme.api.gallery.get_gallery_images?page=${page}&page_length=${pageLength}`
    )
        .then(response => response.json())
        .then(data => {

            const result = data.message;

            totalImages = result.total;

            

            let html = "";

            result.images.forEach(img => {

                html += `
                <div class="col-6 col-md-3">
                    <img
                        src="${img.image}"
                        class="img-fluid gallery-img"
                        data-src="${img.image}"
                    >
                </div>
            `;
            });

            document.getElementById(
                "gallery-container"
            ).innerHTML = html;


            renderPagination(
                result.total,
                result.page_length,
                result.page
            );

            bindGalleryEvents();

        })
        .catch(error => {
            console.error(error);
        });
}

function renderPagination(
    total,
    pageLength,
    currentPage
) {

    const totalPages =
        Math.ceil(total / pageLength);

    let html = "";

    html += `
        <li class="page-item ${currentPage === 1 ? 'disabled' : ''}">
            <a class="page-link"
               href="#"
               data-page="${currentPage - 1}">
               Previous
            </a>
        </li>
    `;

    for (let i = 1; i <= totalPages; i++) {

        html += `
            <li class="page-item ${currentPage === i ? 'active' : ''}">
                <a class="page-link"
                   href="#"
                   data-page="${i}">
                   ${i}
                </a>
            </li>
        `;
    }

    html += `
        <li class="page-item ${currentPage === totalPages ? 'disabled' : ''}">
            <a class="page-link"
               href="#"
               data-page="${currentPage + 1}">
               Next
            </a>
        </li>
    `;

    document.getElementById(
        "pagination"
    ).innerHTML = html;

    document
        .querySelectorAll("#pagination .page-link")
        .forEach(link => {

            link.addEventListener("click", function (e) {

                e.preventDefault();

                const page =
                    parseInt(this.dataset.page);

                changePage(page);
            });
        });
}

function changePage(page) {

    const totalPages =
        Math.ceil(totalImages / pageLength);

    if (page < 1 || page > totalPages) {
        return;
    }

    currentPage = page;

    loadImages(page);

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}





let galleryImages = [];
let currentIndex = 0;

function bindGalleryEvents() {

    galleryImages =
        document.querySelectorAll(".gallery-img");

    const modalImage =
        document.getElementById("modalImage");

    const modal =
        new bootstrap.Modal(
            document.getElementById("galleryModal")
        );

    galleryImages.forEach((img, index) => {

        img.addEventListener("click", function () {

            currentIndex = index;

            modalImage.src = this.src;

            modal.show();
        });
    });
}

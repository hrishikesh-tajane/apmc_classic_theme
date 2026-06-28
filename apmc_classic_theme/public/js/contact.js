document.addEventListener("DOMContentLoaded", function () {

    fetch(
        "/api/method/apmc_classic_theme.api.contact.get_contact_details"
    )
        .then(response => response.json())
        .then(data => {


            const contact = data.message;
            document.getElementById("Office_Name").innerText =
                contact.company_name;

            document.getElementById("address").innerText =
                contact.address;

            document.getElementById("phone_number").innerText =
                contact.phone_no;

            document.getElementById("mail").innerText =
                contact.email;

            document.getElementById("map_iframe").src =
                contact.location_url;
        })
        .catch(error => {
            console.error(error);
        });

});
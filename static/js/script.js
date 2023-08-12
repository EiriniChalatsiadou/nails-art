// active nav bar js code//
$(document).ready(
    function () {
        const dictionary = {
            '/': 'homeMenu',
            '/treatments': 'treatmentsMenu',
            '/book-a-treatment/': 'bookTreatmentMenu',
            '/contact': 'contactMenu',
            '/about-us': 'aboutUsMenu',
            '/accounts/logout/': 'logoutMenu',
            '/accounts/login/': 'loginMenu',
        };

        const currentPage = window.location.pathname;
        const matchingPage = Object.keys(dictionary).slice(1).find(key => currentPage.includes(key));
        const menuId = dictionary[matchingPage ?? currentPage];
        // active navbarNav li>a js code//
        $('#navbarNav li>a').removeClass('active');
        $(`#${menuId}`).addClass('active');
    }
);

if (window.location.pathname == "/contact") {
    //initialise map
    let map;

    async function initMap() {
        const { Map } = await google.maps.importLibrary("maps");

        map = new Map(document.getElementById("map"), {
            center: { lat: -34.397, lng: 150.644 },
            zoom: 8,
        });
    }

    initMap();

}
// $('#menu li a').click(function () {

// });



$(document).ready(
    function () {
        const dictionary = {
            '/': 'homeMenu',
            '/treatments': 'treatmentsMenu',
            '/book-a-treatment': 'bookTreatmentMenu',
            '/contact': 'contactMenu',
            '/about-us': 'aboutUsMenu',
            '/accounts/logout/': 'logoutMenu',
            '/accounts/login/': 'loginMenu',
        };
        const currentPage = window.location.pathname;
        const menuId = dictionary[currentPage];

        $('#navbarNav li>a').removeClass('active');
        $(`#${menuId}`).addClass('active');

        console.log(currentPage, menuId, `#${menuId}`);
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
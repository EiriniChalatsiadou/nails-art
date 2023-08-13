/* jshint esversion: 6 */
/* globals $:false */

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

// Define a function for validating the selected date
function validateWorkingHoursAndDays() {
    var selectedDate = new Date($('#id_date').val());
    var selectedTime = selectedDate.getHours() * 60 + selectedDate.getMinutes();
    var isWorkingDay = selectedDate.getDay() >= 1 && selectedDate.getDay() <= 6;
    var isWorkingHour = selectedTime >= 9 * 60 && selectedTime <= 20 * 60;

    if (!isWorkingDay || !isWorkingHour) {
        alert("Please select a working day (Monday to Friday) and a time within working hours (9 AM to 5 PM).");
        return false;
    }

    return true;
}

// Attach a submit event handler to the form
$('form').submit(function (event) {
    if (!validateWorkingHoursAndDays()) {
        event.preventDefault();
    }
});

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
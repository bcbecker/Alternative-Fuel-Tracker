// Initialize and add the map
function initMap() {
    const center = { lat: 39, lng: -98 };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: center,
    });
    geocoder = new google.maps.Geocoder();

    if (document.getElementById("stationsResult")) {
        codeLocation(geocoder, map);
    }
}

function codeLocation(geocoder, map) {
    let targetName = document.getElementsByName("placeName");
    let targetAddress = document.getElementsByName("placeAddress");

    for (let i = 0; i < targetName.length; i++) {
        geocoder.geocode({'address': targetAddress[i].innerText}, function(results, status) {
            if (status === 'OK') {
                if ( i == 0) {
                    //sets to lat/long object as center for the closest result
                    map.setCenter(results[0].geometry.location);
                }
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location,
                label: targetName[i].innerText,
                animation:google.maps.Animation.DROP
            });
            }
        });
    }   
    map.setZoom(11);
}

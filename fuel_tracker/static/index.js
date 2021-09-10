// Initialize and add the map
function initMap() {
    const chicago = { lat: 41.87388888, lng: -87.75555555 };
    // The map, centered at chicago
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: chicago,
    });
    geocoder = new google.maps.Geocoder();

    codeLocation(geocoder, map);
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
                label: targetName[i].innerText
            });
            }
        });
    }   
    map.setZoom(11);  
}


function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 47.215, lng: 38.899},
        zoom: 14
    });
    var Coordinaty = document.getElementById('coord');

    var input = /** @type {!HTMLInputElement} */(
        document.getElementById('pac-input'));

    var types = document.getElementById('type-selector');
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(types);

    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);

    var infowindow = new google.maps.InfoWindow();
    var marker = new google.maps.Marker({
        map: map,
        anchorPoint: new google.maps.Point(0, -29),
        position: {lat: 47.215, lng: 38.899}
    });
    var marker2 = new google.maps.Marker({
        map: map,
        // position: {lat: 47.215, lng: 38.89}
    });

    autocomplete.addListener('place_changed', function() {
        infowindow.close();
        marker.setVisible(false);
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            // User entered the name of a Place that was not suggested and
            // pressed the Enter key, or the Place Details request failed.
            window.alert("No details available for input: '" + place.name + "'");
            return;
        }
        console.log("lat", place.geometry.location.lat());
        console.log("lng", place.geometry.location.lng());

        // If the place has a geometry, then present it on a map.
        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);  // Why 17? Because it looks good.
        }
        marker.setIcon(/** @type {google.maps.Icon} */({
            url: place.icon,
            size: new google.maps.Size(71, 71),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(17, 34),
            scaledSize: new google.maps.Size(35, 35)
        }));
        marker.setPosition(place.geometry.location);
        marker.setVisible(true);

        marker2.setPosition(place.geometry.location);
        marker2.setVisible(true);

        Coordinaty.innerHTML = place.name;

        var address = '';
        if (place.address_components) {
            address = [
                (place.address_components[0] && place.address_components[0].short_name || ''),
                (place.address_components[1] && place.address_components[1].short_name || ''),
                (place.address_components[2] && place.address_components[2].short_name || '')
            ].join(' ');
        }

        infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + address);
        infowindow.open(map, marker);
    });

    // Sets a listener on a radio button to change the filter type on Places
    // Autocomplete.
    function setupClickListener(id, types) {
        var radioButton = document.getElementById(id);
        radioButton.addEventListener('click', function() {
            autocomplete.setTypes(types);
        });
    }

    setupClickListener('changetype-all', []);
    setupClickListener('changetype-address', ['address']);
    setupClickListener('changetype-establishment', ['establishment']);
    setupClickListener('changetype-geocode', ['geocode']);
}


window.onload = function() {
    // ----- Work with JSON ----- 
    var btnAkcept = document.getElementById('akcept');
    var JsonStr = {
        name: "Админ",
        Email: "test@email.ru",
        ObjectName: "Точка сбора мусора",
        adress: "Место", // place.name,
        date: "сегодня"
    },
        textj = ' ';
    // var p_name = JSON.parse(JsonStr.name),
    //     p_email = JSON.parse(JsonStr.Email),
    //     p_objName = JSON.parse(JsonStr.ObjectName),
    //     p_adress = JSON.parse(JsonStr.adress),
    //     p_date = JSON.parse(JsonStr.date);
    // Coordinaty.innerHTML = place.name;
    
    btnAkcept.addEventListener("click", function() {
     var adres = document.getElementById('coord'),
        name = document.getElementById('pname'),
        email = document.getElementById('pemail'),
        obj_name = document.getElementById('pobj');

        JsonStr.adress = adres.innerHTML;
        JsonStr.name = name.value;
        JsonStr.Email = email.value;
        JsonStr.ObjectName = obj_name.value;
        textj = JSON.stringify(JsonStr);
        // Тут вхерач пост запрос на сервер с этим ЖСОНОм
        // на роут http://0.0.0.0:8000/map_append_object/

        var xhr = new XMLHttpRequest();
        var jsontext;
        var url_ = "http://0.0.0.0:8000/map_append_object/"
        xhr.timeout = 2000;
        xhr.onreadystatechange = function(e){
            console.log(this);
            if (xhr.readyState === 4){
                if (xhr.status === 200){
                    jsontext = xhr.response; // get answer and pars Json
                    console.log(jsontext);
                } else {
                    console.error("XHR didn't work: ", xhr.status);
                }
            }
        };
        xhr.ontimeout = function (){
            console.error("request timedout: ", xhr);
        };
        xhr.open("POST", url_, true); 
        // xhr.responseType = "text";
        xhr.send(textj);   
        // alert(JSON.stringify(JsonStr));
    });
};

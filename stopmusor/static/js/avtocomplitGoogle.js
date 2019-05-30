// --- Этот файл не использовается для Яндекс карт ----
function initMap() {
    console.log("initMap");
    
    window.dolgota = 0,
    window.shirota = 0;
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

    // var infowindow = new google.maps.InfoWindow();
    // var marker = new google.maps.Marker({
    //     map: map,
    //     anchorPoint: new google.maps.Point(0, -29),
    //     position: {lat: 47.215, lng: 38.899}
    // });

    var infoWindow = new google.maps.InfoWindow({
        maxWidth: 160
    });
    var Markers = new Array();
    var markerCounter = 0;

    console.log(window.koordx);

    autocomplete.addListener('place_changed', function() {
        // infowindow.close();
        // marker.setVisible(false);
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            // User entered the name of a Place that was not suggested and
            // pressed the Enter key, or the Place Details request failed.
            window.alert("No details available for input: '" + place.name + "'");
            return;
        }
        console.log("lat", place.geometry.location.lat());
        console.log("lng", place.geometry.location.lng());
        window.dolgota = place.geometry.location.lng();
        window.shirota = place.geometry.location.lat();
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

        // marker2.setPosition(38.92, 47.225);
        // marker2.setVisible(true);

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


    /////avtocomplit.js


    var xhr1 = new XMLHttpRequest();
    var jsontext1;
    var url1_ = "http://0.0.0.0:8000/get_map_objects/";
    xhr1.timeout = 2000;
    xhr1.onreadystatechange = function(e){
        console.log(this);
        if (xhr1.readyState === 4){
            if (xhr1.status === 200){
                jsontext1 = xhr1.response;
                var jsontext2 = JSON.parse(jsontext1);
                var data = Array();
                data = jsontext2.data;
                
                //

                for (var i = 0; i < data.length; i++){
                    var marker = new google.maps.Marker({
                        position: new google.maps.LatLng(data[i].lat, data[i].lng),
                        map: map,
                    });
                    Markers.push(marker);
                    google.maps.event.addListener(
                        marker,
                        'click',
                        (function(marker, i){
                            return function(){
                                infoWindow.setContent("Объект по адресу: \n" + data[i].adress);
                                infoWindow.open(map, marker);
                            }
                        })(marker, i)
                    );
                }
                
            } else {
                console.error("XHR didn't work: ", xhr1.status);
            }
        }
    };
    xhr1.ontimeout = function (){
        console.error("request timedout: ", xhr1);
    };
    xhr1.open("GET", url1_, true); 
    xhr1.send();
}


window.onload = function() {
    // ----- Work with JSON ----- 
    var btnAkcept = document.getElementById('akcept');
    var JsonStr = {
        name: "Админ",
        Email: "test@email.ru",
        ObjectName: "Точка сбора мусора",
        adress: "Место", // place.name,
        lng: "Долгота:",
        lat: "Широта",
        date: "сегодня"
    },
        textj = ' ';

    // ----- Add event listener to accept button -----
    btnAkcept.addEventListener("click", function() {
     var adres = document.getElementById('coord'),
        name = document.getElementById('pname'),
        email = document.getElementById('pemail'),
        obj_name = document.getElementById('pobj');

        JsonStr.adress = adres.innerHTML;
        JsonStr.name = name.value;
        JsonStr.Email = email.value;
        JsonStr.ObjectName = obj_name.value;
        JsonStr.lng = window.dolgota;
        JsonStr.lat = window.shirota;
        textj = JSON.stringify(JsonStr);

        var xhr = new XMLHttpRequest();
        var jsontext;
        var lat1 = "temp";
        var url_ = "http://0.0.0.0:8000/map_append_object/";
        xhr.timeout = 2000;
        xhr.onreadystatechange = function(e){
            console.log(this);
            if (xhr.readyState === 4){
                if (xhr.status === 200){
                    jsontext = xhr.response;
                    vivod();
                } else {
                    console.error("XHR didn't work: ", xhr.status);
                }
            }
        };
        
        xhr.ontimeout = function (){
            console.error("request timedout: ", xhr);

        };

        xhr.open("POST", url_, true); 
        xhr.send(textj); 
        
        function vivod() {
            lat1 = JSON.parse(jsontext);
            console.log("Долгота: "+lat1.lng+" Широта: "+lat1.lat); 
        }
  
    });
};

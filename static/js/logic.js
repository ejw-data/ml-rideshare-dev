  //MapQuest Key
  L.mapquest.key = '6aMCYSpGBo4Eg20Lw7RljQ0nXcUGsA5S';
  
  //START MAIN CODE
     
  var map = L.mapquest.map("map", {
    center: [41.881832, -87.623177],
    layers: L.mapquest.tileLayer('map'),
    zoom: 12
  });

  L.mapquest.directions().route({
    start: '425 N. Wabash Ave., Chicago, IL 60611',
    end: '255 E Grand Ave, Chicago, IL 60611'
  });
//END MAIN CODE

  
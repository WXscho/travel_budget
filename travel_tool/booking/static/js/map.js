// Initialize and add the map
let map;

async function initMap() {
  // The location of Uluru
  const omaha = { lat: 41.2565, lng: -95.9345  };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("map"), {
    zoom: 4,
    center: omaha,
    mapId: "5bb371f7ed5bf9c83b56cc50"
  });

  //marker
  const marker = new AdvancedMarkerElement({
    map: map,
    position: omaha,
    title: "Omaha, NE",
  });
}
window.initMap = initMap;
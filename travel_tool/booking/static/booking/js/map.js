console.log("Javascript file being called");
document.addEventListener('DOMContentLoaded', () => {

    console.log("Javascript file being called");
    const geoBtn = document.getElementById("geoBtn");
    const output = document.getElementById("output");
    const addressInput = document.getElementById("inputAddress");
    const gmpMap = document.getElementById("map");
    if (!gmpMap) {
        console.error("gmp-map element not found");
        return;
    }
    let dynamicMarker = document.createElement("gmp-advanced-marker");
    gmpMap.appendChild(dynamicMarker);

//Relearn event listening in base JavaScript
    geoBtn.addEventListener("click", async () => {
        const address = addressInput.value.trim();
        if (!address){
            output.textContent="Please enter an address";
            return;
        }
        const apiKey ="AIzaSyDkXYMnF_IcOBCNQS_iERScFy2ETP9p9_w"
        const encodedAddress = encodeURIComponent(address);
        console.log(encodedAddress);
        const url = `https://maps.googleapis.com/maps/api/geocode/json?address=${encodedAddress}&key=${apiKey}`;
        console.log(url);

        try {
            const response = await fetch(url);
            const data = await response.json();
            console.log(data.status);
            if (data.status === "OK"){

                const location = data.results[0].geometry.location;
                output.textContent = `Latitude: ${location.lat}, Longitude: ${location.lng}`;

                gmpMap.setAttribute("center", `${location.lat},${location.lng}`);
                gmpMap.setAttribute("zoom","14");

                dynamicMarker.setAttribute("position",`${location.lat},${location.lng}`);
                dynamicMarker.setAttribute("title",address);
            }else{
                output.textContent="Couldn't find location";
            }
        }catch (error){
            console.error("Error:", error);
            output.textContent = "Error fetching location.";
        }

    });
});


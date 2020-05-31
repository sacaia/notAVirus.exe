// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

(function (apiUrl) {
    function fetchTest() {
        return fetch(apiUrl + "/test")
            .then(function (response) {
                if (response.status === 200)
                    console.log(response)
                // response tem o JSON
                return response.json()
            })
        }

        function fetchAirPolution() {
            return fetch(apiUrl + "/airpolution")
                .then(function (response) {
                    if (response.status === 200)
                        console.log(response)
                    // response tem o JSON
                    return response.json()
                })
        }
        

        fetchAirPolution()
    }) ("https://notav1rus.herokuapp.com");

/*
// Area Chart Example
fetch('https://ghoapi.azureedge.net/api/WHS9_92').then((r) => r.json()).then((data) => {

    console.log(data)

    const countries = ChartGeo.topojson.feature(data, data.objects.countries).features;

    console.log(countries)

    const chart = new Chart(document.getElementById("canvas").getContext("2d"), {
        type: 'choropleth',
        data: {
            labels: countries.map((d) => d.properties.name),
            datasets: [{
                label: 'Countries',
                data: countries.map((d) => ({ feature: d, value: Math.random() })),
            }]
        },
        options: {
            showOutline: true,
            showGraticule: true,
            legend: {
                display: false
            },
            scale: {
                projection: 'equalEarth'
            },
            geo: {
                colorScale: {
                    display: true,
                },
            },
        }
    });
});*/
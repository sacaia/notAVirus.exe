// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

(function (apiUrl, header = "origin: notavirus.biz") {
    function fetchWHS9_92() {
      return fetch(apiUrl + "/test")
        .then(function (response) {
          if (response.status === 200)
            console.log(response)
            return response.json()
        })
        .then(function (response) {
          console.log(response)
        })
    }
  
    console.log(fetchWHS9_92())
  })("https://notav1rus.herokuapp.com");

/*
https://notav1rus.herokuapp.com/?name=Life+expectancy+at+age+60+%28years%29&filter_data=Dim1&value=2001
https://notav1rus.herokuapp.com/?name=Life+expectancy+at+age+60+%28years%29&filter_data=Dim1&value=BTSX
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
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
        return fetch(apiUrl + "/unstats/392")
            .then(function (response) {
                if (response.status === 200)
                    console.log(response)
                // response tem o JSON
                return response.json()
            })
            .then(function (data) {
                console.log(data)

                const countries = []
                const values = []

                data.forEach(element => {
                    if (element.Value != null) {
                        countries.push(element.Country)
                        values.push(element.Value)
                    }
                })

                console.log(countries)
                console.log(values)

                var ctx = document.getElementById("canvas");
                var myLineChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: countries,
                        datasets: [{
                            label: "Percentage",
                            backgroundColor: "[rgba(200,200,200,200),rgba(200,200,200,200)]",
                            borderColor: "rgba(2,117,216,1)",
                            data: values,
                        }],
                    },
                    options: {
                        scales: {
                            xAxes: [{
                                time: {
                                    unit: 'Countries'
                                },
                                gridLines: {
                                    display: false
                                },
                                ticks: {
                                    maxTicksLimit: 205
                                }
                            }],
                            yAxes: [{
                                ticks: {
                                    min: 0,
                                    max: 100,
                                    maxTicksLimit: 10
                                },
                                gridLines: {
                                    display: true
                                }
                            }],
                        },
                        legend: {
                            display: false
                        }
                    }
                });
                /*
                const chart = new Chart(document.getElementById("canvas").getContext("2d"), {
                    type: 'bar',
                    data: {
                        labels: countries,
                        datasets: [{
                            label: 'Countries',
                            data: values,
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
                })
                */
            })
    }

    a = fetchAirPolution()

    console.log(a)
})("https://notav1rus.herokuapp.com");


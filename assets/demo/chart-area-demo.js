// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

function fetchAirPolution() {
  return fetch("https://notav1rus.herokuapp.com/unstats/621")
    .then(function (response) {
      if (response.status === 200)
        console.log(response)
      return response.json()
    })
    .then(function (response) {
      console.log(response)
    })
}

// Area Chart Example
var ctx = document.getElementById('myChart');
var chartData = {
  type: 'line',
  data: {
    labels: ['Running', 'Swimming', 'Eating', 'Cycling'],
    datasets: [{
      label: 'Line Dataset',
      data: [10, 20, 30, 40],
      order: 1
    }, {
      label: 'Line Dataset',
      data: [10, 30, 10, 10],
      backgroundColor: 'rgb(255, 99, 132)',
      type: 'line',
      order: 2
    }],
  },
  options: {
    scales: {},
    title: {
      display: true,
      text: 'Custom Chart Title'
    },
    tooltips: {
      mode: 'point',
    },
  }
};
var myChart = new Chart(ctx, chartData);

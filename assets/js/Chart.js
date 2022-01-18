/*
const labels = [
    10,20,30,40,50
];

const data = {
    labels: labels,
    datasets: [{
        label: 'My First dataset',
        //backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        data: [1000,1250,1500,1750,2000,2250,2500,2750,3000],
    }]
};

const config = {
    type: 'line',
    data: data,
    options: {}
};

const myChart = new Chart(
    document.getElementById('myChart'),
    config
);*/
const config = {
    type: 'scatter',
    data: data,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Chart.js Scatter Multi Axis Chart'
            }
        },
        scales: {
            y: {
                type: 'linear', // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                position: 'left',
                ticks: {
                    color: Utils.CHART_COLORS.red
                }
            },
            y2: {
                type: 'linear', // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                position: 'right',
                reverse: true,
                ticks: {
                    color: Utils.CHART_COLORS.blue
                },
                grid: {
                    drawOnChartArea: false // only want the grid lines for one axis to show up
                }
            }
        }
    },
};
document.addEventListener("DOMContentLoaded", async () => {

    const response = await fetch('/data');
    const chartData = await response.json();
    const ctx = document.getElementById('tempHumidityChart').getContext('2d');
    
    const data = {
        labels: chartData.labels,
        datasets: 
        [
        {
            label: 'Temperature (°C)',
            data: chartData.temperature,
            fill: true,
            borderColor: 'rgba(255, 99, 132, 1)',
            backgroundColor: 'rgba(255, 0, 0, 0.2)',
            pointBackgroundColor: 'rgb(255, 255, 255)',
            tension: 0,
            pointStyle: false,
            yAxisID: 'y',
        },
        {
            label: 'humidity',
            data: chartData.humidity,
            fill:false,
            borderColor: 'rgb(35, 32, 216)',
            backgroundColor: 'rgb(7, 8, 92)',
            pointBackgroundColor: 'rgb(255, 255, 255)',
            tension: 0,
            pointStyle: false,
            yAxisID: 'y1',
        }
        ]

        }
        const config = {
            type: 'line',
            data: data,
            options: {
                responsive: true,
                interaction: {
                  mode: 'index',
                  intersect: false,
                },
                stacked: false,
                plugins: {
                  legend: {
                    display: true,
                    labels: {
                        usePointstyle: true
                    }
                
                  }
                  },
                scales: {
                  y: {
                    type: 'linear',
                    display: true,
                    position: 'left',
                    suggestedMin: Math.min(...chartData.temperature) - 0.2,
                    suggestedMax: Math.max(...chartData.temperature) + 0.2,
                    grid:{
                      drawOnChartArea: false,
                    }
                  },
                  y1: {
                    type: 'linear',
                    display: true,
                    position: 'right',
                    suggestedMin: Math.min(...chartData.temperature) - 4,
                    // grid line settings
                    grid: {
                      drawOnChartArea: false, // only want the grid lines for one axis to show up
                    },
                  },
                }
              },
          };
    const tempHumidityChart = new Chart(ctx, config);

})
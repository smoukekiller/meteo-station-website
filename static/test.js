document.addEventListener("DOMContentLoaded", async () => {

    const response = await fetch('/data');
    const chartData = await response.json();
    const ctx = document.getElementById('tempHumidityChart').getContext('2d');
    const sampledData = {
        labels: chartData.labels.filter((_, index) => index % 40 === 0),
        temperature: chartData.temperature.filter((_, index) => index % 40 === 0)
    };
    
    const tempHumidityChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: sampledData.labels, // Use fewer labels
            datasets: [
                {
                    label: 'Temperature (°C)',
                    data: sampledData.temperature, 
                    borderColor: 'rgba(255, 99, 132, 1)',
                    backgroundColor: 'rgba(255, 0, 0, 0.2)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.3, // Smooth curve
                },
                // {
                //     label: 'Humidity (%)',
                //     data: chartData.humidity, // Use all 168 data points
                //     borderColor: 'rgba(54, 162, 235, 1)',
                //     backgroundColor: 'rgba(54, 162, 235, 0.2)',
                //     borderWidth: 2,
                //     fill: true,
                //     tension: 0.3,
                // }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
            },
            scales: {
                x: {
                    type: 'category', // Linear scale for more data points than labels
                    ticks: {
                        callback: function(value, index) {
                            return index % 200 === 0 ? sampledData.labels[index] : '';
                        }
                    }
                },
                y: {
                    beginAtZero: true,
                    suggestedMin: Math.min(...sampledData.temperature) - 5,
                    suggestedMax: Math.max(...sampledData.temperature) + 5
                }
            }
        }
    });
});
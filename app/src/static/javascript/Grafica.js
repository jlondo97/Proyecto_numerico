$(document).ready(function () {
  var _data;
  var _labels;

  $.ajax({
    url: "/get_data_Biseccion",
    type: "get",
    data: { vals: "" },
  }).then(function (response) {
    full_data = JSON.parse(response.payload);
    _data = full_data["data"];
    _labels = full_data["labels"];

    var ctx = document.getElementById("canvas").getContext("2d");
    var myChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: _labels,
        datasets: [
          {
            label: "Grafica1",
            data: _data,

            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
      },
    });
  });
});

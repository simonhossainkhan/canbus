$( document ).ready(function() {
    var trip_info_endpoint = "api/trip-information/"
    console.log(hostName);

    function get_trip_info(tripID) {
        $.ajax({
          type: "GET",
          url: hostName + trip_info_endpoint + "?tripID=" + tripID,
          success: function(apiData){
            generateTimeChart("mph", "Time vs MPH", apiData["list"]["time"], apiData["list"]["mph"], "MPH", "Time")
            generateTimeChart("rpm", "Time vs RPM", apiData["list"]["time"], apiData["list"]["rpm"], "RPM", "Time")
            generateTimeChart("throttle", "Time vs Throttle", apiData["list"]["time"], apiData["list"]["throttle"], "Throttle", "Time")
            generateTimeChart("load", "Time vs % Load", apiData["list"]["time"], apiData["list"]["load"], "Load", "Load")
            generateTimeChart("fuel_status", "Time vs Fuel Status", apiData["list"]["time"], apiData["list"]["fuel_status"], "Fuel Status", "Time")
          },
          error: function(){
          }
        });
    }

    function generateTimeChart(elemID, title, x_data, y_data, x_axis_title, y_axis_title) {
        var data = [
          {
            x: x_data,
            y: y_data,
            type: 'scatter'
          }
        ];

        var layout = {
          title: title,
          xaxis: {
            title: x_axis_title,
          },
          yaxis: {
            title: y_axis_title,
          }
        };

        Plotly.newPlot(elemID, data, layout);

    }

    $('.trip-panel').click(function(event) {
        var status = $(this).attr('id');
        $(".active").removeClass("active");
        $(this).addClass("active");

        get_trip_info(status)
    });


});


d3.csv("../Data/per-capita-alcohol-1890.csv").then(function(rows){

    var frames = []
    var slider_steps = []
  
    //number of years - 1
    var n = 7;
    //starting date
    var num = 1890;
    for (var i = 0; i <= n; i++) {
      //get alcohol consumption number
      var z = rows.filter(row => row['Year'] == num).map(row => row['alcohol_consumption'])
      //use country code to get location
      var locations = rows.filter(row => row['Year'] == num).map(row => row['Code'])
      //add frame info to list
      frames[i] = {data: [{z: z, locations: locations, text: locations}], name: num}
      slider_steps.push ({
          label: num.toString(),
          method: "animate",
          args: [[num], {
              mode: "immediate",
              transition: {duration: 300},
              frame: {duration: 300}
            }
          ]
        })
      if (num == 1890) {
        num = num + 30;
      }
      else if (num == 1920) {
        num = num + 40;
      }
      else if (num == 2000) {
        num = num + 14;
      }
      else {
        num = num + 10;
      }
    }

  var data = [{
        type: 'choropleth',
        locationmode: 'world',
        locations: frames[0].data[0].locations,
        z: frames[0].data[0].z,
        text: frames[0].data[0].locations,
        zauto: false,
        zmin: 4,
        zmax: 23
  
  }];
  var layout = {
      title: 'Per Capita Alcohol Consumption in Select Countries<br>1890 - 2014',
      geo:{
         scope: 'world',
         countrycolor: 'rgb(255, 255, 255)',
         showland: true,
         landcolor: 'rgb(217, 217, 217)',
         showlakes: true,
         lakecolor: 'rgb(255, 255, 255)',
         subunitcolor: 'rgb(255, 255, 255)',
         lonaxis: {},
         lataxis: {}
      },
      updatemenus: [{
        x: 0.1,
        y: 0,
        yanchor: "top",
        xanchor: "right",
        showactive: false,
        direction: "left",
        type: "buttons",
        pad: {"t": 87, "r": 10},
        buttons: [{
          method: "animate",
          args: [null, {
            fromcurrent: true,
            transition: {
              duration: 50,
            },
            frame: {
              duration: 1000
            }
          }],
          label: "Play"
        }, {
          method: "animate",
          args: [
            [null],
            {
              mode: "immediate",
              transition: {
                duration: 0
              },
              frame: {
                duration: 0
              }
            }
          ],
          label: "Pause"
        }]
      }],
      sliders: [{
        active: 0,
        steps: slider_steps,
        x: 0.1,
        len: 0.9,
        xanchor: "left",
        y: 0,
        yanchor: "top",
        pad: {t: 50, b: 10},
        currentvalue: {
          visible: true,
          prefix: "Year:",
          xanchor: "right",
          font: {
            size: 20,
            color: "#666"
          }
        },
        transition: {
          duration: 300,
          easing: "cubic-in-out"
        }
      }]
  };
  
  Plotly.newPlot('global_consumption', data, layout).then(function() {
      Plotly.addFrames('global_consumption', frames);
    });
  })
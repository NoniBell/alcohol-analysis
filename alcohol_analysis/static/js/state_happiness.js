function optionChanged2(){

    //Get input value from drop down
    let state = d3.select("#selDataset2").node().value;
    let alcohol = d3.select("#selDataset3").node().value;
    // build plot with new data
    buildPlot2(state,alcohol);
  };
  
  //Build Plots
  function buildPlot2(state,alcohol){
    d3.json("/api/happiness")
        .then((data)=>
        d3
        .csv("/api/cleaned_sales")
          .then(states1=>{
        let filteredData = states1.filter(d => d.FIPS === state);
        //console.log(filteredData);
        let happiness = data.filter(d=>d.country_name === "United States").map(d=>d.life_ladder);
        let years = data.filter(d=>d.country_name === "United States").map(d=>d.year);
  
        if(alcohol === "All Alcohol Types" || alcohol === "All Beverages"){
            let trace1 = {
                x: years,
                y: happiness,
                type: 'scatter',
                name: 'Happiness Index'
              };
              let trace2 = {
                x: years,
                y: filteredData.filter(d=>d.Beverage === "All Beverages").map(d=>d.Ethanol),
                type: 'scatter',
                name: 'Alcohol Consumption (G)',
                yaxis: "y2"
              };
            
            let data1 = [trace1, trace2];
  
            var layout = {
                title: `United States Happiness Index vs. ${state} Alcohol Consumption`,
                yaxis: {title: 'Happiness Index (10 pt scale)'},
                yaxis2: {
                  title: 'Alcohol G/person',
                  titlefont: {color: 'rgb(0,0,0)'},
                  tickfont: {color: 'rgb(0,0,0)'},
                  overlaying: 'y',
                  side: 'right'
                }
              };
            
            Plotly.newPlot('stateHappiness', data1,layout);
  
            stateHappiness.on('plotly_relayout', function(eventdata){});
        }else if (alcohol === "Wine"){
            let trace1 = {
                x: years,
                y: happiness,
                type: 'scatter',
                name: 'Happiness Index'
              };
            let trace2 = {
                x: years,
                y: filteredData.filter(d=>d.Beverage === "Wine").map(d=>d.Gallons),
                type: 'scatter',
                name: `${alcohol} Consumption`,
                yaxis: "y2"
              };
            
            let data1 = [trace1, trace2];
  
            var layout = {
                title: `United States Happiness Index vs. ${state} ${alcohol} Consumption`,
                yaxis: {title: 'Happiness Index (10 pt scale)'},
                yaxis2: {
                  title: `${alcohol} Consumption G`,
                  titlefont: {color: 'rgb(0,0,0)'},
                  tickfont: {color: 'rgb(0,0,0)'},
                  overlaying: 'y',
                  side: 'right'
                }
              };
            
            Plotly.newPlot('stateHappiness', data1,layout);
  
            stateHappiness.on('plotly_relayout', function(eventdata){});
        }else if(alcohol === "Spirits"){
            let trace1 = {
                x: years,
                y: happiness,
                type: 'scatter',
                name: 'Happiness Index'
              };
            let trace2 = {
                x: years,
                y: filteredData.filter(d=>d.Beverage === "Spirits").map(d=>d.Gallons),
                type: 'scatter',
                name: `${alcohol} Consumption`,
                yaxis: "y2"
              };
            
            let data1 = [trace1, trace2];
  
            var layout = {
                title: `United States Happiness Index vs. ${state} ${alcohol} Consumption`,
                yaxis: {title: 'Happiness Index (10 pt scale)'},
                yaxis2: {
                  title: `${alcohol} Consumption G`,
                  titlefont: {color: 'rgb(0,0,0)'},
                  tickfont: {color: 'rgb(0,0,0)'},
                  overlaying: 'y',
                  side: 'right'
                }
              };
            
            Plotly.newPlot('stateHappiness', data1,layout);
  
            stateHappiness.on('plotly_relayout', function(eventdata){});
        }else if (alcohol === "Beer"){
            let trace1 = {
                x: years,
                y: happiness,
                type: 'scatter',
                name: 'Happiness Index'
              };
            let trace2 = {
                x: years,
                y: filteredData.filter(d=>d.Beverage === "Beer").map(d=>d.Gallons),
                type: 'scatter',
                name: `${alcohol} Consumption`,
                yaxis: "y2"
              };
            
            let data1 = [trace1, trace2];
  
            var layout = {
                title: `United States Happiness Index vs. ${state} ${alcohol} Consumption`,
                yaxis: {title: 'Happiness Index (10 pt scale)'},
                yaxis2: {
                  title: `${alcohol} Consumption G`,
                  titlefont: {color: 'rgb(0,0,0)'},
                  tickfont: {color: 'rgb(0,0,0)'},
                  overlaying: 'y',
                  side: 'right'
                }
              };
            
            Plotly.newPlot('stateHappiness', data1,layout);
  
            stateHappiness.on('plotly_relayout', function(eventdata){});
        }
        
        }
        )
    )    
  }
  
  
  //load in initial happiness and alcohol data
  function init2(){
    //read data
    d3.csv("/api/happiness")
        .then((countries)=>
        d3
            .csv("/api/cleaned_sales")
            .then(states=>{
  
    //build dropdownMenu1 with initial page being United States
    let state = states.map(d=>d.FIPS)
    let unique_states = []
    state.forEach(element =>{
        if(!unique_states.includes(element)){
        // console.log(element);
        unique_states.push(element)
    }
        else if(unique_states.includes(element)){
            console.log('skip')
        }})
    let selector = d3.select("#selDataset2");
    selector.append("option").text("Illinois");
    unique_states.forEach((i)=>{
        let option = selector.append("option");
        option.text(i);
    });
  
    //build dropdownMenu2 with initial page being all alcohol types
    let alcohol_types = states.map(d=>d.Beverage);
    let unique_alcohol = []
    alcohol_types.forEach(element =>{
      if(!unique_alcohol.includes(element)){
      // console.log(element);
      unique_alcohol.push(element)
  }
      else if(unique_alcohol.includes(element)){
          console.log('skip')
      }})
    let selector1 = d3.select("#selDataset3");
    selector1.append("option").text("All Alcohol Types");
    unique_alcohol.forEach((i)=>{
        let option = selector1.append("option");
        option.text(i)
    });
  
   //filter data for plot
    let initialState = states.filter(d => d.FIPS === "Illinois");
    let initialHappiness = countries.filter(d=>d.country_name === "United States").map(d=>d.life_ladder);
    let initialYears = countries.filter(d=>d.country_name === "United States").map(d=>d.year);
    let initialAll = initialState.map(d=>d.Ethanol);
    
    let initialTrace1 = {
        x: initialYears,
        y: initialHappiness,
        type: 'scatter',
        name: 'Happiness Index'
      };
  
    let initialTrace2 = {
        x: initialYears,
        y: initialAll,
        type: 'scatter',
        name: 'Beverage Consumption',
        yaxis: "y2"
      };
      
    let initialData = [initialTrace1, initialTrace2];
  
    var initialLayout = {
        title: 'United States Happiness vs. Illinois Alcohol Consumption',
        yaxis: {title: 'Happiness Index (10 pt scale)'},
        yaxis2: {
          title: 'Alcohol G/person',
          titlefont: {color: 'rgb(0,0,0)',size:12},
          tickfont: {color: 'rgb(0,0,0)'},
          overlaying: 'y',
          side: 'right'
        },
      };
      
    Plotly.newPlot('stateHappiness', initialData,initialLayout);
  
    stateHappiness.on('plotly_relayout',
    function(eventdata){
    });
  }))
  };
  
  init2();
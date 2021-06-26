function optionChanged1(){

    //Get input value from drop down
    let country = d3.select("#selDataset").node().value;
    let alcohol = d3.select("#selDataset1").node().value;
    // console.log(alcohol);
    // console.log(country);
    // build plot with new data
    buildPlot1(country,alcohol);
};

function buildPlot1(country,alcohol){
    d3.json("/api/happiness")
        .then((data)=>
        d3
        .json("/api/wine")
        .then(wine1=>
            d3.json("/api/spirits")
            .then(spirits1=>
                d3.json("/api/beer")
                .then(beer1=>{
        let filteredData = data.filter(d => d.country_name === country);
        let happiness = filteredData.map(d=>d.life_ladder);
        let years = filteredData.map(d=>d.year);
        let wine = wine1.filter(d=>d.country_name === country).map(d=>d.wine_consumption);
        let spirits = spirits1.filter(d=>d.country_name === country).map(d=>d.spirits_consumption);
        let beer = beer1.filter(d=>d.country_name === country).map(d=>d.beer_consumption);
        //console.log(happiness);
        //console.log(years);
        console.log(wine);
        if(alcohol === "All Alcohol Types"){
            let trace1 = {
                x: years,
                y: happiness,
                type: 'scatter',
                name: 'Happiness Index'
              };
              let trace2 = {
                x: years,
                y: wine,
                type: 'scatter',
                name: 'Wine Consumption',
                yaxis: "y2"
              };
            let trace3 = {
                x: years,
                y: spirits,
                type: 'scatter',
                name: 'Spirits Consumption',
                yaxis: "y2"
              };
            let trace4 = {
                x: years,
                y: beer,
                type: 'scatter',
                name: 'Beer Consumption',
                yaxis: "y2"
              };
            
            let data1 = [trace1, trace2, trace3, trace4];

            var layout = {
                title: `${country} Happiness Index vs. Alcohol Consumption`,
                yaxis: {title: 'Happiness Index (10 pt scale)'},
                yaxis2: {
                  title: 'Alcohol L/person',
                  titlefont: {color: 'rgb(0,0,0)'},
                  tickfont: {color: 'rgb(0,0,0)'},
                  overlaying: 'y',
                  side: 'right'
                }
              };
            
            Plotly.newPlot('worldHappiness', data1,layout);

            worldHappiness.on('plotly_relayout', function(eventdata){});
        }else if (alcohol === "Wine"){
            let trace1 = {
                x: years,
                y: happiness,
                type: 'scatter',
                name: 'Happiness Index'
              };
            let trace2 = {
                x: years,
                y: wine,
                type: 'scatter',
                name: `${alcohol} Consumption`,
                yaxis: "y2"
              };
            
            let data1 = [trace1, trace2];

            var layout = {
                title: `${country} Happiness Index vs. ${alcohol} Consumption`,
                yaxis: {title: 'Happiness Index (10 pt scale)'},
                yaxis2: {
                  title: `${alcohol} Consumption L`,
                  titlefont: {color: 'rgb(0,0,0)'},
                  tickfont: {color: 'rgb(0,0,0)'},
                  overlaying: 'y',
                  side: 'right'
                }
              };
            
            Plotly.newPlot('worldHappiness', data1,layout);

            worldHappiness.on('plotly_relayout', function(eventdata){});
        }else if(alcohol === "Spirits"){
            let trace1 = {
                x: years,
                y: happiness,
                type: 'scatter',
                name: 'Happiness Index'
              };
            let trace2 = {
                x: years,
                y: spirits,
                type: 'scatter',
                name: `${alcohol} Consumption`,
                yaxis: "y2"
              };
            
            let data1 = [trace1, trace2];

            var layout = {
                title: `${country} Happiness Index vs. ${alcohol} Consumption`,
                yaxis: {title: 'Happiness Index (10 pt scale)'},
                yaxis2: {
                  title: `${alcohol} Consumption L`,
                  titlefont: {color: 'rgb(rgb(0,0,0))'},
                  tickfont: {color: 'rgb(rgb(0,0,0))'},
                  overlaying: 'y',
                  side: 'right'
                }
              };
            
            Plotly.newPlot('worldHappiness', data1,layout);

            worldHappiness.on('plotly_relayout', function(eventdata){});
        }else if (alcohol === "Beer"){
            let trace1 = {
                x: years,
                y: happiness,
                type: 'scatter',
                name: 'Happiness Index'
              };
            let trace2 = {
                x: years,
                y: beer,
                type: 'scatter',
                name: `${alcohol} Consumption`,
                yaxis: "y2"
              };
            
            let data1 = [trace1, trace2];

            var layout = {
                title: `${country} Happiness Index vs. ${alcohol} Consumption`,
                yaxis: {title: 'Happiness Index (10 pt scale)'},
                yaxis2: {
                  title: `${alcohol} Consumption L`,
                  titlefont: {color: 'rgb(0,0,0)'},
                  tickfont: {color: 'rgb(0,0,0)'},
                  overlaying: 'y',
                  side: 'right'
                }
              };
            
            Plotly.newPlot('worldHappiness', data1,layout);

            worldHappiness.on('plotly_relayout', function(eventdata){});
        }
        
        }
        )
    )    
))}


//load in initial happiness and alcohol data
function init1(){
    //read data
    d3.json("/api/happiness")
        .then((countries)=>
        d3
            .json("/api/wine")
            .then(wine=>
                d3
                .json("/api/spirits")
                .then(spirits=>
                    d3.json("/api/beer")
                    .then(beer=>{

    //build dropdownMenu1 with initial page being United States
    let country = countries.map(d=>d.country_name)
    let unique_countries = []
    country.forEach(element =>{
        if(!unique_countries.includes(element)){
        // console.log(element);
        unique_countries.push(element)
    }
        else if(unique_countries.includes(element)){
            console.log('skip')
        }})
    let selector = d3.select("#selDataset");
    selector.append("option").text("United States");
    unique_countries.forEach((i)=>{
        let option = selector.append("option");
        option.text(i);
    });

    //build dropdownMenu2 with initial page being all alcohol types
    let alcohol_types = ['Wine','Spirits','Beer'];
    let selector1 = d3.select("#selDataset1");
    selector1.append("option").text("All Alcohol Types");
    alcohol_types.forEach((i)=>{
        let option = selector1.append("option");
        option.text(i)
    });

   //filter data for plot
    let initialFilteredData = countries.filter(d => d.country_name === "United States");
    let initialHappiness = initialFilteredData.map(d=>d.life_ladder);
    let initialYears = initialFilteredData.map(d=>d.year);
    let initialWine = wine.filter(d=>d.country_name ==="United States").map(d=>d.wine_consumption);
    let initialSpirits = spirits.filter(d=>d.country_name === "United States").map(d=>d.spirits_consumption);
    let initialBeer = beer.filter(d=>d.country_name === "United States").map(d=>d.beer_consumption);
    
    let initialTrace1 = {
        x: initialYears,
        y: initialHappiness,
        type: 'scatter',
        name: 'Happiness Index'
      };

    let initialTrace2 = {
        x: initialYears,
        y: initialWine,
        type: 'scatter',
        name: 'Wine Consumption',
        yaxis: "y2"
      };

    let initialTrace3 = {
        x: initialYears,
        y: initialSpirits,
        type: 'scatter',
        name: 'Spirits Consumption',
        yaxis: "y2"
      };
    
    let initialTrace4 = {
        x: initialYears,
        y: initialBeer,
        type: 'scatter',
        name: 'Beer Consumption',
        yaxis: "y2"
      };
      
    let initialData = [initialTrace1, initialTrace2, initialTrace3, initialTrace4];

    var initialLayout = {
        title: 'United States Happiness vs. Alcohol Consumption',
        yaxis: {title: 'Happiness Index (10 pt scale)'},
        yaxis2: {
          title: 'Alcohol L/person',
          titlefont: {color: 'rgb(0,0,0)',size:12},
          tickfont: {color: 'rgb(0,0,0)'},
          overlaying: 'y',
          side: 'right'
        },
      };
      
    Plotly.newPlot('worldHappiness', initialData,initialLayout);

    worldHappiness.on('plotly_relayout',
    function(eventdata){
    });
}))
)    
)
};

init1();

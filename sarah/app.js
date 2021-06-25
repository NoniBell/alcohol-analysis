function optionChanged(){

    //Get input value from drop down
    let country = d3.select("#selDataset0").node().value;
    console.log(country)
    //build plot with new data
    buildPlot(country);
};

function buildPlot(country){
    d3.csv("happiness.csv").then(function(data){
        let filteredData = data.filter(d => d.country_name === country);
        //console.log(filteredData);
        let happiness = filteredData.map(d=>d.life_ladder);
        let years = filteredData.map(d=>d.year);
        //console.log(happiness);
        //console.log(years);
        
        let trace1 = {
            x: years,
            y: happiness,
            type: 'scatter',
            name: 'Happiness Index'
          };
          
        let data1 = [trace1];

        let layout = {
            title: `${country} Happiness Index`,
            yaxis:{
                title: "Happiness Index (out of 10)"
            }
        }
          
        Plotly.newPlot('MyDiv1', data1,layout);
    })
}


//load in initial happiness data
function init(){
    //read data
    d3.csv("happiness.csv").then((countries)=>{

    //build dropdownMenu with initial page being United States
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
    let selector = d3.select("#selDataset0");
    selector.append("option").text("United States");
    unique_countries.forEach((i)=>{
        let option = selector.append("option");
        option.text(i);
    });
    let initialFilteredData = countries.filter(d => d.country_name === "United States");
    let initialHappiness = initialFilteredData.map(d=>d.life_ladder);
    let initialYears = initialFilteredData.map(d=>d.year);
    let initialTrace = {
        x: initialYears,
        y: initialHappiness,
        type: 'scatter',
        name: 'Happiness Index'
      };
      
    let initialData = [initialTrace];

    let initialLayout = {
        title: "United States Happiness Index",
        yaxis:{
            title: "Happiness Index (out of 10)"
        }
    }
      
    Plotly.newPlot('MyDiv1', initialData,initialLayout);
});
};

init();
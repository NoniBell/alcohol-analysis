function buildPlot(){
    d3.csv("cleaned_sales.csv").then(function(data){
        console.log(data);
        // let filteredData = data.samples.filter(d => d.id === bio);
        // let sample_values = filteredData[0].sample_values.sort(function(a,b){return b-a});
        // let otu_ids = filteredData[0].otu_ids;
        // let otu_labels = filteredData[0].otu_labels;
        // //build horizontal bar chart
        // let trace1 = {
        //     y: otu_ids.toString(),
        //     x: sample_values.slice(0,10),
        //     marker: otu_ids.slice(0,10),
        //     text: otu_labels,
        //     orientation:'h',
        //     type:"bar"
        // };
        // let data1 = [trace1];
        // let ticker = otu_ids.map(d=>d);
        // let layout = {
        //     title: "Top 10 Bacteria Cultures Found",
        //     yaxis: {
        //         title: "OTU",
        //         autorange: 'reversed',
        //         tickmode: "array", // If "array", the placement of the ticks is set via `tickvals` and the tick text is `ticktext`.
        //         tickvals: [0,1,2,3,4,5,6,7,8,9],
        //         ticktext: ticker
        //         }
        //     }
        // Plotly.newPlot('bar', data1, layout);
    })
}

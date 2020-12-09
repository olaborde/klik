
// var review_rating = []
// var review_date = []

// function addReview_rating(){
//   let thetable=document.getElementById("mytab1").getElementsByTagName('tbody')[0];  
//   for (let therow of thetable.rows) {
//     review_rating.push(therow.cells[1].innerText);
// }

// }

// function addReview_date(){
//   let thetable=document.getElementById("mytab1").getElementsByTagName('tbody')[0];  
//   for (let therow of thetable.rows) {
//     review_date.push(therow.cells[3].innerText);
// }

// }
// addReview_rating()
// addReview_date()

// console.log(review_date)
// console.log(review_rating)

// document.getElementById("button002").addEventListener("click", function(){
// });
// var table = document.getElementById("mytab1");
// for (var i = 0, row; row = table.rows[i]; i++) {
//    //iterate through rows
//    console.log(row)
//    //rows would be accessed using the "row" variable assigned in the for loop
//    for (var j = 0, col; col = row.cells[j]; j++) {
//      //iterate through columns
//      //columns would be accessed using the "col" variable assigned in the for loop
//    }  
// }



console.log("Hello from shape.js")

var dataArray = [5, 11, 18, 45, 60];

// var svg = d3.select("body").append("svg").attr("height", "100%").attr("width", "100%")
// height = function(d, i){ return d * 15; }
// var x = function(d, i){ return 60 * i; }
// var y = function(d, i){ return 300 - (d*15); }

// svg.selectAll("rect")
//     .data(dataArray)
//     .enter().append("rect")
//         .attr("height", height)
//         .attr("width", "50")
//         .attr("fill", "orange")
//         .attr("x", x)
//         .attr("y", y)



// new

var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    datasets: [{
      data: [15339, 21345, 18483, 24003, 23489, 24092, 12034],
      lineTension: 0,
      backgroundColor: 'transparent',
      borderColor: '#007bff',
      borderWidth: 4,
      pointBackgroundColor: '#007bff'
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: false
        }
      }]
    },
    legend: {
      display: false,
    }
  }
});




















// Old


// var bardata = [];
//     for (var i = 0; i<50; i++) {
//       bardata.push(Math.random() * 30);
//     }
// var height = 400,
//     width = 600,
//     barWidth = 50,
//     barOffset = 5,
//     tempColor;

// var yScale = d3.scaleLinear()
//     .domain([0, d3.max(bardata)])
//     .range([0,height]);

// var xScale = d3.scaleBand()
//     .domain(bardata)
//     .paddingInner(.3)
//     .paddingOuter(.1)
//     .range([0, width])

// var colors = d3.scaleLinear()
//     .domain([0, bardata.length *.33,
//                 bardata.length *.66,
//                 bardata.length
//                 ])
//     .range(['#B58929', '#C61C6F',
//             '#268BD2', '#85992C'])

// var tooltip = d3.select('body')
//                 .append('div')
//                 .style('position', 'absolute')
//                 .style('padding', '0 10px')
//                 .style('background', 'white')
//                 .style('opacity', 0);
// var ctx = document.getElementById("myChart");                

// var myChart = 
// d3.select(ctx).append('svg')
//   .attr('width', width)
//   .attr('height', height)
// .selectAll('rect').data(bardata)
//   .enter().append('rect')
//     .attr('fill', function(d, i) {
//       return colors(i)
//     })
//     .attr('width', function(d) {
//       return xScale.bandwidth();
//     })
//     .attr('height', 0)
//     .attr('x', function(d) {
//       return xScale(d);
//     })
//     .attr('y', height)
    
//     .on('mouseover', function(d) {

//       tooltip.transition().duration(200)
//         .style('opacity', .9)

//       tooltip.html(d)
//         .style('left', (d3.event.pageX -35) + 'px')
//         .style('top', (d3.event.pageY -30) + 'px')

//       tempColor = this.style.fill;
//       d3.select(this)
//         .style('fill', 'yellow')
//     })

//     .on('mouseout', function(d) {
//       d3.select(this)
//         .style('fill', tempColor)
//     });


// myChart.transition()
//   .attr('height', function(d) {
//     return yScale(d);
//   })
//   .attr('y', function(d) {
//     return height - yScale(d);
//   })
//   .delay(function(d, i) {
//     return i * 20;
//   })
//   .duration(1000)
//   .ease(d3.easeBounceOut)
let data = null;
let attributeX = "budget";
let attributeY = "revenue";
let width = window.innerWidth;
let height = window.innerHeight;
let margin = { top: 10, right: 30, bottom: 10, left: 10 };

console.log(width, height);

d3.csv("csv/cars.csv", d3.autoType).then(function (iris) {
    data = iris;
    drawParaCoords();
});

function drawParaCoords() {
    const svg = d3.select("body").append("svg").attr("viewBox", [0, 0, width, height]);

    let attributes = data.columns.filter(d => d !== "name");
    console.log(attributes);

    let color = d3
        .scaleOrdinal()
        .domain(data.map(d => d.origin))
        .range(d3.schemeCategory10);

    let y = new Map();

    // quantitative attributes
    attributes
        .filter(d => d !== "name" && d !== "origin")
        .forEach(function (attribute) {
            y.set(
                attribute,
                d3.scaleLinear(d3.extent(data, d => d[attribute]), [
                    height - margin.bottom,
                    margin.top
                ])
            );
        });

    // ordinal and categorical attributes
    attributes
        .filter(d => d === "origin")
        .forEach(function (attribute) {
            y.set(
                attribute,
                d3
                    .scalePoint()
                    .domain(data.map(d => d[attribute]).sort())
                    .range([height - margin.bottom, margin.top])
            );
        });

    let x = d3.scalePoint(attributes, [margin.left, width - margin.right]);

    // set the style of hidden data items
    svg
        .append("style")
        .text("path.hidden { stroke: #000; stroke-opacity: 0.01;}");

    // a map that holds any active brush per attribute
    let activeBrushes = new Map();

    const polylines = svg
        .append("g")
        .attr("fill", "none")
        .attr("stroke-width", 1.5)
        .selectAll("path")
        .data(data)
        .join("path")
        .attr("stroke", d => color(d.origin))
        .attr("stroke-width", 1)
        .attr("stroke-opacity", 0.4)
        .attr("d", d =>
            d3
                .line()
                .defined(([, value]) => value != null)
                .x(([attribute]) => x(attribute))
                .y(([attribute, value]) => y.get(attribute)(value))(
                    d3.cross(attributes, [d], (attribute, d) => [attribute, d[attribute]])
                )
        );

    // create the group nodes for the axes
    const axes = svg
        .append("g")
        .selectAll("g")
        .data(attributes)
        .join("g")
        .attr("transform", d => `translate(${x(d)},0)`);

    // add the visual representation of the axes
    axes
        .append("g")
        .each(function (d) {
            d3.select(this).call(d3.axisRight(y.get(d)));
        })
        .call(g =>
            g
                .append("text")
                .attr("x", margin.left)
                .attr("y", -6)
                .attr("text-anchor", "start")
                .attr("fill", "currentColor")
                .text(d => d)
        )
        .call(g =>
            g
                .selectAll("text")
                .clone(true)
                .lower()
                .attr("fill", "none")
                .attr("stroke-width", 5)
                .attr("stroke-linejoin", "round")
                .attr("stroke", "white")
        );
}
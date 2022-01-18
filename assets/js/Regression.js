//experimental data
var rawData = [
    [0.1, 2.1],
    [1, 2.4],
    [2, 2.6],
    [4, 2.8],
    [5, 3]
];

//getting the regression object
//the type of regression depends on the experimental data
var result = regression('linear', rawData);

//get coefficients from the calculated formula
var coeff = result.equation;

anychart.onDocumentReady(function () {

    var data_1 = rawData;
    var data_2 = setTheoryData(rawData);

    chart = anychart.scatter();

    chart.title("The calculated formula: " + result.string + "\nThe coefficient of determination (R2): " + result.r2.toPrecision(2));

    chart.legend(true);

    // creating the first series (marker) and setting the experimental data
    var series1 = chart.marker(data_1);
    series1.name("Experimental data");

    // creating the second series (line) and setting the theoretical data
    var series2 = chart.line(data_2);
    series2.name("Theoretically calculated data");
    series2.markers(true);

    chart.container("container");
    chart.draw();
});

//input X and calculate Y using the formula found
//this works with all types of regression
function formula(coeff, x) {
    var result = null;
    for (var i = 0, j = coeff.length - 1; i < coeff.length; i++, j--) {
        result += coeff[i] * Math.pow(x, j);
    }
    return result;
}

//setting theoretical data array of [X][Y] using experimental X coordinates
//this works with all types of regression
function setTheoryData(rawData) {
    var theoryData = [];
    for (var i = 0; i < rawData.length; i++) {
        theoryData[i] = [rawData[i][0], formula(coeff, rawData[i][0])];
    }
    return theoryData;
}
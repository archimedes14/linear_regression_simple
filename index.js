var smr = require('smr');
var regression = new smr.Regression({ numX: 2, numY: 1 })

var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('data.txt')
});

lineReader.on('line', function (line) {
	line = line.split(',')
	regression.push({x:[line[0],line[1]], y:[line[2]]})
	t = regression.calculateCoefficients()
	console.log(t)
});



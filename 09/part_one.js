const readFile = require('fs').readFileSync;

class Point{
    constructor(x,y){
        this.x = x;
        this.y = y;
    }
    distance(other){
        return (Math.abs(this.x - other.x) + 1) * (1 + Math.abs(this.y - other.y))
    }
    toString(){
        return `${this.x},${this.y}`
    }
}

function biggestRectNaive(redTiles) {
    let maxDist = 0;
    for( let i = 0; i < redTiles.length; i++ ) {
        for( let j = i + 1; j < redTiles.length; j++ ) {
            maxDist = Math.max(maxDist, redTiles[i].distance(redTiles[j]));
        }
    }
    return maxDist;
}

const redTiles = readFile(__dirname + '/input.txt', 'utf-8')
    .trim()
    .split('\n')
    .map(line => {
        const [x,y] = line.split(',');
        return new Point(parseInt(x),parseInt(y))
    })
console.log(biggestRectNaive(redTiles));
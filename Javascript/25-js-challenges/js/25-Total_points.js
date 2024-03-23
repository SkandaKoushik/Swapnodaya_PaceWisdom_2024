function points(games) {
    let s = 0;
    games.forEach(function(score) {
        const [x, y] = score.split(':').map(Number);
        if(x>y) s += 3;
        else if (x === y) s += 1;
        else s += 0;
    });
    return s;
}


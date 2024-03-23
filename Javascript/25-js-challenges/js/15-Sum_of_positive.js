function positiveSum(arr) {
    let sum = 0;
    arr.forEach(function(i) {
        if(i > 0) sum += i;
    });
    return sum;
}


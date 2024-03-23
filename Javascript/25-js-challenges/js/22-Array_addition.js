function arrayPlusArray(arr1, arr2) {
    let arr = [...arr1, ...arr2];
    let sum = 0;
    arr.forEach(v => sum += v);
    return sum;
}


function arrayPlusArray(arr1, arr2) {
    const arr = arr1.concat(arr2);
    return arr.reduce((acc, cur) => acc + cur);
}


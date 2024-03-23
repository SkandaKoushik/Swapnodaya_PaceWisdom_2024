function getCount(str) {
    const vowelReg = /[aeiou]/g;
    const match = str.match(vowelReg);
    return match ? match.length : 0;
}


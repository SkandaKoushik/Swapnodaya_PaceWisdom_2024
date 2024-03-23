function clr() {
    let x = document.getElementById('result').value = '';
}

function display(val) {
    document.getElementById('result').value += val;
}

function equate() {
    let x = document.getElementById('result');
    let y = eval(x.value);
    x.value = y;
}
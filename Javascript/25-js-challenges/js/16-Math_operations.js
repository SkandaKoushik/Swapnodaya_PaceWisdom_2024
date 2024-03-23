function basicOp(op, v1, v2){
    switch(op) {
        case '+': return v1 + v2;
        case '-': return v1 - v2;
        case '*': return v1 * v2;
        case '/': 
            if(v2 === 0) return 'Error';
            return v1 / v2;
    }
}


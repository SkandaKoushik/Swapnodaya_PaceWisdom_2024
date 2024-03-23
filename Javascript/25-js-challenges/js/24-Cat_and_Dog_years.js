var humanYearsCatYearsDogYears = function(humanYears) {
    let cat = 0, dog = 0;
    
    for(let i=1; i <= humanYears; i++) {
        if(i === 1) {
            cat += 15;
            dog += 15;
        }
        else if(i === 2) {
            cat += 9;
            dog += 9;
        }
        else {
            cat += 4;
            dog += 5;
        }
    }
    return [humanYears, cat, dog];
  }
  
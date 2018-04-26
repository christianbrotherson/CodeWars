toWeirdCase = (s) => {
    return s.split(' ').map(function (word) {
        return word.split('').map(function (letter, index) {
            return index % 2 == 0 ? letter.toUpperCase() : letter.toLowerCase()
        }).join('');
    }).join(' ');
}

console.log(toWeirdCase("Hello there"));

toWeirdCase = s => {
    a = s.split(' ')
    c = []
    d = []
    e = []
    for (i in a) {
        b = a[i].split('')
        for (x in b) {
            if (x % 2 == 0) {
                c.push(b[x].toUpperCase())
            } else {
                c.push(b[x].toLowerCase())
            }
        }

        d.push(c)
        e.push(d[0].join(''))
        c = []
        d = []
    }
    return e.join(' ')
}

console.log(toWeirdCase('Hello THERE')); 
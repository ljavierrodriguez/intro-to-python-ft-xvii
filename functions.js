/* 

function nombreFuncion(){
    sentences
}

const nombreFuncion = function(){
    sentences
}

*/

function suma(a, b){
    return a + b;
}

const _suma = function(a, b){
    return a + b;
}

suma(10, 10)


let notas = [1, 2, 3, 4, 5];

let resultado = notas.map(function(nota){
    return nota * nota;
})

console.log(resultado);

let resultado2 = [...notas]
resultado2.sort((a, b) => a > b ? -1 : 1)
console.log(resultado2)

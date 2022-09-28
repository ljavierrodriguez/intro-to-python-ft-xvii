/* 

if (condition) {
    sentences
}

if (condition) {
    sentences
} else {
    sentences
}

if (condition) {
    sentences
} else if (condition) {
    sentences
} else {
    sentences
}

and => &&
or => ||
not => !
 
*/
let a = 5;
let b = 10;
let c = 6;

if (a === b) {
    console.log(a === b)
}

if (a > b) {
    console.log("Verdadero")
} else {
    console.log("Falso")
}

if (a > b && a > c){
    console.log("A es mayor")
} else if (b > c){
    console.log("B es mayor")
} else {
    console.log("C es mayor")
}
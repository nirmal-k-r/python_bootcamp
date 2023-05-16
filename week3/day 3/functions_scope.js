

//var age=10; //global variable

let age=10; //global variable

function info(){
    var name="John"; //local variable
    console.log(age);
    console.log(name);
}

info();

console.log(name);



paid=true;
if (paid==true){
    //let price=100; //local variable to the block of code
    var price=100;// global and accessible outside the block
    console.log(price);
}

console.log(price);



const pi=3.145; //constant which is readonly
// pi=5;

console.log(pi);


var name="Nirmal";

//console.log("Hello "+name+" You are "+age+" years old");
console.log(`Hello ${name}. You are ${age} years old`); 

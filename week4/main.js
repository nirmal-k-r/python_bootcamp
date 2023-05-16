
function menu(){ //function definition
    console.log(" 1. Play the game");
    console.log(" 2. View scores");
    console.log(" 3. Exit");
}

menu(); //function call

function add(a,b){ //a and b are called function parameters
    var c=a+b;
    return c;
}

var c= add(10,20); //10 and 20 are function arguments
console.log(c);


console.log(add(40,50));


function display_names(names){
    for (name of names){
        console.log(name);
    }
}

my_names=["John","Mary","Joe","Jane"];
display_names(my_names);

my_names.push("Nirmal");
display_names(my_names);


console.log(Math.sqrt(4));

//default values

function born(name, gender, age=0){
    console.log(`${name} is ${age} years old and is ${gender}`);
}


born("John");


person={
    name: "John",
    age: 20,
    gender: "male",
    born: born, //object method
    details: function(){
        console.log(`${this.name} is ${this.age} years old and is ${this.gender}`);
    }

}

person.born(person.name,person.gender,person.age);

person.details()


function displayMessage(){
    console.log("this is a test");
    alert("this is a test");
    confirm("Play?");
}
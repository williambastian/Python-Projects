// javascript file for project 10//

//example of a while loop
function Call_Loop(){
    var Digit = "";
    var X = 1;
    while (X < 11) {
        Digit += "<br>" + X;
        X++;
    }
    document.getElementById("Loop").innerHTML = Digit;
}

//example of .length
function showLength(){
    var text = "What is the length of this text string?";
    var Len = text.length;
    document.getElementById("Length").innerHTML = Len;
}

//example of for loop
var Toppings = ["Mozzarella", "Parmesan", "Basil", "Classic Red Sauce", "Pepperoni", "Sausage", "Mushroom", "Onion", "Sweet Peppers", "Hot Peppers", "Anchovy", "Olives", "Canadian Bacon", "Pineapple"];
var Content = "";
var Y;
function forLoop(){
    for (Y = 0; Y < Toppings.length; Y++){
        Content += Toppings[Y] + "<br>";
    }
    document.getElementById("ListID").innerHTML = Content;
}

//function that uses an array
function arrayFunction(){
    var WeatherType = [];
    WeatherType[0] = "sunny";
    WeatherType[1] = "rainy";
    WeatherType[2] = "cloudy";
    WeatherType[3] = "windy";
    WeatherType[4] = "snowy";
    document.getElementById("Array").innerHTML = "In Texas, the weather is currently " + WeatherType[0] + ".";
}

//using const
function constantFunction(){
    const Vehicle = {type:"sedan", make:"Honda", model:"Civic"};
    Vehicle.model = "Accord";
    Vehicle.color = "blue";
    document.getElementById("Constant").innerHTML = "This " +Vehicle.color + " " + Vehicle.type + " is a " + Vehicle.make + " " + Vehicle.model + ".";
}

//using let
function letFunction(){
    let printValue = "Variables declared with let cannot be redeclared, must be declared before use, and have block scope."
    document.getElementById("letID").innerHTML = printValue;
}
//printValue cannot be used outside this block

//using return
var returnX = returnFunction(4, 4);
document.getElementById("returnID").innerHTML = returnX;
function returnFunction(a, b){
    return a * b;
}

//using an object method
let cakeType = {
    size: "three layer ",
    flavorPrefix: "dark ",
    flavor: "chocolate ",
    flavorSuffix: "mousse ",
    cakeFormat: "cake ",
    description : function() {
        return "The dessert is a " + this.size + this.flavorPrefix + this.flavor + this.flavorSuffix + this.cakeFormat;
        }
    
    };
    
document.getElementById("objMethod").innerHTML = cakeType.description();

//using break
let text = "";
for (let i = 0; i < 10; i++) {
    if (i === 3) { break; }
    text += "The number is " + i + "<br>";
}

document.getElementById("breakID").innerHTML = text;

//using continue
let textContinue = "";
for (let i = 0; i < 10; i++) {
    if (i === 3) { continue; }
    textContinue += "The number is " + i + "<br>";
}

document.getElementById("continueID").innerHTML = textContinue;

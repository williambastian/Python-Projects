// js file for project 6 //

//example of function containing ternary operator, using input from browser
function VoteFunction(){
    var Height, canRide;
    Height = document.getElementById("Age").value;
    canRide = (Height < 18) ? "You are not eligible":"You are eligible";
    document.getElementById("Vote").innerHTML = canRide + " to vote.";
}

function Vehicle(Make, Model, Year, Color) {
    this.Vehicle_Make = Make;
    this.Vehicle_Model = Model;
    this.Vehicle_Year = Year;
    this.Vehicle_Color = Color;
}
var Jack = new Vehicle("Dodge", "Viper", 2020, "Red");
var Emily = new Vehicle("Jeep", "Trail Hawk", 2019, "White and Black");
var Erik = new Vehicle("Ford", "Pinto", 1971, "Mustard");
function myFunction(){
    document.getElementById("Keywords_and_Constructors").innerHTML = ("Erik drives a " + Erik.Vehicle_Color + "-colored " + Erik.Vehicle_Model + " manufactured in " + Erik.Vehicle_Year);
}

//Object constructor function for Cat, uses "this" keyword//
function Cat(Color, Breed, Weight){
    this.Cat_Color = Color;
    this.Cat_Breed = Breed;
    this.Cat_Weight = Weight;
}

//use of "new" keyword to create Cat "Jinx"//
//output of catFunction() displays in element with id "New_and_This"
var Jinx = new Cat("Black", "Domestic Short Hair", "9 lbs");
function catFunction(){
    document.getElementById("New_and_This").innerHTML = "Jinx is a " + Jinx.Cat_Color + " " + Jinx.Cat_Breed + " who weighs " + Jinx.Cat_Weight + ".";
}

//test variable with reserved word. Returns "unexpected token" error
//var test = switch;
//document.write(test);

//example of nested function: minusOne() is nested within countBackwards()
function nestFunction(){
    document.getElementById("Nested_Function").innerHTML = countBackwards();
    function countBackwards(){
        var numStart = 10;
        function minusOne() {numStart -= 1;}
        minusOne();
        return numStart;
    }
}
// js file for project7//

//global variable X //
var x = 100;
function addNum1(){
    document.getElementById("Add1").innerHTML=(x+25);
}
function addNum2(){
    document.getElementById("Add2").innerHTML=(x+200);
}

//addNum3() uses a local variable, y
function addNum3(){
    var y = 100
    document.getElementById("Add3").innerHTML=(y+200);
}

//function illustrating improper use of local variable [ y is not defined within addNum4(), and returns error in the console ]
function addNum4(){
    document.getElementById("Add4").innerHTML=console.log(y+100);
}

function get_Date(){
    if (new Date().getHours() < 18) {
        document.getElementById("Greeting").innerHTML = "How are you today?";
    }
}

function ifCheck(){
    if (10 > 9){
        document.getElementById("CheckIf").innerHTML = "10 > 9";
    }
}

//functions with "if," "else," and "elseif" statements//
function ageToRent(){
    Age = document.getElementById("rentAge").value;
    if (Age >= 25){
        CarRental = "You are old enough to rent a car.";
    }
    else {
        CarRental = "You are not old enough to rent a car.";
    }
    document.getElementById("ageAnswer").innerHTML = CarRental;
}

//Time function//
function TimeFunction(){
    var Time = new Date().getHours();
    var Reply;
    if (Time < 12 == Time > 0) {
        Reply = "It is morning.";
    }
    else if (Time >= 12 == Time < 18) {
        Reply = "It is afternoon.";
    }
    else {
        Reply = "It is evening.";
    }
    document.getElementById("todayTime").innerHTML = Reply;
}
//javascript for project 3//

//This function adds two numbers, x & y, and returns the sum in the HTML element with id "Math"//
function addNumbers(x, y) {
    document.getElementById("Math").innerHTML=(x+y);
}

//returns difference of numbers x - y in HMTL element with id "Subtract"//
function subtractNumbers(x, y) {
    document.getElementById("Subtract").innerHTML=(x-y);
}


//returns product of numbers x * y in HTML element with id "Multiply"//
function multiplyNumbers(x, y) {
    document.getElementById("Multiply").innerHTML=(x*y);
}

//returns quotient of x / y in HTML element with id "Divide"//
function divideNumbers(x, y){
    document.getElementById("Divide").innerHTML=(x/y);
}

//returns value of given equation, which includes various math operators, in HTML element with id "MoreMath"//
function multipleMathOps(){
    var multiMath = (3+4) * 5 / 2-3;
    document.getElementById("MoreMath").innerHTML = "3 plus 4, multiplied by 5, divided by 2 and then subtracted by 3 equals " + multiMath;
}

//returns remainder of 27 / 5 using modulus operator, in HTML elements with id "Modulus"//
function modulusNum(){
    var modulusRemainder = 27 % 5;
    document.getElementById("Modulus").innerHTML = "27 divided by 5 gives a remainder of " + modulusRemainder;

}

//Illustrates negation of variable using the minus sign [ - ]. Returns negative value of z in HTML element with id "UnaryNegate"//
function numNegate(){
    var z = 12;
    document.getElementById("UnaryNegate").innerHTML = -z;
}

//Illustrates increment operator [ ++ ]//
function incrementNum(){
    var startNum = 17;
    startNum++;
    document.getElementById("Increment").innerHTML = startNum;
}

//Illustrates decrement operator [--]//
function decrementNum(){
    var minusOne = 99;
    minusOne--;
    document.getElementById("Decrement").innerHTML = minusOne;
}

//Illustrates Math.random method; generates random number between 0 and 100.//
function randomNum(){
    document.getElementById("Random").innerHTML = (Math.random()*100);
}

//Illustrates one example of Math object and another Math object method (cube root)//
function cubeRoot(){
    document.getElementById("CubeRoot").innerHTML = (Math.cbrt(27));
}
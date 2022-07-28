// javascript file for project5 //

function showTypeOf(){
    //document.write(typeof "Text");//
    document.getElementById("TypeOf").innerHTML=(typeof "Text");
}

function typeCoerce(){
    //document.write("100"+1); statement contains type coercion with string and numeric data//
    document.getElementById("Coerce").innerHTML=("100" + 1);
}

function NaN_one(){
    document.getElementById("NaN1").innerHTML= 0/0;
}

function NaN_two(){
    document.getElementById("NaN2").innerHTML = isNaN('This is a string');
}

function NaN_three(){
    document.getElementById("NaN3").innerHTML = isNaN(7);
}

function posInfin(){
    document.getElementById("plusInfinity").innerHTML = (3E310);
}

function minInfin(){
    document.getElementById("minusInfinity").innerHTML = (-3E310);
}

function boolTrue(){
    document.getElementById("trueBool").innerHTML = (10 > 3);
}

function boolFalse(){
    document.getElementById("falseBool").innerHTML = (10 < 3);
}

function checkLog(){
    document.getElementById("consoleLogCheck").innerHTML = console.log(2 +3);
}

function boolConsole(){
    document.getElementById("consoleLogBool").innerHTML = console.log(10 < 3);
}

//This code utilizes [ == ] //
function boolEqualTrue(){
    document.getElementById("DoubleEqual").innerHTML = console.log(10 == 10);
}

function boolEqualFalse(){
    document.getElementById("falseDoubleEqual").innerHTML = console.log(10 == 11);
}

//This code utilizes [ === ] // 
function typeValueTrue(){
    document.getElementById("tripleEqualTrue").innerHTML = console.log(10===10);
}

function typeValueFalse(){
    document.getElementById("falseTypeValue").innerHTML = console.log(10==="1");
}

function typeFalse(){
    document.getElementById("falseType").innerHTML = console.log(10==="10");
}

function valueFalse(){
    document.getElementById("falseValue").innerHTML = console.log(10===1);
}

function andOperator(){
    document.getElementById("boolAnd").innerHTML = (10 > 9 && 19 > 8);
}

//This code utilizes [ > ], [ && ], [ || ], [ ! ], and [ < ] //
function andOperatorFalse(){
    document.getElementById("boolAndFalse").innerHTML = (10 > 9 && 19 < 8);
}

function orOperator(){
    document.getElementById("boolOr").innerHTML = (10 > 9 || 19 < 8);
}

function orOperatorFalse(){
    document.getElementById("boolOrFalse").innerHTML = (10 < 9 || 19 < 8);
}

function notOperator(){
    document.getElementById("boolNot").innerHTML = !(10 < 9);
}

function notOperatorFalse(){
    document.getElementById("boolNotFalse").innerHTML = !(10 > 9);
}
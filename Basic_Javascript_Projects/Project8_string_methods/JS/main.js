// main js file for project 8//

//concatenating strings with .concat() method
function concatFunction(){
    var part1 = "This is ";
    var part2 = "a concatenated ";
    var part3 = "phrase. It was made up of three separate strings.";
    var allParts = part1.concat(part2, part3);
    document.getElementById("concatOne").innerHTML = allParts;
}

//slice and concatenate methods used together, taking letters from initial string and re-concatenating them into second string
function sliceFunction(){
    var Sentence = "I see you quiver with anticip-"
    var Section1 = Sentence.slice(29, 30);
    var Section2 = Sentence.slice(28, 29);
    var Section3 = Sentence.slice(22, 23);
    var Section4 = Sentence.slice(24, 25);
    var Section5 = Sentence.slice(25, 26);
    var Section6 = Sentence.slice(7, 8);
    var Section7 = "n";
    var Section = Section1.concat(Section2, Section3, Section4, Section5, Section6, Section7);
    document.getElementById("sliceOne").innerHTML = Section;
}

//example  of .toUpperCase() returning all-caps string
function toUpperFunction(){
    var sample1 = "click to use toUpperCase()";
    var sample2 = sample1.toUpperCase();
    document.getElementById("upperString").innerHTML = sample2;
}

// example of .search() returning specified index value of character in string
function searchFunction(){
    var text = "Search Test";
    var indexResult = text.search("Test");
    document.getElementById("textSearch").innerHTML = indexResult;
}

//example of .toString() returning number input as string output
function numStringFunction(){
    var numVar = 600;
    var numString = numVar.toString();
    document.getElementById("NumString").innerHTML = numString;
}

//example of .toPrecision truncating number value to specified number of significant digits
function precisionFunction(){
    var X = 3.3333333;
    var X4 = X.toPrecision(4);
    document.getElementById("precision").innerHTML = X4;
}

//example of rounding number to specified digit and converting to string output with .toFixed()
function toFixedFunction(){
    var Y = 7.89;
    var Y2 = Y.toFixed(1);
    document.getElementById("fixedRound").innerHTML = Y2;
}

//using .valueOf() to return primitive value of input
function primitiveValue(){
    var Z = 99;
    var Z2 = Z.valueOf();
    document.getElementById("primitive").innerHTML = Z2;
    console.log(Z);
    console.log(Z2);
}
//the addNumbers functions uses two variables, getElementByID, and returns the sum of those two variables within the paragraph element with id "demo"//
function addNumbers(x, y) {
    document.getElementById("demo").innerHTML=(x+y);
    
}
//the concatFunction function uses += to concatenate two strings and print them within the paragraph element with id "Concatenate"//

function concatFunction() {
    var sentence = "I am learning";
    sentence += " a lot from this course.";
    document.getElementById("Concatenate").innerHTML = sentence;
}

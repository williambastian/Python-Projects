//launches modal slide view
function openModal() {
    document.getElementById("myModal").style.display = "block";
}
//closes modal slide view
function closeModal() {
    document.getElementById("myModal").style.display = "none";
}
//assigns index to slides to allow us to iterate through each one in sequence
var slideIndex = 1;
showSlides(slideIndex);

//function to move to next highest slide index, and show the image assigned to that index
function plusSlides(n) {
    showSlides(slideIndex += n);
}

//sets current slide index 
function currentSlide(n) {
    showSlides(slideIndex = n);
}

//functionality for progressing through slides
function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("demo");
    var captionText = document.getElementById("caption");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace("active", "");
    }
    slides[slideIndex-1].style.display="block";
    dots[slideIndex-1].className += "active";
    captionText.innerHTML = dots[slideIndex-1].alt;
}
//validates that text is entered
function validateForm() {
    let x = document.forms["myForm"] 
    ["phoneNum"].value;
        if (x =="") {
            alert("Please enter a valid phone number");
            return false;
        }
}
//opens popup version of contact
function openForm() {
    document.getElementById("popForm").style.display="block";
}
//closes popup version of contact
function closeForm() {
    document.getElementById("popForm").style.display="none";
}
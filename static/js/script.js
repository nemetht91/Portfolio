

/* Navbar */
var toggle = document.querySelector(".toggle");
var navbar = document.querySelector(".nav");
var showcase = document.querySelector(".showcase");
var mainTitle = document.querySelector(".showcase h1");
var subTitle = document.querySelector(".showcase h2");


toggle.addEventListener("click", () => {
    navbar.classList.toggle("hidden");

    mainTitle.classList.toggle("shifted-left");
    subTitle.classList.toggle("shifted-right");

});
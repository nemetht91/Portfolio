

/* Navbar */
var toggle = document.querySelector(".toggle");
var navbar = document.querySelector(".nav");
var showcase = document.querySelector(".showcase");
var mainTitle = document.querySelector(".showcase h1");
var subTitle = document.querySelector(".showcase h2");
var contactTitle = document.querySelector(".contact h1");
var contacts = document.querySelector(".contact .info");


toggle.addEventListener("click", () => {
    navbar.classList.toggle("hidden");
    toggle.classList.toggle("closed");
    if(window.location.href.match('index.html') != null || window.location.href.match('index') != null){
        mainTitle.classList.toggle("shifted-up");
        subTitle.classList.toggle("shifted-down");
    }
    if(window.location.href.match('contact.html') != null || window.location.href.match('contact') != null){
        contactTitle.classList.toggle("shifted-up");
        contacts.classList.toggle("shifted-down");
       
    }
});
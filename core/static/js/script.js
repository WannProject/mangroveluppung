// DOM Elements
const header = document.querySelector("header");
const menu = document.querySelector("#menu-icon");
const navbar = document.querySelector(".navbar");
const scrollContainer = document.getElementById("testimonials-scroll");
const scrollLeftBtn = document.getElementById("scroll-left");
const scrollRightBtn = document.getElementById("scroll-right");
// Get the modal
var modal = document.getElementById("imageModal");

// Get the image and insert it inside the modal
var modalImg = document.getElementById("modalImage");
var captionText = document.getElementById("caption");
var images = document.querySelectorAll(".popup-image");

// Variables
let autoScrollInterval;

// Functions
function toggleSticky() {
  header.classList.toggle("sticky", window.scrollY > 0);
}

function toggleMenu() {
  menu.classList.toggle("bx-x");
  navbar.classList.toggle("open");
}

function closeMenu() {
  menu.classList.remove("bx-x");
  navbar.classList.remove("open");
}

function autoScroll() {
  if (
    scrollContainer.scrollLeft >=
    scrollContainer.scrollWidth - scrollContainer.clientWidth
  ) {
    scrollContainer.scrollTo({ left: 0, behavior: "smooth" });
  } else {
    scrollContainer.scrollBy({ left: 320, behavior: "smooth" });
  }
}

function startAutoScroll() {
  autoScrollInterval = setInterval(autoScroll, 5000);
}

function resetAutoScroll() {
  clearInterval(autoScrollInterval);
  startAutoScroll();
}

function scrollLeft() {
  scrollContainer.scrollBy({ left: -320, behavior: "smooth" });
  resetAutoScroll();
}

function scrollRight() {
  scrollContainer.scrollBy({ left: 320, behavior: "smooth" });
  resetAutoScroll();
}

// Event Listeners
window.addEventListener("scroll", toggleSticky);
menu.addEventListener("click", toggleMenu);
window.addEventListener("scroll", closeMenu);
scrollLeftBtn.addEventListener("click", scrollLeft);
scrollRightBtn.addEventListener("click", scrollRight);
scrollContainer.addEventListener("mouseenter", () =>
  clearInterval(autoScrollInterval)
);
scrollContainer.addEventListener("mouseleave", startAutoScroll);

// Initialize
startAutoScroll();

images.forEach(function (image) {
  image.onclick = function () {
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
  };
});

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
  modal.style.display = "none";
};

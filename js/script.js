// ===================== toggle icon navbar ===================================
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('header nav a');


menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
};

// ===================== scroll sections active link ===================================
let sections = document.querySelectorAll("section");
let navLinks = document.querySelectorAll("header nav a");

window.onscroll = () => {
  sections.forEach((section) => {
    let top = window.scrollY;
    let offset = section.offsetTop - 150;
    let height = section.offsetHeight;
    let id = section.getAttribute("id");

    if (top >= offset && top < offset + height) {
      navLinks.forEach((links) => {
        links.classList.remove("active");
        document
          .querySelector("header nav a[href*=" + id + "]")
          .classList.add("active");
      });
    }
  });
  // ===================== sticky navbar ===================================

  let header = document.querySelector("header");
  header.classList.toggle("sticky", window.scrollY > 100);

  // ===================== remove toggle icon and nabr when  click navbar link (scroll) ===================================
   menuIcon.classList.remove("bx-x");
   navbar.classList.remove("active");
};


// scroll reveal
ScrollReveal({
    reset: true,
    distance: '80px',
    duration: 2000,
    delay:1000,
});
  
ScrollReveal().reveal(".home-content, .heading", { origin: 'top' });
ScrollReveal().reveal(".home-img, .services-container", ".portfolio-box", ".contact form", { origin: 'bottom' });
ScrollReveal().reveal(".home-content h1, .about-img", { origin: 'left' });
ScrollReveal().reveal(".home-content p, .about-content", { origin: 'right' });


// typed js

const typed = new Typed('.multiple-text', {
    strings: ['Frontend Developer', 'Youtuber', 'Blogger'],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true
});
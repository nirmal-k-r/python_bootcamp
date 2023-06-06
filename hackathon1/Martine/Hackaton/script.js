const slideshowImages = document.querySelectorAll('.slideshow img');

let currentIndex = 0;
slideshowImages[currentIndex].classList.add('active');

function showNextSlide() {
  slideshowImages[currentIndex].classList.remove('active');
  currentIndex = (currentIndex + 1) % slideshowImages.length;
  slideshowImages[currentIndex].classList.add('active');
}

setInterval(showNextSlide, 3000);
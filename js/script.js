// Counter animation using IntersectionObserver
const counters = document.querySelectorAll('.counter');

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const counter = entry.target;
            const updateCount = () => {
                const target = +counter.getAttribute('data-target');
                const count = +counter.innerText;
                const increment = Math.ceil(target / 200);

                if (count < target) {
                    counter.innerText = count + increment;
                    setTimeout(updateCount, 20);
                } else {
                    counter.innerText = target;
                }
            };
            updateCount();
            // Stop observing the counter once it has started
            observer.unobserve(counter);
        }
    });
}, {
    threshold: 0.5 // This means the animation will start when 50% of the element is visible
});

// Observe each counter
counters.forEach(counter => {
    observer.observe(counter);
});

// Toggle Sidebar
function toggleMenu() {
  const sidebar = document.getElementById("sidebar");
  const overlay = document.getElementById("overlay");

  if (sidebar.classList.contains("open")) {
    sidebar.classList.remove("open");
    if (overlay) overlay.style.display = "none";
  } else {
    sidebar.classList.add("open");
    if (overlay) overlay.style.display = "block";
  }
}

// Counter animation using IntersectionObserver
document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll('.counter');

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counter = entry.target;
        const targetString = counter.getAttribute('data-target');
        const target = parseFloat(targetString);
        const suffix = targetString.replace(target, '');

        const updateCount = () => {
          const count = parseFloat(counter.innerText);
          const increment = Math.ceil(target / 200);

          if (count < target) {
            counter.innerText = (count + increment) + suffix;
            setTimeout(updateCount, 20);
          } else {
            counter.innerText = target + suffix;
          }
        };

        updateCount();
        observer.unobserve(counter);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => {
    observer.observe(counter);
  });

  // Partners auto-load logos from images/partners
  function loadPartners() {
    const partnersLogos = document.getElementById('partnersLogos');
    if (partnersLogos) {
      for (let i = 1; i <= 8; i++) {
        const img = document.createElement('img');
        img.src = `images/partners/${i}.png`;
        img.alt = `Partner logo ${i}`;
        img.onerror = function() { this.style.display = 'none'; };
        partnersLogos.appendChild(img);
      }
    }
  }

  function loadGallery() {
  const galleryGrid = document.getElementById('galleryGrid');
  if (galleryGrid) {
    const frameClasses = ['', 'tall', 'wide', 'big'];
    let used = {};
    for (let i = 1; i <= 40; i++) {
      const img = document.createElement('img');
      img.src = `images/gallery/${i}.jpg`;
      img.alt = `Gallery image ${i}`;
      img.onerror = function() { this.style.display = 'none'; };

      let frameClass = frameClasses[Math.floor(Math.random() * frameClasses.length)];
      if (frameClass === 'big') {
        used['big'] = (used['big'] || 0) + 1;
        if (used['big'] > 2) frameClass = '';
      }
      img.className = frameClass;

      // Add click listener to open in lightbox
      img.addEventListener('click', () => openLightbox(img.src));

      galleryGrid.appendChild(img);
    }
  }
}

// Lightbox functions
function openLightbox(src) {
  const lightbox = document.getElementById("lightbox");
  const lightboxImg = document.getElementById("lightbox-img");
  lightbox.style.display = "flex";
  lightboxImg.src = src;
}

function closeLightbox() {
  document.getElementById("lightbox").style.display = "none";
}

// Setup close events
window.addEventListener("load", () => {
  const lightbox = document.getElementById("lightbox");
  const closeBtn = document.getElementById("lightbox-close"); // safer with unique ID

  if (lightbox && closeBtn) {
    // Close when clicking the X
    closeBtn.addEventListener("click", closeLightbox);

    // Close when clicking outside the image
    lightbox.addEventListener("click", (e) => {
      if (e.target === lightbox) closeLightbox();
    });
  }
});


loadPartners();
loadGallery();
});

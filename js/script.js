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
document.addEventListener("DOMContentLoaded", () => {
    const counters = document.querySelectorAll(".counter");
    counters.forEach(counter => {
      const updateCounter = () => {
        const target = +counter.getAttribute("data-target");
        const current = +counter.innerText;
        const increment = target / 200;

        if (current < target) {
          counter.innerText = Math.ceil(current + increment);
          setTimeout(updateCounter, 10);
        } else {
          counter.innerText = target;
        }
      };
      updateCounter();
    });
  });


document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('enquiry-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        alert('Thank you for your enquiry! We will get back to you soon.');
        form.reset();
    });
});

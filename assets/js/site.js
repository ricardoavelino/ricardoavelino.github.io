const items = [...document.querySelectorAll('.reveal')];
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        const i = items.indexOf(e.target);
        e.target.style.transitionDelay = Math.min(i,6)*60 + 'ms';
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    });
  }, {threshold:.12, rootMargin:'0px 0px -6% 0px'});
  items.forEach(el=>io.observe(el));

// --- BibTeX show/hide + copy-to-clipboard ---
document.addEventListener('click', (e) => {
  const btn = e.target.closest('[data-bib]');
  if (btn) {
    const box = document.getElementById(btn.getAttribute('data-bib'));
    if (box) box.hidden = !box.hidden;
    return;
  }
  if (e.target.classList.contains('copy')) {
    const code = e.target.parentElement.querySelector('code');
    if (code && navigator.clipboard) navigator.clipboard.writeText(code.textContent.trim());
    e.target.textContent = 'Copied';
    setTimeout(() => { e.target.textContent = 'Copy'; }, 1200);
  }
});

// --- Contact form: show confirmation after FormSubmit redirect (?sent=true) ---
if (location.search.indexOf('sent=true') !== -1) {
  const form = document.querySelector('.contact-form');
  if (form) {
    const b = document.createElement('div');
    b.className = 'sent-banner';
    b.textContent = 'Thank you — your message has been sent. I’ll get back to you soon.';
    form.parentNode.insertBefore(b, form);
    form.reset();
  }
}

// --- Mobile nav toggle (hamburger) ---
(function(){
  const btn = document.querySelector('.navtoggle');
  const nav = document.getElementById('navlinks');
  if (!btn || !nav) return;
  btn.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  // close after tapping a link
  nav.addEventListener('click', (e) => {
    if (e.target.closest('a')) { nav.classList.remove('open'); btn.setAttribute('aria-expanded','false'); }
  });
})();

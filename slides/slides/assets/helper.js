document.addEventListener("DOMContentLoaded", function() {
  const initPersistence = () => {
    const notes = document.querySelectorAll('.persistent-notes');
    notes.forEach(note => {
      const storageKey = 'reveal-note-' + note.id;

      // 1. Load saved content
      const savedContent = localStorage.getItem(storageKey);
      if (savedContent) {
        note.innerText = savedContent;
      }

      // 2. Save content on input (if not already attached)
      if (!note.dataset.listenerAttached) {
        note.addEventListener('input', () => {
          localStorage.setItem(storageKey, note.innerText);
        });
        note.dataset.listenerAttached = "true";
      }
    });
  };

  // Run when the presentation is ready and every time the slide changes
  if (typeof Reveal !== 'undefined') {
    Reveal.on('ready', initPersistence);
    Reveal.on('slidechanged', initPersistence);
  } else {
    // Fallback if Reveal isn't ready yet
    setTimeout(initPersistence, 500);
  }
});

// Title slide footer. A deck sets its text with `data-title-footer: "..."` under
// title-slide-attributes (e.g. to credit an AI image). The title slide cannot hold a
// ::: footer, so add one footer next to Quarto's and show it only on the title slide.
document.addEventListener("DOMContentLoaded", function() {
  const title = document.getElementById("title-slide");
  const text = title && title.getAttribute("data-title-footer");
  if (!text || typeof Reveal === "undefined") return;
  const footer = document.createElement("div");
  footer.className = "footer footer-default footer-on-image";
  footer.textContent = text;
  const update = () => {
    if (!footer.parentNode) Reveal.getRevealElement().appendChild(footer);
    footer.style.display = Reveal.getCurrentSlide() === title ? "block" : "none";
  };
  Reveal.on("ready", update);
  Reveal.on("slidechanged", update);
  if (Reveal.isReady()) update();
});

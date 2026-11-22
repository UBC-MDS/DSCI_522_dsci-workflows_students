// Pyodide (the in-browser Python behind the {pyodide} cells) runs in a plain web
// worker and does not need cross-origin isolation. Earlier versions of this deck
// registered coi-serviceworker.js, which stops the Pyodide worker from loading.
// If a visitor's browser still has that service worker, unregister it once and
// reload so the page is no longer controlled by it.
if (navigator.serviceWorker && navigator.serviceWorker.controller && !sessionStorage.getItem("coiCleaned")) {
  navigator.serviceWorker.getRegistrations()
    .then(rs => Promise.all(rs.map(r => r.unregister())))
    .then(() => { sessionStorage.setItem("coiCleaned", "1"); location.reload(); });
}

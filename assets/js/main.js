/* StripChat Token Safety Guide — progressive enhancement only.
   The site is fully readable and navigable with JavaScript disabled. */
(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    /* Mobile navigation toggle */
    var toggle = document.querySelector(".nav-toggle");
    var nav = document.getElementById("primary-nav");
    if (toggle && nav) {
      toggle.addEventListener("click", function () {
        var open = nav.classList.toggle("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
      nav.addEventListener("click", function (e) {
        if (e.target.closest("a")) {
          nav.classList.remove("open");
          toggle.setAttribute("aria-expanded", "false");
        }
      });
    }

    /* Dismissible age/content notice (preference stored locally only) */
    var notice = document.getElementById("age-notice");
    var dismiss = document.getElementById("age-dismiss");
    if (notice && dismiss) {
      try {
        if (localStorage.getItem("ageNoticeDismissed") === "1") {
          notice.hidden = true;
        }
      } catch (err) { /* storage unavailable: leave notice visible */ }
      dismiss.addEventListener("click", function () {
        notice.hidden = true;
        try { localStorage.setItem("ageNoticeDismissed", "1"); } catch (err) {}
      });
    }

    /* Contact form: open the visitor's email client (no server, no tracking) */
    var form = document.getElementById("contact-form");
    if (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var to = form.getAttribute("data-to") || "";
        var topic = (form.querySelector("#cf-topic") || {}).value || "Website message";
        var name = (form.querySelector("#cf-name") || {}).value || "";
        var from = (form.querySelector("#cf-email") || {}).value || "";
        var message = (form.querySelector("#cf-message") || {}).value || "";
        var subject = "[" + topic + "] StripChat Token Safety Guide";
        var body =
          "Topic: " + topic + "\n" +
          "Name: " + name + "\n" +
          "Reply-to: " + from + "\n\n" +
          message + "\n";
        window.location.href =
          "mailto:" + to + "?subject=" + encodeURIComponent(subject) +
          "&body=" + encodeURIComponent(body);
      });
    }

    /* Table-of-contents scrollspy (enhancement, keyboard nav unaffected) */
    var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc a[href^='#']"));
    if (tocLinks.length && "IntersectionObserver" in window) {
      var byId = {};
      tocLinks.forEach(function (a) {
        byId[a.getAttribute("href").slice(1)] = a;
      });
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          var link = byId[entry.target.id];
          if (!link) return;
          if (entry.isIntersecting) {
            tocLinks.forEach(function (l) { l.classList.remove("active"); });
            link.classList.add("active");
          }
        });
      }, { rootMargin: "-20% 0px -70% 0px", threshold: 0 });
      tocLinks.forEach(function (a) {
        var section = document.getElementById(a.getAttribute("href").slice(1));
        if (section) observer.observe(section);
      });
    }
  });
})();

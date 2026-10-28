/* Perspective site behaviour. Progressive enhancement: every page is complete
   with JavaScript off, apart from the ICS footer, which ics-site also injects. */

/* ── Masthead navigation, copied from the ICS MA & PhD site
      (philosophy/docs/assets/site.js, itself from faculty.icscanada.edu) ── */
(function () {
  'use strict';

  document.documentElement.classList.add('js');

  var burger = document.querySelector('.ics-burger');
  var menu = document.getElementById('mobileMenu');

  function closeMenu() {
    if (!menu) return;
    menu.classList.remove('is-open');
    document.body.style.overflow = '';
    if (burger) {
      burger.setAttribute('aria-expanded', 'false');
      burger.focus();
    }
  }

  if (burger && menu) {
    burger.setAttribute('aria-expanded', 'false');
    burger.setAttribute('aria-controls', 'mobileMenu');
    burger.addEventListener('click', function () {
      menu.classList.add('is-open');
      document.body.style.overflow = 'hidden';
      burger.setAttribute('aria-expanded', 'true');
      var close = menu.querySelector('.ics-mobile-menu__close');
      if (close) close.focus();
    });
    var closeBtn = menu.querySelector('.ics-mobile-menu__close');
    if (closeBtn) closeBtn.addEventListener('click', closeMenu);
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') closeMenu();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('is-open')) closeMenu();
    });
  }

  Array.prototype.forEach.call(
    document.querySelectorAll('.ics-nav__item > button'),
    function (btn) {
      btn.addEventListener('click', function () {
        var open = this.getAttribute('aria-expanded') === 'true';
        this.setAttribute('aria-expanded', open ? 'false' : 'true');
      });
    }
  );
})();

/* ── Archive: the issue you last opened keeps a red flag on its cover,
      so a reader working through the run can pick up where they left off.
      Stored only in this browser; the page is whole without it. ── */
(function () {
  'use strict';
  var KEY = 'perspective:last-issue';
  var issues = document.querySelectorAll('.issue[data-slug]');
  if (!issues.length) return;

  function mark(slug) {
    Array.prototype.forEach.call(issues, function (el) {
      var on = el.getAttribute('data-slug') === slug;
      el.classList.toggle('is-last', on);
      var flag = el.querySelector('.issue__flag');
      if (on && !flag) {
        flag = document.createElement('span');
        flag.className = 'issue__flag';
        flag.textContent = 'Last opened';
        el.querySelector('.issue__cover').appendChild(flag);
      } else if (!on && flag) {
        flag.remove();
      }
    });
  }

  try { var saved = localStorage.getItem(KEY); if (saved) mark(saved); } catch (e) {}

  Array.prototype.forEach.call(issues, function (el) {
    el.addEventListener('click', function () {
      var slug = el.getAttribute('data-slug');
      try { localStorage.setItem(KEY, slug); } catch (e) {}
      mark(slug);
    });
  });
})();

/* ── Decade rail: marks the decade in view ── */
(function () {
  'use strict';
  var links = document.querySelectorAll('.decades a[href^="#d"]');
  if (!links.length || !('IntersectionObserver' in window)) return;
  var byId = {};
  Array.prototype.forEach.call(links, function (a) { byId[a.getAttribute('href').slice(1)] = a; });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting || !byId[e.target.id]) return;
      Array.prototype.forEach.call(links, function (l) { l.removeAttribute('aria-current'); });
      byId[e.target.id].setAttribute('aria-current', 'true');
    });
  }, { rootMargin: '-30% 0px -65% 0px' });
  Object.keys(byId).forEach(function (id) {
    var s = document.getElementById(id);
    if (s) io.observe(s);
  });
})();

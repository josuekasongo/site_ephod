/* ── LANGUAGE ENGINE SYNCHRONIZATION ── */
// Relying on global variables declared in lang.js: window.translations and window.currentLang

// --- PORTFOLIO FILTERING SYSTEM ---
function initPortfolioFiltering() {
  const filterBtns = document.querySelectorAll('[data-filter]');
  const filterItems = document.querySelectorAll('.filter-item');

  if (filterBtns.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        // Change active button styling
        filterBtns.forEach(b => {
          b.classList.remove('active', 'btn-ephod-primary');
          b.classList.add('btn-ephod-outline');
        });
        btn.classList.add('active', 'btn-ephod-primary');
        btn.classList.remove('btn-ephod-outline');

        const filterValue = btn.getAttribute('data-filter');

        filterItems.forEach(item => {
          if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
            item.style.display = 'block';
            setTimeout(() => { item.style.opacity = '1'; item.style.transform = 'translateY(0)'; }, 10);
          } else {
            item.style.opacity = '0';
            item.style.transform = 'translateY(20px)';
            setTimeout(() => { item.style.display = 'none'; }, 300);
          }
        });
      });
    });
  }
}
// Multiple init blocks merged into the final one at the bottom of the file

// --- HERO SWIPER INITIALIZATION ---
function initHeroSwiper() {
  const swiperEl = document.querySelector('.hero-swiper');
  if (!swiperEl || swiperEl.classList.contains('swiper-initialized')) return;
  const hSwiper = new Swiper('.hero-swiper', {
    loop: true,
    speed: 1000,
    autoplay: {
      delay: 8000,
      disableOnInteraction: false,
    },
    pagination: {
      el: '.hero-pagination',
      clickable: true,
    },
    on: {
      slideChangeTransitionStart: function () {
        // Reset typewriter animations on slide change if needed
        const activeSlide = this.slides[this.activeIndex];
        const chainedEls = activeSlide.querySelectorAll('.chained');
        chainedEls.forEach(el => {
          el.style.width = '0';
          setTimeout(() => el.style.width = '100%', 100);
        });
      }
    }
  });

  // Next slide button in Slide 1
  document.querySelectorAll('.next-slide-btn').forEach(btn => {
    btn.addEventListener('click', () => hSwiper.slideNext());
  });
}

// --- ANIMATED COUNTERS ---
function initCounters() {
  const counters = document.querySelectorAll('.stat-number');
  const speed = 200;

  const startCounter = (el) => {
    const target = +el.getAttribute('data-target');
    let count = 0;
    const updateCount = () => {
      const inc = target / speed;
      if (count < target) {
        count += inc;
        el.innerText = Math.ceil(count);
        setTimeout(updateCount, 1);
      } else {
        el.innerText = target;
      }
    };
    updateCount();
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        startCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(c => observer.observe(c));
}

// Language events are dispatched by lang.js


/* ── PRELOADER ─────────────────────────────────────────── */
function initPreloader() {
  const preloader = document.getElementById('preloader');
  
  // Always ensure preloader-active is removed as a safety measure
  setTimeout(() => {
    document.body.classList.remove('preloader-active');
  }, 1000);

  if (!document.querySelector('.noise-overlay')) {
    const noise = document.createElement('div');
    noise.className = 'noise-overlay';
    document.body.appendChild(noise);
  }

  if (!preloader) return;
  window.addEventListener('load', () => {
    setTimeout(() => {
      preloader.classList.add('hidden');
      document.body.classList.remove('preloader-active');
    }, 700);
  });
  setTimeout(() => {
    if (preloader && !preloader.classList.contains('hidden')) {
      preloader.classList.add('hidden');
      document.body.classList.remove('preloader-active');
    }
  }, 3500);
}

/* ── CUSTOM CURSOR ─────────────────────────────────────── */
function initCursor() {
  if ('ontouchstart' in window) return;
  const dot    = document.getElementById('cursor-dot');
  const circle = document.getElementById('cursor-circle');
  if (!dot || !circle) return;
  document.body.classList.add('has-cursor');
  let mx = -200, my = -200, cx = -200, cy = -200;
  document.addEventListener('mousemove', e => {
    mx = e.clientX; my = e.clientY;
    dot.style.transform = `translate(${mx - 3}px,${my - 3}px)`;
  });
  (function tick() {
    cx += (mx - cx) * 0.13;
    cy += (my - cy) * 0.13;
    circle.style.transform = `translate(${cx - 20}px,${cy - 20}px)`;
    requestAnimationFrame(tick);
  })();
  document.addEventListener('mouseover', e => {
    const over = e.target.closest('a,button,.service-card,.portfolio-card,.job-card,.value-card,.btn-ephod');
    dot.classList.toggle('hov', !!over);
    circle.classList.toggle('hov', !!over);
  });
}

/* ── NAVBAR ────────────────────────────────────────────── */
function initNavbar() {
  const nav = document.getElementById('mainNavbar');
  if (!nav) return;
  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    nav.classList.toggle('scrolled', y > 40);
    // Dynamic hiding disabled to ensure logo visibility and prevent clipping issues
    nav.style.transform = 'translateY(0)';
  }, { passive: true });
}

/* ── SCROLL REVEAL ─────────────────────────────────────── */
function initReveal() {
  const els = document.querySelectorAll('.fade-up, .fade-left, .fade-right, .scale-in, .clip-reveal');
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (!en.isIntersecting) return;
      const el = en.target;
      const delay = parseFloat(el.dataset.delay || 0) * 1000;
      
      // Add a slight random jitter to staggered grid elements for a more organic feel
      const extraDelay = el.closest('.reveal-group') ? 50 : 0;

      setTimeout(() => {
        el.classList.add('visible');
      }, delay + extraDelay);

      io.unobserve(el);
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
  els.forEach(el => io.observe(el));
}

/* ── COUNTERS ──────────────────────────────────────────── */
function initCounters() {
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (!en.isIntersecting) return;
      const el = en.target;
      const end = parseInt(el.dataset.count, 10);
      const sfx = el.dataset.suffix || '';
      const t0 = Date.now(), dur = 2200;
      (function tick() {
        const p = Math.min((Date.now() - t0) / dur, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(end * eased) + sfx;
        if (p < 1) requestAnimationFrame(tick);
      })();
      io.unobserve(el);
    });
  }, { threshold: 0.6 });
  document.querySelectorAll('[data-count]').forEach(el => io.observe(el));
}

/* ── MAGNETIC BUTTONS ──────────────────────────────────── */
function initMagnetic() {
  document.querySelectorAll('.btn-ephod, .rmda-plus-btn, .lang-btn').forEach(btn => {
    btn.addEventListener('mousemove', e => {
      const r = btn.getBoundingClientRect();
      const x = (e.clientX - r.left - r.width / 2) * 0.28;
      const y = (e.clientY - r.top - r.height / 2) * 0.28;
      btn.style.transform = `translate(${x}px,${y}px)`;
    });
    btn.addEventListener('mouseleave', () => btn.style.transform = '');
  });
}

/* ── PROGRESS BARS ─────────────────────────────────────── */
function initProgress() {
  const bars = document.querySelectorAll('.progress-bar-custom,.progress-bar-gold');
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (!en.isIntersecting) return;
      const b = en.target;
      const w = b.dataset.width || b.style.width;
      b.style.width = '0%';
      setTimeout(() => b.style.width = w, 150);
      io.unobserve(b);
    });
  }, { threshold: 0.3 });
  bars.forEach(b => { b.dataset.width = b.style.width; b.style.width = '0%'; io.observe(b); });
}

/* ── MARQUEE ───────────────────────────────────────────── */
function initMarquee() {
  document.querySelectorAll('.marquee-track').forEach(t => {
    t.innerHTML += t.innerHTML;
  });
}

/* ── PAGE TRANSITION ───────────────────────────────────── */
function initTransition() {
  const ov = document.getElementById('page-transition');
  if (!ov) return;
  // Reveal on load
  ov.classList.add('loaded');
  setTimeout(() => { ov.classList.add('leaving'); setTimeout(() => ov.classList.remove('loaded','leaving'), 600); }, 50);
  
  // Cover on navigate
  document.querySelectorAll('a[href]').forEach(a => {
    const h = a.getAttribute('href');
    if (!h || h.startsWith('mailto') || h.startsWith('tel') || h.includes('://')) return;

    a.addEventListener('click', e => {
      // Check if it's an intra-page anchor
      const isAnchor = h.includes('#');
      const parts = h.split('#');
      const pathOnly = parts[0];
      const anchorOnly = parts[1] ? '#' + parts[1] : '';
      
      const currentPage = window.location.pathname.split('/').pop() || 'index.html';

      // Function to close mobile menu
      const closeMenu = () => {
        const navCollapse = document.getElementById('navMenu');
        if (navCollapse && navCollapse.classList.contains('show')) {
          const bsCollapse = bootstrap.Collapse.getInstance(navCollapse);
          if (bsCollapse) bsCollapse.hide();
        }
      };

      if (isAnchor && (pathOnly === '' || pathOnly === currentPage)) {
        // It's a same-page anchor
        e.preventDefault();
        closeMenu();
        
        const target = document.querySelector(anchorOnly);
        if (target) {
          const offset = 90;
          const targetPos = target.getBoundingClientRect().top + window.pageYOffset - offset;
          window.scrollTo({ top: targetPos, behavior: 'smooth' });
          // Update URL without jump
          history.pushState(null, null, anchorOnly);
        }
        return; 
      }

      if (h[0] === '#') return;

      e.preventDefault();
      closeMenu();
      ov.classList.remove('leaving');
      ov.classList.add('entering');
      setTimeout(() => location.href = h, 480);
    });
  });
}

function handleInitialAnchor() {
  const hash = window.location.hash;
  if (hash) {
    setTimeout(() => {
      const target = document.querySelector(hash);
      if (target) {
        const offset = 100;
        const targetPos = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: targetPos, behavior: 'smooth' });
      }
    }, 1000); // Delay to allow page transition to finish
  }
}

/* ── TYPEWRITER ENGINE (Robust Version) ──────────────── */
let activeTypewriters = new Set();
window.stopAllTypewriters = function() {
  activeTypewriters.forEach(id => clearInterval(id));
  activeTypewriters.clear();
  document.querySelectorAll('.typing-active, .typing-complete').forEach(el => {
    el.classList.remove('typing-active', 'typing-complete');
  });
};


function typeWriter(el, speed = 50, callback = null) {
  // 1. Force state
  el.classList.add('typing-active');
  el.style.opacity = '1';
  el.style.visibility = 'visible';
  el.style.display = 'inline-block';

  // 2. Get text from data attribute (protected) or innerHTML
  let text = el.getAttribute('data-typewriter-text') || el.innerHTML;
  
  // Cleanup initial HTML if it's still containing data-i18n tags
  if (text.includes('data-i18n')) {
     setTimeout(() => {
       const retryText = el.getAttribute('data-typewriter-text') || el.innerHTML;
       startTyping(el, retryText, speed, callback);
     }, 100);
     return;
  }
  
  startTyping(el, text, speed, callback);
}

function startTyping(el, text, speed, callback) {
  el.innerHTML = '';
  let i = 0;
  let currentHTML = '';
  
  const interval = setInterval(() => {
    if (i < text.length) {
      if (text.charAt(i) === '<') {
        let tag = '';
        while (i < text.length && text.charAt(i) !== '>') {
          tag += text.charAt(i);
          i++;
        }
        tag += '>';
        i++;
        currentHTML += tag;
      } else {
        currentHTML += text.charAt(i);
        i++;
      }
      el.innerHTML = currentHTML;
    } else {
      clearInterval(interval);
      el.classList.remove('typing-active');
      el.classList.add('typing-complete');
      activeTypewriters.delete(interval);
      if (callback) callback();
    }
  }, speed);
  
  activeTypewriters.add(interval);
}

function initScrollTypewriter() {
  const groups = document.querySelectorAll('.typewriter-group');
  
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const group = entry.target;
        const elements = Array.from(group.querySelectorAll('.chained'));
        
        // Safety: hide all initially in case CSS is slow
        elements.forEach(el => { el.style.opacity = '0'; el.style.visibility = 'hidden'; });

        function playChain(idx) {
          if (idx >= elements.length) return;
          const el = elements[idx];
          typeWriter(el, parseInt(el.dataset.speed, 10) || 60, () => {
            setTimeout(() => playChain(idx + 1), 350); 
          });
        }
        
        playChain(0);
        observer.unobserve(group);
      }
    });
  }, { threshold: 0.05, rootMargin: '0px 0px -100px 0px' });

  groups.forEach(g => {
    observer.observe(g);
  });
}

// Global accessors for language switcher
window.resetAllTypewriters = function() {
  window.stopAllTypewriters();
  
  // Restart Scroll-based typewriters
  document.querySelectorAll('.typewriter-scroll, .chained').forEach(el => {
    el.style.opacity = '0';
    el.style.visibility = 'hidden';
  });
  
  // Re-run the observers to catch elements currently in view
  initScrollTypewriter();
};

/* ── HERO PARALLAX ─────────────────────────────────────── */
function initParallax() {
  const shape = document.querySelector('.hero-bg-shape');
  if (!shape) return;
  window.addEventListener('scroll', () => {
    if (window.scrollY < window.innerHeight)
      shape.style.transform = `translateY(${window.scrollY * 0.15}px)`;
  }, { passive: true });
}

/* ── CARD TILT ─────────────────────────────────────────── */
function initTilt() {
  document.querySelectorAll('.service-card,.value-card,.srv-square-card').forEach(card => {
    card.addEventListener('mousemove', e => {
      const r = card.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width - 0.5;
      const y = (e.clientY - r.top) / r.height - 0.5;
      card.style.transform = `perspective(700px) rotateY(${x*7}deg) rotateX(${-y*7}deg) translateY(-6px)`;
    });
    card.addEventListener('mouseleave', () => card.style.transform = '');
  });
}

/* ── SCROLL INDICATOR ──────────────────────────────────── */
function initScrollIndicator() {
  const si = document.querySelector('.scroll-indicator');
  if (!si) return;
  si.addEventListener('click', () => {
    const next = document.querySelector('header + *');
    if (next) next.scrollIntoView({ behavior: 'smooth' });
  });
}

/* ── ACTIVE NAV ────────────────────────────────────────── */
function initActiveNav() {
  const currentPath = window.location.pathname;
  let pageName = currentPath.split('/').pop() || 'index.html';
  if (pageName === '') pageName = 'index.html';
  const currentHash = window.location.hash;

  const links = document.querySelectorAll('.nav-link, .nav-dropdown-item');
  links.forEach(a => {
    a.classList.remove('active');
    const href = a.getAttribute('href');
    if (!href) return;

    const hrefParts = href.split('#');
    let hrefPath = hrefParts[0] || 'index.html';
    if (hrefPath === './' || hrefPath === '/') hrefPath = 'index.html';
    const hrefHash = hrefParts[1] ? '#' + hrefParts[1] : '';

    // Standardize comparison
    const isCurrentPage = (hrefPath === pageName);
    const isHashMatch = (!hrefHash || hrefHash === currentHash);

    if (isCurrentPage && isHashMatch) {
      a.classList.add('active');
      // Also highlight parent if in dropdown
      const parentDropdown = a.closest('.nav-item.has-dropdown');
      if (parentDropdown) {
        const topLink = parentDropdown.querySelector('.nav-link');
        if (topLink) topLink.classList.add('active');
      }
    }
  });
  
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 50);
    }, { passive: true });
    navbar.classList.toggle('scrolled', window.scrollY > 50);
  }

  // Auto-close mobile menu on link click
  const navCollapse = document.getElementById('navMenu');
  if (navCollapse) {
    links.forEach(link => {
      link.addEventListener('click', () => {
        if (navCollapse.classList.contains('show')) {
          const bsCollapse = bootstrap.Collapse.getInstance(navCollapse) || new bootstrap.Collapse(navCollapse);
          bsCollapse.hide();
        }
      });
    });
  }
}

/* ── NEWS SLIDER (SWIPER) ──────────────────────────────── */
function initNewsSlider() {
  if (!document.querySelector('.newsSwiper')) return;
  const swiper = new Swiper('.newsSwiper', {
    loop: true,
    speed: 1000,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    effect: 'fade',
    fadeEffect: {
      crossFade: true
    },
  });
}

/* ── PARTNERS MARQUEE ──────────────────────────────────── */
function initPartnersMarquee() {
  const swiperEl = document.querySelector('.partners-swiper');
  if (!swiperEl) return;
  new Swiper('.partners-swiper', {
    loop: true,
    speed: 5000,
    autoplay: {
      delay: 0,
      disableOnInteraction: false,
    },
    slidesPerView: 2,
    spaceBetween: 30,
    breakpoints: {
      640: { slidesPerView: 3 },
      768: { slidesPerView: 4 },
      1024: { slidesPerView: 5 },
    },
    freeMode: true,
  });
}

/* ── CONTACT FORM HANDLER ──────────────────────────── */
function initContactForm() {
  const form = document.getElementById('contactForm');
  if (!form) return;
  
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const originalText = btn.innerHTML;
    
    // Simulate loading state
    btn.disabled = true;
    btn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> ...';
    
    setTimeout(() => {
      // Success state
      btn.classList.remove('btn-ephod-primary');
      btn.classList.add('btn-success');
      btn.innerHTML = '<i class="bi bi-check-lg"></i> Envoyé !';
      
      // Reset after 3s
      setTimeout(() => {
        form.reset();
        btn.disabled = false;
        btn.classList.remove('btn-success');
        btn.classList.add('btn-ephod-primary');
        btn.innerHTML = originalText;
      }, 3000);
    }, 1500);
  });
}

/* ── PORTFOLIO FILTER ──────────────────────────────────── */
function initPortfolioFilter() {
  const filterBtns = document.querySelectorAll('[data-filter]');
  const filterItems = document.querySelectorAll('.filter-item');
  if (filterBtns.length === 0 || filterItems.length === 0) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.getAttribute('data-filter');
      
      // Update buttons
      filterBtns.forEach(b => {
        b.classList.remove('active', 'btn-ephod-primary');
        b.classList.add('btn-ephod-outline');
      });
      btn.classList.add('active', 'btn-ephod-primary');
      btn.classList.remove('btn-ephod-outline');

      // Filter items
      filterItems.forEach(item => {
        const cat = item.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          item.classList.remove('hidden-filter');
          // Relative position to allow grid layout to naturally fill gaps
          setTimeout(() => {
            item.style.position = 'relative';
            item.style.visibility = 'visible';
          }, 400);
        } else {
          item.classList.add('hidden-filter');
          // Absolute position to "remove" it from flow after fade out
          setTimeout(() => {
            if (item.classList.contains('hidden-filter')) {
              item.style.position = 'absolute';
              item.style.visibility = 'hidden';
            }
          }, 600);
        }
      });
    });
  });
}

/* ── MODAL POPULATION UTILITY ── */
function populateAndOpen(modal, type, id) {
  if (!modal) return;
  
  // Use window-level globals from lang.js
  const lang = window.currentLang || 'fr';
  const data = window.translations ? window.translations[lang] : null;
  
  if (!data) {
    console.error('Translation data missing for:', lang);
    return;
  }

  // Determine prefix (e.g. 'port.refX_' or 'srv.sX_' or 'port.pX_')
  let prefix = '';
  if (type === 'project') {
    // Check if id starts with 'p' (our new system) or is a number (old system)
    prefix = id.toString().startsWith('p') ? `port.${id}_` : `port.ref${id}_`;
  } else {
    // Service
    prefix = `srv.s${id}_`;
  }

  // Store ID for download
  const container = modal.querySelector('.ephod-modal-container');
  if (container) {
    if (type === 'project') container.dataset.currentProjectId = id;
    if (type === 'service') container.dataset.currentServiceId = id;
  }

  // Populate Modal Content
  if (type === 'project') {
    modal.querySelector('.modal-badge-elite').innerHTML = data['port.modal_badge'] || 'REU';
    modal.querySelector('#modal-client').innerHTML      = data[prefix + 'client'] || '';
    modal.querySelector('#modal-title').innerHTML       = data[prefix + 'title']  || '';
    
    // Mission Meta Grid
    modal.querySelector('#modal-zone').innerHTML    = data[prefix + 'zone'] || '-';
    modal.querySelector('#modal-date').innerHTML    = data[prefix + 'date'] || '-';
    modal.querySelector('#modal-contact').innerHTML = data[prefix + 'contact'] || '-';

    modal.querySelector('#modal-context').innerHTML = data[prefix + 'context']  || '';
    modal.querySelector('#modal-strategy').innerHTML = data[prefix + 'solution'] || '';
    modal.querySelector('#modal-impact').innerHTML   = data[prefix + 'impact']   || '';
  } else {
    // SERVICE MODAL
    modal.querySelector('.modal-client-name').innerHTML   = data['nav.services'] || 'Expertise';
    modal.querySelector('.modal-project-title').innerHTML = data['srv.s' + id + '_title'] || '';
    
    modal.querySelector('#modal-need').innerHTML   = data[prefix + 'need']  || '';
    modal.querySelector('#modal-method').innerHTML = data[prefix + 'how']   || '';
    modal.querySelector('#modal-value').innerHTML  = data[prefix + 'value'] || '';

    // Section Headers
    modal.querySelector('#header-need').innerHTML   = data['srv.modal_need'];
    modal.querySelector('#header-method').innerHTML = data['srv.modal_how'];
    modal.querySelector('#header-value').innerHTML  = data['srv.modal_value'];
  }

  // Open the modal
  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

/* ── EPHOD DYNAMIC MODALS ─────────────────────────────── */
function initEphodModals() {
  const projectModal = document.getElementById('projectModal');
  const serviceModal = document.getElementById('serviceModal');
  const closeBtns = document.querySelectorAll('.ephod-modal-close');
  const overlays = document.querySelectorAll('.ephod-modal-overlay');

  if (!projectModal && !serviceModal) return;

  // Binding logic for cards


  function closeModal() {
    document.querySelectorAll('.ephod-modal').forEach(m => m.classList.remove('active'));
    document.body.style.overflow = '';
  }

  // PROJECTS
  document.querySelectorAll('.portfolio-card .btn-view-project').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const card = btn.closest('.portfolio-card');
      const pid = card.dataset.projectId;
      if (pid && projectModal) populateAndOpen(projectModal, 'project', pid);
    });
  });

  // SERVICES
  document.querySelectorAll('.service-card .btn-view-service').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const card = btn.closest('.service-card');
      const sid = card.dataset.serviceId;
      if (sid && serviceModal) populateAndOpen(serviceModal, 'service', sid);
    });
  });

  closeBtns.forEach(b => b.addEventListener('click', closeModal));
  overlays.forEach(o => o.addEventListener('click', closeModal));
  
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
  });

  // DOWNLOAD LOGIC (PROJECTS)
  const downloadBtn = document.getElementById('btnDownloadProject');
  if (downloadBtn) {
    downloadBtn.addEventListener('click', () => {
      const container = document.getElementById('modalContainer');
      const pid = container ? container.dataset.currentProjectId : null;
      if (pid) downloadProjectReport(pid);
    });
  }

  // DOWNLOAD LOGIC (SERVICES)
  const downloadSrvBtn = document.getElementById('btnDownloadService');
  if (downloadSrvBtn) {
    downloadSrvBtn.addEventListener('click', () => {
      const container = document.getElementById('serviceModalContainer');
      const sid = container ? container.dataset.currentServiceId : null;
      if (sid) downloadServiceReport(sid);
    });
  }
}

function downloadProjectReport(pid) {
  const lang = currentLang || 'fr';
  const data = translations[lang];
  if (!data) return;

  const prefix = pid.toString().startsWith('p') ? `port.${pid}_` : `port.ref${pid}_`;
  const client = data[prefix + 'client'] || 'Client';
  const title  = data[prefix + 'title']  || 'Project';
  
  // Get content (cleaning HTML if necessary)
  const context  = (data[prefix + 'context']  || '').replace(/<[^>]*>?/gm, '');
  const strategy = (data[prefix + 'solution'] || '').replace(/<[^>]*>?/gm, '');
  const impact   = (data[prefix + 'impact']   || '').replace(/<[^>]*>?/gm, '');

  const labelChallenge = data['port.modal_challenge'] || 'Challenge';
  const labelStrategy  = data['port.modal_strategy']  || 'Strategy';
  const labelImpact    = data['port.modal_impact_title'] || 'Impact';

  const reportText = `
EPHOD CONSULTING - EXECUTIVE SUMMARY
------------------------------------
PROJECT: ${title.toUpperCase()}
CLIENT: ${client}
DATE: ${new Date().toLocaleDateString(lang === 'fr' ? 'fr-FR' : 'en-US')}

[${labelChallenge.toUpperCase()}]
${context}

[${labelStrategy.toUpperCase()}]
${strategy}

[${labelImpact.toUpperCase()}]
${impact}

------------------------------------
© ${new Date().getFullYear()} EPHOD Consulting - Excellence & Transformation
  `.trim();

  const blob = new Blob([reportText], { type: 'text/plain' });
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `EPHOD_Project_${pid}_${lang.toUpperCase()}.txt`;
  document.body.appendChild(a);
  a.click();
  window.URL.revokeObjectURL(url);
  document.body.removeChild(a);
}

function downloadServiceReport(sid) {
  const lang = currentLang || 'fr';
  const data = translations[lang];
  if (!data) return;

  const prefix = `srv.s${sid}_`;
  const title  = data[prefix + 'title']  || 'Service';
  
  const need   = (data[prefix + 'need']  || '').replace(/<[^>]*>?/gm, '');
  const how    = (data[prefix + 'how']   || '').replace(/<[^>]*>?/gm, '');
  const value  = (data[prefix + 'value'] || '').replace(/<[^>]*>?/gm, '');

  const labelNeed   = data['srv.modal_need']  || 'Needs';
  const labelHow    = data['srv.modal_how']   || 'Strategy';
  const labelValue  = data['srv.modal_value'] || 'Value';

  const reportText = `
EPHOD CONSULTING - EXPERTISE SHEET
------------------------------------
SERVICE: ${title.toUpperCase()}
OFFICE: KINSHASA / GOMA
DATE: ${new Date().toLocaleDateString(lang === 'fr' ? 'fr-FR' : 'en-US')}

[${labelNeed.toUpperCase()}]
${need}

[${labelHow.toUpperCase()}]
${how}

[${labelValue.toUpperCase()}]
${value}

------------------------------------
Methodological Rigor for Sustainable Impact
© ${new Date().getFullYear()} EPHOD Consulting SARL
  `.trim();

  const blob = new Blob([reportText], { type: 'text/plain' });
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `EPHOD_Service_${sid}_${lang.toUpperCase()}.txt`;
  document.body.appendChild(a);
  a.click();
  window.URL.revokeObjectURL(url);
  document.body.removeChild(a);
}

/* ── INIT ──────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  // Use a try-catch for the main init to ensure one failure doesn't kill the whole app
  try {
    initPreloader();
    initCursor();
    initNavbar();
    if (document.querySelector('.hero-swiper') && !document.querySelector('.hero-swiper').classList.contains('swiper-initialized')) {
      if (typeof initHeroAnimation === 'function') initHeroAnimation();
      initHeroSwiper();
    }
    initReveal();
    initCounters();
    initMagnetic();
    initProgress();
    initMarquee();
    initTransition();
    initParallax();
    initTilt();
    initScrollIndicator();
    initActiveNav();
    initNewsSlider();
    initPartnersMarquee();
    initScrollTypewriter();
    initContactForm();
    initPortfolioFilter();
    initEphodModals();
    handleInitialAnchor();
    
    const yr = document.getElementById('year');
    if (yr) yr.textContent = new Date().getFullYear();
    
    console.log("EPHOD ENGINE: Initialized successfully.");
    document.body.classList.remove('preloader-active');

    // SECURITY WATCHDOG: Force unlock scroll & close stuck menus after 1.5s
    setTimeout(() => {
      document.body.classList.remove('preloader-active');
      document.body.style.overflow = 'auto';
      document.documentElement.style.overflow = 'auto';
      // Close any persistent dropdowns if JS crashed during hover
      document.querySelectorAll('.nav-dropdown').forEach(d => {
        d.style.opacity = ''; d.style.visibility = '';
      });
      console.log("EPHOD WATCHDOG: Site visibility guaranteed.");
    }, 1500);

  } catch (err) {
    console.error("EPHOD ENGINE CRASH:", err);
    document.body.classList.remove('preloader-active');
    document.body.style.overflow = 'auto';
  }
});

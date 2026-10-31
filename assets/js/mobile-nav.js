/**
 * Adeeshy Mountain Manor - Mobile Navigation Enhancer
 * Bulletproof mobile drawer controller with event delegation,
 * body scroll lock, conflict resolution, and concierge actions.
 */
(function () {
  'use strict';

  function isMobile() {
    return window.innerWidth <= 991;
  }

  function getElements() {
    return {
      menuBtn: document.querySelector('.nav-menu-button'),
      navMenu: document.querySelector('.nav-menu'),
      navbar: document.querySelector('.navbar')
    };
  }

  function openMenu() {
    const els = getElements();
    if (els.menuBtn) {
      els.menuBtn.classList.add('is-active', 'w--open');
    }
    if (els.navMenu) {
      els.navMenu.classList.add('is-open', 'w--open');
      els.navMenu.style.setProperty('display', 'flex', 'important');
      if (window.gsap) {
        window.gsap.killTweensOf(els.navMenu);
      }
      const drawerFooter = els.navMenu.querySelector('.nav-menu-footer');
      if (drawerFooter) {
        drawerFooter.style.setProperty('opacity', '1', 'important');
        drawerFooter.style.setProperty('visibility', 'visible', 'important');
        drawerFooter.style.setProperty('transform', 'none', 'important');
      }
    }
    if (els.navbar) {
      els.navbar.classList.add('is-menu-open');
    }
    document.body.classList.add('mobile-nav-open');
    document.documentElement.classList.add('mobile-nav-open');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    const els = getElements();
    if (els.menuBtn) {
      els.menuBtn.classList.remove('is-active', 'w--open');
    }
    if (els.navMenu) {
      els.navMenu.classList.remove('is-open', 'w--open');
      els.navMenu.style.setProperty('display', 'none', 'important');
      if (window.gsap) {
        window.gsap.killTweensOf(els.navMenu);
        window.gsap.set(els.navMenu, { clearProps: 'all' });
      }
    }
    if (els.navbar) {
      els.navbar.classList.remove('is-menu-open');
      els.navbar.removeAttribute('menu-open');
      els.navbar.removeAttribute('menu-open-mobile');
    }
    document.body.classList.remove('mobile-nav-open');
    document.documentElement.classList.remove('mobile-nav-open');
    document.body.style.overflow = '';
  }

  let toggleLocked = false;
  function toggleMenu(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
      if (e.stopImmediatePropagation) e.stopImmediatePropagation();
    }
    if (toggleLocked) return;
    toggleLocked = true;
    setTimeout(function () { toggleLocked = false; }, 250);

    const els = getElements();
    if (!els.navMenu) return;

    if (els.navMenu.classList.contains('is-open')) {
      closeMenu();
    } else {
      openMenu();
    }
  }

  // Global capture-phase click and touch handler on document
  document.addEventListener('click', function (e) {
    if (!isMobile()) return;

    const btn = e.target.closest('.nav-menu-button');
    if (btn) {
      toggleMenu(e);
      return;
    }

    const els = getElements();
    if (!els.navMenu || !els.navMenu.classList.contains('is-open')) return;

    // Close when clicking any nav link inside drawer (excluding action buttons)
    const link = e.target.closest('.nav-menu a:not(.nav-drawer-quick-btn)');
    if (link) {
      closeMenu();
      return;
    }

    // If clicking inside concierge or booking button, let them work
    if (e.target.closest('.nav-drawer-quick-contact') || e.target.closest('.nav-menu-footer .button') || e.target.closest('.mobile-subnav-links')) {
      return;
    }

    // If clicked on backdrop or outside drawer content, close menu
    if (e.target === els.navMenu || !e.target.closest('.nav-main')) {
      closeMenu();
      return;
    }
  }, true);

  // Close on Escape key
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      closeMenu();
    }
  });

  // Init helpers and ensure footer actions
  function initDrawerContent() {
    const els = getElements();
    if (!els.navMenu) return;

    // Refine subnav bullet points to elegant gold dashes
    els.navMenu.querySelectorAll('.nav-sublink').forEach(function (sublink) {
      if (sublink.innerHTML.includes('&bull;') || sublink.innerHTML.includes('•')) {
        sublink.innerHTML = sublink.innerHTML.replace(/(?:&bull;|•)\s*/g, '<span class="subnav-bullet">—</span> ');
      }
    });

    // Ensure quick call, WhatsApp, and location signature exist in drawer footer
    const drawerFooter = els.navMenu.querySelector('.nav-menu-footer');
    if (drawerFooter && !drawerFooter.querySelector('.nav-drawer-quick-contact')) {
      const quickContactDiv = document.createElement('div');
      quickContactDiv.className = 'nav-drawer-quick-contact';
      quickContactDiv.innerHTML = `
        <a href="tel:+919876543210" class="nav-drawer-quick-btn">
          <svg fill="currentColor" height="15" viewBox="0 0 20 20" width="15" xmlns="http://www.w3.org/2000/svg">
            <path d="M14.36 19.4c-.05 0-.11 0-.17-.01-7.36-1.29-11.92-5.85-13.56-13.56-.06-.26 0-.54.15-.76.7-.1 1.56-.97 2.54-1.66.32-.22.75-.24 1.09-.06 1.35.74 2.49 1.87 3.39 3.36.25.42.19.95-.15 1.29l-1.51 1.51c-.14.14-.17.37-.08.54.56 1.04 1.25 1.98 2.05 2.77.79.79 1.73 1.48 2.77 2.05.18.1.4.06.54-.08l1.51-1.51c.34-.34.87-.41 1.29-.15 1.49.9 2.62 2.04 3.36 3.39.19.34.17.76-.05 1.08-.69.99-1.57 1.85-2.59 2.55-.16.11-.36.17-.55.17z"/>
          </svg>
          Call Concierge
        </a>
        <a href="https://wa.me/919876543210" target="_blank" rel="noopener" class="nav-drawer-quick-btn">
          <svg fill="currentColor" height="15" viewBox="0 0 24 24" width="15" xmlns="http://www.w3.org/2000/svg">
            <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.694.075-2.029-.481-1.613-.671-2.651-2.316-2.731-2.424-.08-.107-.648-.864-.648-1.649 0-.784.412-1.17.558-1.328.146-.159.32-.198.427-.198.106 0 .213.001.306.006.1.005.234-.038.366.279.136.327.465 1.134.506 1.217.042.083.07.181.013.292-.057.112-.086.182-.172.282-.086.101-.18.225-.258.303-.086.086-.176.18-.076.353.1.172.443.731.95 1.183.654.582 1.206.762 1.378.848.172.086.272.072.373-.044.101-.115.433-.504.549-.676.115-.173.232-.144.39-.086.158.058 1.002.472 1.174.558.172.086.287.129.33.201.042.072.042.419-.102.824z"/>
          </svg>
          WhatsApp
        </a>
      `;
      drawerFooter.appendChild(quickContactDiv);

      if (!drawerFooter.querySelector('.nav-drawer-signature')) {
        const locationSig = document.createElement('div');
        locationSig.className = 'nav-drawer-signature';
        locationSig.innerHTML = 'Sirumalai Hills, Tamil Nadu &bull; 5-Star Luxury Retreat';
        drawerFooter.appendChild(locationSig);
      }
    }
  }

  // ============================================================
  // BULLETPROOF HERO VIDEO & AUDIO MANAGER
  // Audio is ON by default, persists across page navigation,
  // handles Barba.js PJAX swaps, BFcache, and browser policies.
  // ============================================================
  function getDesiredAudioState() {
    return sessionStorage.getItem('adeeshy_hero_audio') || 'on';
  }

  function setDesiredAudioState(state) {
    sessionStorage.setItem('adeeshy_hero_audio', state);
  }

  function updateSoundUI(isUnmuted) {
    const soundToggle = document.getElementById('hero-sound-toggle');
    if (!soundToggle) return;
    if (isUnmuted) {
      soundToggle.classList.add('is-unmuted');
      const text = soundToggle.querySelector('.sound-toggle-text');
      if (text) text.textContent = 'Sound On';
      soundToggle.setAttribute('aria-pressed', 'true');
    } else {
      soundToggle.classList.remove('is-unmuted');
      const text = soundToggle.querySelector('.sound-toggle-text');
      if (text) text.textContent = 'Sound Off';
      soundToggle.setAttribute('aria-pressed', 'false');
    }
  }

  function toggleHeroAudio() {
    const heroVideo = document.getElementById('hero-drone-video') || document.querySelector('video.drone-video-player');
    if (!heroVideo) return;

    if (heroVideo.muted) {
      // Turn sound ON
      heroVideo.muted = false;
      heroVideo.volume = 1.0;
      setDesiredAudioState('on');
      updateSoundUI(true);
      if (heroVideo.paused) {
        heroVideo.play().catch(function () {});
      }
    } else {
      // Turn sound OFF
      heroVideo.muted = true;
      setDesiredAudioState('off');
      updateSoundUI(false);
    }
  }

  // Delegated click handler on document — NEVER lost across Barba / PJAX container swaps!
  document.addEventListener('click', function (e) {
    const toggleBtn = e.target.closest('#hero-sound-toggle');
    if (toggleBtn) {
      e.preventDefault();
      e.stopPropagation();
      toggleHeroAudio();
    }
  });

  // Unlock sound on first user gesture anywhere on page if cold-load autoplay policy deferred audio
  let gestureUnlockAttached = false;
  function setupGestureUnlock() {
    if (gestureUnlockAttached) return;
    gestureUnlockAttached = true;

    const unlockOnGesture = function () {
      if (getDesiredAudioState() === 'on') {
        const curVideo = document.getElementById('hero-drone-video') || document.querySelector('video.drone-video-player');
        if (curVideo && curVideo.muted) {
          curVideo.muted = false;
          curVideo.volume = 1.0;
          curVideo.play().then(function () {
            updateSoundUI(true);
          }).catch(function () {});
        }
      }
      window.removeEventListener('pointerdown', unlockOnGesture);
      window.removeEventListener('click', unlockOnGesture);
      window.removeEventListener('touchstart', unlockOnGesture);
      window.removeEventListener('keydown', unlockOnGesture);
      window.removeEventListener('scroll', unlockOnGesture);
      gestureUnlockAttached = false;
    };

    window.addEventListener('pointerdown', unlockOnGesture, { once: true, passive: true });
    window.addEventListener('click', unlockOnGesture, { once: true });
    window.addEventListener('touchstart', unlockOnGesture, { once: true, passive: true });
    window.addEventListener('keydown', unlockOnGesture, { once: true });
    window.addEventListener('scroll', unlockOnGesture, { once: true, passive: true });
  }

  function initVideoAutoplay() {
    const heroVideo = document.getElementById('hero-drone-video') || document.querySelector('video.drone-video-player');
    if (!heroVideo) return;

    const desiredState = getDesiredAudioState();

    if (desiredState === 'off') {
      heroVideo.muted = true;
      updateSoundUI(false);
      if (heroVideo.paused) {
        heroVideo.play().catch(function () {});
      }
      return;
    }

    // Default: Audio ON
    heroVideo.muted = false;
    heroVideo.volume = 1.0;
    updateSoundUI(true);

    const playPromise = heroVideo.play();
    if (playPromise !== undefined) {
      playPromise.then(function () {
        updateSoundUI(true);
      }).catch(function () {
        // Cold-load browser autoplay restriction prevented unmuted play:
        // Start playing muted temporarily, and immediately unlock sound on first interaction
        heroVideo.muted = true;
        heroVideo.play().catch(function () {});
        updateSoundUI(false);
        setupGestureUnlock();
      });
    }
  }

  // Universal Sticky Header Scroll Controller
  function initStickyScroll() {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
      let ticking = false;
      const updateNavbarScroll = function () {
        if (window.scrollY > 20) {
          navbar.classList.add('scrolled');
        } else {
          navbar.classList.remove('scrolled');
        }
        ticking = false;
      };

      window.addEventListener('scroll', function () {
        if (!ticking) {
          window.requestAnimationFrame(updateNavbarScroll);
          ticking = true;
        }
      }, { passive: true });

      updateNavbarScroll();
    }
  }

  // Init on DOM ready and Barba transitions
  function initScrollCue() {
    const scrollCue = document.querySelector('.drone-scroll-indicator');
    if (scrollCue) {
      scrollCue.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.getElementById('welcome-section') || document.querySelector('.hero-description-section');
        if (target) {
          target.scrollIntoView({ behavior: 'smooth' });
        }
      });
    }
  }

  // 1. DOM ready & window load
  document.addEventListener('DOMContentLoaded', function () {
    initDrawerContent();
    initVideoAutoplay();
    initStickyScroll();
    initScrollCue();

    const droneHero = document.querySelector('.drone-video-hero');
    if (droneHero) {
      droneHero.style.setProperty('transform', 'none', 'important');
    }
  });

  window.addEventListener('load', function () {
    initVideoAutoplay();
  });

  // 2. BFcache & history navigation (back/forward)
  window.addEventListener('pageshow', function () {
    initVideoAutoplay();
  });
  window.addEventListener('popstate', function () {
    setTimeout(initVideoAutoplay, 80);
  });

  // 3. MutationObserver on document.body for dynamic container swaps
  let observerThrottle = null;
  const bodyObserver = new MutationObserver(function (mutations) {
    for (let i = 0; i < mutations.length; i++) {
      const added = mutations[i].addedNodes;
      for (let j = 0; j < added.length; j++) {
        const node = added[j];
        if (node.nodeType === 1) {
          if (node.id === 'hero-drone-video' || (node.querySelector && node.querySelector('#hero-drone-video'))) {
            if (!observerThrottle) {
              observerThrottle = setTimeout(function () {
                initVideoAutoplay();
                initStickyScroll();
                initScrollCue();
                observerThrottle = null;
              }, 40);
            }
            return;
          }
        }
      }
    }
  });
  bodyObserver.observe(document.body, { childList: true, subtree: true });

  // 4. Barba.js transition hooks (with retry timer in case Barba is deferred)
  function attachBarbaHooks() {
    if (window.barba && window.barba.hooks) {
      window.barba.hooks.afterEnter(function () {
        closeMenu();
        initDrawerContent();
        initVideoAutoplay();
        initStickyScroll();
        initScrollCue();
      });
      return true;
    }
    return false;
  }
  if (!attachBarbaHooks()) {
    let barbaAttempts = 0;
    const barbaTimer = setInterval(function () {
      barbaAttempts++;
      if (attachBarbaHooks() || barbaAttempts > 30) {
        clearInterval(barbaTimer);
      }
    }, 200);
  }
})();

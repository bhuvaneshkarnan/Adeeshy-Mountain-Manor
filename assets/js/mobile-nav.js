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
  // BULLETPROOF PERSISTENT BACKGROUND MUSIC SYSTEM
  // Audio is ON by default, plays continuously across ALL pages,
  // survives Barba.js PJAX swaps, BFcache, and browser policies.
  // ============================================================

  function getDesiredAudioState() {
    return sessionStorage.getItem('adeeshy_hero_audio') || 'on';
  }

  function setDesiredAudioState(state) {
    sessionStorage.setItem('adeeshy_hero_audio', state);
  }

  // Ensure persistent global <audio> element exists outside <main> on document.body
  function getOrCreateGlobalAudio() {
    let audio = document.getElementById('global-ambient-audio');
    if (!audio) {
      audio = document.createElement('audio');
      audio.id = 'global-ambient-audio';
      audio.src = '/herovideowithaudio.MP4';
      audio.loop = true;
      audio.preload = 'auto';
      audio.style.display = 'none';
      document.body.appendChild(audio);
    }
    return audio;
  }

  // Ensure navbar has the luxury background sound toggle button
  function ensureNavbarSoundToggle() {
    const navBtnGroup = document.querySelector('.button-group_nav');
    if (navBtnGroup && !navBtnGroup.querySelector('#global-sound-toggle')) {
      const toggleBtn = document.createElement('button');
      toggleBtn.id = 'global-sound-toggle';
      toggleBtn.className = 'global-sound-toggle is-unmuted';
      toggleBtn.type = 'button';
      toggleBtn.setAttribute('aria-label', 'Toggle Background Music');
      toggleBtn.setAttribute('title', 'Background Music');
      toggleBtn.innerHTML = `
        <span class="global-sound-icon">
          <svg class="sound-icon-unmuted" viewBox="0 0 24 24" fill="currentColor">
            <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
          </svg>
          <svg class="sound-icon-muted" viewBox="0 0 24 24" fill="currentColor">
            <path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/>
          </svg>
        </span>
        <span class="sound-wave-bars">
          <span class="bar bar-1"></span>
          <span class="bar bar-2"></span>
          <span class="bar bar-3"></span>
        </span>
        <span class="sound-text-label">Music</span>
      `;
      navBtnGroup.insertBefore(toggleBtn, navBtnGroup.firstChild);
    }

    ensureMobileSoundPill();
  }

  // Ensure floating sound pill on mobile subpages
  function ensureMobileSoundPill() {
    let mobilePill = document.getElementById('mobile-sound-pill');
    if (!mobilePill) {
      mobilePill = document.createElement('button');
      mobilePill.id = 'mobile-sound-pill';
      mobilePill.className = 'mobile-sound-pill is-unmuted';
      mobilePill.type = 'button';
      mobilePill.setAttribute('aria-label', 'Toggle Background Music');
      mobilePill.setAttribute('title', 'Background Music');
      mobilePill.innerHTML = `
        <span class="global-sound-icon">
          <svg class="sound-icon-unmuted" viewBox="0 0 24 24" fill="currentColor">
            <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
          </svg>
          <svg class="sound-icon-muted" viewBox="0 0 24 24" fill="currentColor">
            <path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/>
          </svg>
        </span>
        <span class="sound-wave-bars">
          <span class="bar bar-1"></span>
          <span class="bar bar-2"></span>
          <span class="bar bar-3"></span>
        </span>
        <span class="sound-toggle-text">Music</span>
      `;
      document.body.appendChild(mobilePill);
    }

    const isHomePage = document.body.classList.contains('is-home') ||
                       window.location.pathname === '/' ||
                       window.location.pathname === '/en/' ||
                       window.location.pathname === '/index.html' ||
                       !!document.querySelector('.drone-video-hero');
    mobilePill.style.display = isHomePage ? 'none' : '';
  }

  // Synchronize UI across all sound buttons on the page (hero button + navbar button + mobile pill)
  function updateAllSoundUI(isUnmuted) {
    const heroBtn = document.getElementById('hero-sound-toggle');
    const navBtn = document.getElementById('global-sound-toggle');
    const mobilePill = document.getElementById('mobile-sound-pill');

    [heroBtn, navBtn, mobilePill].forEach(function (btn) {
      if (!btn) return;
      if (isUnmuted) {
        btn.classList.add('is-unmuted');
        btn.setAttribute('aria-pressed', 'true');
        const text = btn.querySelector('.sound-toggle-text');
        if (text) text.textContent = btn.id === 'hero-sound-toggle' ? 'Sound On' : 'Music';
      } else {
        btn.classList.remove('is-unmuted');
        btn.setAttribute('aria-pressed', 'false');
        const text = btn.querySelector('.sound-toggle-text');
        if (text) text.textContent = btn.id === 'hero-sound-toggle' ? 'Sound Off' : 'Muted';
      }
    });
  }

  // Toggle Background Audio
  function toggleGlobalAudio() {
    const audio = getOrCreateGlobalAudio();
    const isCurrentlyPlaying = !audio.paused && !audio.muted;

    if (isCurrentlyPlaying) {
      // User requested MUTE
      audio.muted = true;
      audio.pause();
      setDesiredAudioState('off');
      updateAllSoundUI(false);
    } else {
      // User requested UNMUTE
      audio.muted = false;
      audio.volume = 1.0;
      setDesiredAudioState('on');
      audio.play().then(function () {
        updateAllSoundUI(true);
      }).catch(function () {});
      updateAllSoundUI(true);
    }
  }

  // Delegated click handler on document — catches clicks on ANY sound button anywhere on any page!
  document.addEventListener('click', function (e) {
    const toggleBtn = e.target.closest('#hero-sound-toggle, #global-sound-toggle, .global-sound-toggle');
    if (toggleBtn) {
      e.preventDefault();
      e.stopPropagation();
      toggleGlobalAudio();
    }
  });

  // Unlock sound on first user gesture anywhere on page if cold-load autoplay policy deferred audio
  let gestureUnlockAttached = false;
  function setupGestureUnlock() {
    if (gestureUnlockAttached) return;
    gestureUnlockAttached = true;

    const unlockOnGesture = function () {
      if (getDesiredAudioState() === 'on') {
        const audio = getOrCreateGlobalAudio();
        if (audio && (audio.paused || audio.muted)) {
          audio.muted = false;
          audio.volume = 1.0;
          audio.play().then(function () {
            updateAllSoundUI(true);
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

  // Main Audio Controller & Hero Video Manager
  function initGlobalAudioSystem() {
    ensureNavbarSoundToggle();
    const audio = getOrCreateGlobalAudio();
    const desiredState = getDesiredAudioState();

    // Ensure hero drone video visual (if present on homepage) plays muted so it never echoes audio
    const heroVideo = document.getElementById('hero-drone-video') || document.querySelector('video.drone-video-player');
    if (heroVideo) {
      heroVideo.muted = true;
      if (heroVideo.paused) {
        heroVideo.play().catch(function () {});
      }
    }

    if (desiredState === 'off') {
      audio.muted = true;
      audio.pause();
      updateAllSoundUI(false);
      return;
    }

    // Default: Audio ON
    audio.muted = false;
    audio.volume = 1.0;

    if (!audio.paused) {
      // Audio is already playing seamlessly from previous page!
      updateAllSoundUI(true);
      return;
    }

    const playPromise = audio.play();
    if (playPromise !== undefined) {
      playPromise.then(function () {
        updateAllSoundUI(true);
      }).catch(function () {
        // Cold load browser autoplay policy blocked immediate sound without gesture:
        updateAllSoundUI(false);
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
  function onReady() {
    initDrawerContent();
    initGlobalAudioSystem();
    initStickyScroll();
    initScrollCue();

    const droneHero = document.querySelector('.drone-video-hero');
    if (droneHero) {
      droneHero.style.setProperty('transform', 'none', 'important');
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', onReady);
  } else {
    onReady();
  }

  window.addEventListener('load', function () {
    initGlobalAudioSystem();
  });

  // 2. BFcache & history navigation (back/forward)
  window.addEventListener('pageshow', function () {
    initGlobalAudioSystem();
  });
  window.addEventListener('popstate', function () {
    setTimeout(initGlobalAudioSystem, 60);
  });

  // 3. MutationObserver on document.body for dynamic container swaps
  let observerThrottle = null;
  const bodyObserver = new MutationObserver(function (mutations) {
    for (let i = 0; i < mutations.length; i++) {
      const added = mutations[i].addedNodes;
      for (let j = 0; j < added.length; j++) {
        const node = added[j];
        if (node.nodeType === 1) {
          if (node.id === 'hero-drone-video' || (node.querySelector && (node.querySelector('#hero-drone-video') || node.querySelector('.button-group_nav')))) {
            if (!observerThrottle) {
              observerThrottle = setTimeout(function () {
                initGlobalAudioSystem();
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
        initGlobalAudioSystem();
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

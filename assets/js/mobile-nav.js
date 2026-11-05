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
  // HERO SECTION AUDIO ONLY (NO AUDIO OR MUTE ON OTHER PAGES)
  // Audio plays strictly in the home hero section.
  // Mutes when scrolled out of hero or navigating to other pages.
  // ============================================================

  function getDesiredAudioState() {
    return sessionStorage.getItem('adeeshy_hero_audio') || 'on';
  }

  function setDesiredAudioState(state) {
    sessionStorage.setItem('adeeshy_hero_audio', state);
  }

  function removeExtraneousSoundToggles() {
    const strayNavToggle = document.getElementById('global-sound-toggle');
    if (strayNavToggle) strayNavToggle.remove();
    const strayMobilePill = document.getElementById('mobile-sound-pill');
    if (strayMobilePill) strayMobilePill.remove();
    const globalAudio = document.getElementById('global-ambient-audio');
    if (globalAudio) {
      globalAudio.pause();
      globalAudio.muted = true;
      globalAudio.remove();
    }
  }

  function updateHeroSoundUI(isUnmuted) {
    const heroBtn = document.getElementById('hero-sound-toggle');
    if (!heroBtn) return;
    if (isUnmuted) {
      heroBtn.classList.add('is-unmuted');
      heroBtn.setAttribute('aria-pressed', 'true');
      const text = heroBtn.querySelector('.sound-toggle-text');
      if (text) text.textContent = 'Sound On';
    } else {
      heroBtn.classList.remove('is-unmuted');
      heroBtn.setAttribute('aria-pressed', 'false');
      const text = heroBtn.querySelector('.sound-toggle-text');
      if (text) text.textContent = 'Sound Off';
    }
  }

  function toggleHeroAudio() {
    const heroVideo = document.getElementById('hero-drone-video') || document.querySelector('video.drone-video-player');
    if (!heroVideo) return;

    if (heroVideo.muted || heroVideo.paused) {
      heroVideo.muted = false;
      heroVideo.volume = 1.0;
      setDesiredAudioState('on');
      heroVideo.play().then(function () {
        updateHeroSoundUI(true);
      }).catch(function () {});
      updateHeroSoundUI(true);
    } else {
      heroVideo.muted = true;
      setDesiredAudioState('off');
      updateHeroSoundUI(false);
    }
  }

  // Delegated click handler on document strictly for hero sound button
  document.addEventListener('click', function (e) {
    const toggleBtn = e.target.closest('#hero-sound-toggle');
    if (toggleBtn) {
      e.preventDefault();
      e.stopPropagation();
      toggleHeroAudio();
    }
  });

  // Unlock sound on first user gesture anywhere on hero if cold-load autoplay policy deferred audio
  let gestureUnlockAttached = false;
  function setupGestureUnlock(heroVideo) {
    if (gestureUnlockAttached) return;
    gestureUnlockAttached = true;

    const unlockOnGesture = function () {
      if (getDesiredAudioState() === 'on' && heroVideo) {
        if (heroVideo.muted) {
          heroVideo.muted = false;
          heroVideo.volume = 1.0;
          heroVideo.play().then(function () {
            updateHeroSoundUI(true);
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

  let heroObserver = null;

  function initHeroSectionAudio() {
    removeExtraneousSoundToggles();

    const heroSection = document.getElementById('drone-hero') || document.querySelector('.drone-video-hero');
    const heroVideo = document.getElementById('hero-drone-video') || document.querySelector('video.drone-video-player');

    // If NOT in hero section or on another page:
    if (!heroSection || !heroVideo) {
      if (heroObserver) {
        heroObserver.disconnect();
        heroObserver = null;
      }
      return;
    }

    // 1. Kickstart video rendering instantly if paused
    if (heroVideo.paused) {
      heroVideo.play().catch(function () {
        heroVideo.muted = true;
        heroVideo.play().catch(function () {});
      });
    }

    heroVideo.addEventListener('loadeddata', function () {
      if (heroVideo.paused) {
        heroVideo.play().catch(function () {});
      }
    }, { once: true });

    const desiredState = getDesiredAudioState();

    if (desiredState === 'off') {
      heroVideo.muted = true;
      updateHeroSoundUI(false);
    } else {
      // 2. Attempt unmuted audio if allowed by browser MEI/policy
      heroVideo.muted = false;
      heroVideo.volume = 1.0;

      const playPromise = heroVideo.play();
      if (playPromise !== undefined) {
        playPromise.then(function () {
          updateHeroSoundUI(true);
        }).catch(function () {
          // Browser autoplay policy deferred sound until first gesture:
          // Keep video streaming MUTED seamlessly without any stutter!
          heroVideo.muted = true;
          heroVideo.play().catch(function () {});
          updateHeroSoundUI(false);
          setupGestureUnlock(heroVideo);
        });
      }
    }

    // 3. Keep audio playing smoothly across homepage sections on mobile & desktop
    heroVideo.addEventListener('pause', function () {
      const onHomepage = !!(document.getElementById('drone-hero') || document.querySelector('.drone-video-hero'));
      if (onHomepage && getDesiredAudioState() === 'on' && !document.hidden) {
        heroVideo.play().catch(function () {});
      }
    });
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

  // ========================================================
  // 5. ADEESHY UNIVERSAL IN-PAGE IMAGE LIGHTBOX POPUP
  // ========================================================
  let lightboxEl = null;
  let lightboxImg = null;
  let lightboxCaption = null;
  let lightboxCounter = null;
  let lightboxPrevBtn = null;
  let lightboxNextBtn = null;
  let currentGallery = [];
  let currentIndex = 0;
  let touchStartX = 0;
  let touchStartY = 0;

  function ensureLightboxDOM() {
    if (lightboxEl && document.body.contains(lightboxEl)) return;

    const existing = document.getElementById('adeeshy-lightbox');
    if (existing) {
      lightboxEl = existing;
    } else {
      lightboxEl = document.createElement('div');
      lightboxEl.id = 'adeeshy-lightbox';
      lightboxEl.className = 'adeeshy-lightbox-overlay';
      lightboxEl.setAttribute('role', 'dialog');
      lightboxEl.setAttribute('aria-modal', 'true');
      lightboxEl.setAttribute('aria-label', 'Image Lightbox Preview');
      lightboxEl.innerHTML = [
        '<button class="adeeshy-lightbox-close" type="button" aria-label="Close popup">&times;</button>',
        '<button class="adeeshy-lightbox-nav adeeshy-lightbox-prev" type="button" aria-label="Previous image">&#8249;</button>',
        '<button class="adeeshy-lightbox-nav adeeshy-lightbox-next" type="button" aria-label="Next image">&#8250;</button>',
        '<div class="adeeshy-lightbox-container">',
        '  <div class="adeeshy-lightbox-img-wrap">',
        '    <img class="adeeshy-lightbox-img" src="" alt="" loading="eager">',
        '  </div>',
        '  <div class="adeeshy-lightbox-caption"></div>',
        '  <div class="adeeshy-lightbox-counter"></div>',
        '</div>'
      ].join('');
      document.body.appendChild(lightboxEl);
    }

    lightboxImg = lightboxEl.querySelector('.adeeshy-lightbox-img');
    lightboxCaption = lightboxEl.querySelector('.adeeshy-lightbox-caption');
    lightboxCounter = lightboxEl.querySelector('.adeeshy-lightbox-counter');
    lightboxPrevBtn = lightboxEl.querySelector('.adeeshy-lightbox-prev');
    lightboxNextBtn = lightboxEl.querySelector('.adeeshy-lightbox-next');
    const closeBtn = lightboxEl.querySelector('.adeeshy-lightbox-close');

    if (closeBtn) {
      closeBtn.onclick = function (e) {
        e.preventDefault();
        e.stopPropagation();
        closeLightbox();
      };
    }

    if (lightboxPrevBtn) {
      lightboxPrevBtn.onclick = function (e) {
        e.preventDefault();
        e.stopPropagation();
        stepLightbox(-1);
      };
    }
    if (lightboxNextBtn) {
      lightboxNextBtn.onclick = function (e) {
        e.preventDefault();
        e.stopPropagation();
        stepLightbox(1);
      };
    }

    lightboxEl.onclick = function (e) {
      if (e.target === lightboxEl || e.target.classList.contains('adeeshy-lightbox-container') || e.target.classList.contains('adeeshy-lightbox-img-wrap')) {
        closeLightbox();
      }
    };

    lightboxEl.addEventListener('touchstart', function (e) {
      if (e.touches && e.touches.length > 0) {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
      }
    }, { passive: true });

    lightboxEl.addEventListener('touchend', function (e) {
      if (e.changedTouches && e.changedTouches.length > 0) {
        const dx = e.changedTouches[0].clientX - touchStartX;
        const dy = e.changedTouches[0].clientY - touchStartY;
        if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) {
          if (dx < 0) {
            stepLightbox(1);
          } else {
            stepLightbox(-1);
          }
        }
      }
    }, { passive: true });
  }

  window.addEventListener('keydown', function (e) {
    if (!lightboxEl || !lightboxEl.classList.contains('is-open')) return;
    if (e.key === 'Escape' || e.keyCode === 27) {
      closeLightbox();
    } else if (e.key === 'ArrowLeft' || e.keyCode === 37) {
      stepLightbox(-1);
    } else if (e.key === 'ArrowRight' || e.keyCode === 39) {
      stepLightbox(1);
    }
  });

  function openLightbox(items, index) {
    if (!items || items.length === 0) return;
    ensureLightboxDOM();

    currentGallery = items;
    currentIndex = Math.max(0, Math.min(index, items.length - 1));

    updateLightboxDisplay();

    lightboxEl.classList.add('is-open');
    document.body.style.setProperty('overflow', 'hidden', 'important');
  }

  function stepLightbox(delta) {
    if (!currentGallery || currentGallery.length <= 1) return;
    currentIndex = (currentIndex + delta + currentGallery.length) % currentGallery.length;
    updateLightboxDisplay();
  }

  function updateLightboxDisplay() {
    if (!currentGallery[currentIndex]) return;
    const item = currentGallery[currentIndex];

    if (lightboxImg) {
      lightboxImg.style.opacity = '0.35';
      lightboxImg.style.transform = 'scale(0.98)';
      
      const newImg = new Image();
      newImg.onload = function () {
        lightboxImg.src = item.src;
        lightboxImg.alt = item.alt || '';
        lightboxImg.style.opacity = '1';
        lightboxImg.style.transform = 'scale(1)';
      };
      newImg.onerror = function () {
        lightboxImg.src = item.src;
        lightboxImg.style.opacity = '1';
      };
      newImg.src = item.src;
    }

    if (lightboxCaption) {
      lightboxCaption.textContent = item.alt || item.title || '';
      lightboxCaption.style.display = (item.alt || item.title) ? 'block' : 'none';
    }

    if (lightboxCounter) {
      if (currentGallery.length > 1) {
        lightboxCounter.textContent = (currentIndex + 1) + ' / ' + currentGallery.length;
        lightboxCounter.style.display = 'block';
      } else {
        lightboxCounter.style.display = 'none';
      }
    }

    const showNav = currentGallery.length > 1 ? 'flex' : 'none';
    if (lightboxPrevBtn) lightboxPrevBtn.style.display = showNav;
    if (lightboxNextBtn) lightboxNextBtn.style.display = showNav;

    if (currentGallery.length > 1) {
      const nextIdx = (currentIndex + 1) % currentGallery.length;
      const prevIdx = (currentIndex - 1 + currentGallery.length) % currentGallery.length;
      const p1 = new Image(); p1.src = currentGallery[nextIdx].src;
      const p2 = new Image(); p2.src = currentGallery[prevIdx].src;
    }
  }

  function closeLightbox() {
    if (!lightboxEl) return;
    lightboxEl.classList.remove('is-open');
    document.body.style.removeProperty('overflow');
    if (lightboxImg) {
      lightboxImg.src = '';
    }
  }

  function sanitizeImageLinks() {
    const imgLinks = document.querySelectorAll('a[href$=".webp"], a[href$=".jpg"], a[href$=".jpeg"], a[href$=".png"], a[href$=".avif"], a.w-lightbox');
    imgLinks.forEach(function (a) {
      a.removeAttribute('target');
      a.setAttribute('data-lightbox', 'true');
    });
  }

  // Global click interceptor in capture phase
  document.addEventListener('click', function (e) {
    // Check if clicking inside an active lightbox - let lightbox controls handle it
    if (e.target.closest('#adeeshy-lightbox')) return;

    // Detect clickable image triggers
    const link = e.target.closest('a[data-lightbox], a[href$=".webp"], a[href$=".jpg"], a[href$=".jpeg"], a[href$=".png"], a[href$=".avif"], a.w-lightbox');
    const tile = e.target.closest('.room-gallery-tile, .gallery10_item, [data-lightbox-gallery]');
    const clickedImg = e.target.tagName === 'IMG' ? e.target : (link ? link.querySelector('img') : (tile ? tile.querySelector('img') : null));

    if (!link && !tile) {
      return;
    }

    let imgSrc = null;
    let imgAlt = '';

    if (link) {
      const href = link.getAttribute('href') || '';
      if (/\.(webp|jpg|jpeg|png|gif|avif)$/i.test(href)) {
        imgSrc = href;
      }
    }
    if (!imgSrc && clickedImg) {
      imgSrc = clickedImg.getAttribute('src') || clickedImg.currentSrc;
      imgAlt = clickedImg.getAttribute('alt') || '';
    }

    if (!imgSrc) return;

    // Never open in a new tab or navigate!
    e.preventDefault();
    e.stopPropagation();
    if (e.stopImmediatePropagation) e.stopImmediatePropagation();

    // Find context gallery container
    const container = (tile && tile.parentElement) || (link && link.closest('section, .w-layout-grid, [id], .room-overview-section, .gallery10_list')) || document.body;
    const candidates = container.querySelectorAll('.room-gallery-tile, .gallery10_item, a[data-lightbox], a[href$=".webp"], a[href$=".jpg"], a[href$=".jpeg"], a[href$=".png"]');

    let galleryList = [];
    let activeIdx = 0;
    const seenSrcs = new Set();

    if (candidates.length > 1) {
      candidates.forEach(function (c) {
        let s = null;
        let a = '';
        if (c.tagName === 'A') {
          const h = c.getAttribute('href') || '';
          if (/\.(webp|jpg|jpeg|png|gif|avif)$/i.test(h)) s = h;
          const i = c.querySelector('img');
          if (i && !s) s = i.getAttribute('src');
          if (i) a = i.getAttribute('alt') || '';
        } else {
          const i = c.querySelector('img') || (c.tagName === 'IMG' ? c : null);
          if (i) {
            s = i.getAttribute('src') || i.currentSrc;
            a = i.getAttribute('alt') || '';
          }
        }
        if (s && !seenSrcs.has(s)) {
          seenSrcs.add(s);
          galleryList.push({ src: s, alt: a });
        }
      });
    }

    if (galleryList.length === 0) {
      galleryList = [{ src: imgSrc, alt: imgAlt }];
      activeIdx = 0;
    } else {
      activeIdx = galleryList.findIndex(function (item) {
        return item.src === imgSrc || (imgSrc.includes(item.src) || item.src.includes(imgSrc));
      });
      if (activeIdx === -1) activeIdx = 0;
    }

    openLightbox(galleryList, activeIdx);
    return false;
  }, true);

  // 1. DOM ready & window load
  function onReady() {
    initDrawerContent();
    initHeroSectionAudio();
    initStickyScroll();
    initScrollCue();
    sanitizeImageLinks();
    ensureLightboxDOM();

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
    initHeroSectionAudio();
  });

  // 2. BFcache & history navigation (back/forward)
  window.addEventListener('pageshow', function () {
    initHeroSectionAudio();
  });
  window.addEventListener('popstate', function () {
    setTimeout(initHeroSectionAudio, 60);
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
                initHeroSectionAudio();
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
      window.barba.hooks.beforeLeave(function () {
        // Stop hero audio immediately when transitioning to another page
        const heroVideo = document.getElementById('hero-drone-video') || document.querySelector('video.drone-video-player');
        if (heroVideo) {
          heroVideo.pause();
          heroVideo.muted = true;
        }
      });
      window.barba.hooks.afterEnter(function () {
        closeMenu();
        initDrawerContent();
        initHeroSectionAudio();
        initStickyScroll();
        initScrollCue();
        sanitizeImageLinks();
        ensureLightboxDOM();
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

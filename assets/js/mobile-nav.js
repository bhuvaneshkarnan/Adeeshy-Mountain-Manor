/**
 * Adeeshy Mountain Manor - Mobile Navigation Enhancer
 * Provides smooth, reliable mobile drawer toggling with body scroll lock,
 * seamless header synchronization, and quick concierge contact actions.
 */
document.addEventListener('DOMContentLoaded', function () {
  const menuBtn = document.querySelector('.nav-menu-button');
  const navMenu = document.querySelector('.nav-menu');
  const navbar = document.querySelector('.navbar');

  if (!menuBtn || !navMenu) return;

  function openMenu() {
    menuBtn.classList.add('is-active', 'w--open');
    navMenu.classList.add('is-open', 'w--open');
    if (navbar) navbar.classList.add('is-menu-open');
    document.body.classList.add('mobile-nav-open');
    document.documentElement.classList.add('mobile-nav-open');
    navMenu.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    const drawerFooter = navMenu.querySelector('.nav-menu-footer');
    if (drawerFooter) {
      drawerFooter.style.setProperty('opacity', '1', 'important');
      drawerFooter.style.setProperty('visibility', 'visible', 'important');
      drawerFooter.style.setProperty('transform', 'none', 'important');
    }
  }

  function closeMenu() {
    menuBtn.classList.remove('is-active', 'w--open');
    navMenu.classList.remove('is-open', 'w--open');
    if (navbar) navbar.classList.remove('is-menu-open');
    document.body.classList.remove('mobile-nav-open');
    document.documentElement.classList.remove('mobile-nav-open');
    navMenu.style.display = 'none';
    document.body.style.overflow = '';
  }

  menuBtn.addEventListener('click', function (e) {
    e.stopPropagation();
    if (navMenu.classList.contains('is-open') || navMenu.style.display === 'flex') {
      closeMenu();
    } else {
      openMenu();
    }
  });

  // Close menu when clicking backdrop outside menu links
  navMenu.addEventListener('click', function (e) {
    if (e.target === navMenu) {
      closeMenu();
    }
  });

  // Close menu on Escape key
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && navMenu.classList.contains('is-open')) {
      closeMenu();
    }
  });

  // Close menu when clicking navigation links inside drawer (excluding concierge action buttons)
  const navLinks = navMenu.querySelectorAll('a:not(.nav-drawer-quick-btn)');
  navLinks.forEach(function (link) {
    link.addEventListener('click', function () {
      closeMenu();
    });
  });

  // Refine subnav bullet points to elegant gold dashes
  navMenu.querySelectorAll('.nav-sublink').forEach(function(sublink) {
    if (sublink.innerHTML.includes('&bull;') || sublink.innerHTML.includes('•')) {
      sublink.innerHTML = sublink.innerHTML.replace(/(?:&bull;|•)\s*/g, '<span class="subnav-bullet">—</span> ');
    }
  });

  // Ensure quick call, WhatsApp, and location signature exist in drawer footer
  const drawerFooter = navMenu.querySelector('.nav-menu-footer');
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

  // Ensure hero drone video autoplays smoothly across all mobile & desktop browsers
  const heroVideo = document.querySelector('video.drone-video-player');
  if (heroVideo) {
    heroVideo.muted = true;
    const playPromise = heroVideo.play();
    if (playPromise !== undefined) {
      playPromise.catch(function () {
        const triggerAutoplay = function () {
          heroVideo.play().catch(function () {});
          window.removeEventListener('touchstart', triggerAutoplay);
          window.removeEventListener('scroll', triggerAutoplay);
          window.removeEventListener('click', triggerAutoplay);
        };
        window.addEventListener('touchstart', triggerAutoplay, { passive: true, once: true });
        window.addEventListener('scroll', triggerAutoplay, { passive: true, once: true });
        window.addEventListener('click', triggerAutoplay, { passive: true, once: true });
      });
    }
  }

  // Universal Sticky Header Scroll Controller
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

  // Zero-line seamless lock for drone video hero
  const droneHero = document.querySelector('.drone-video-hero');
  if (droneHero) {
    droneHero.style.setProperty('transform', 'none', 'important');
  }
});

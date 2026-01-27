(function() {
  'use strict';

  // Enhance question items with additional features
  function enhanceQuestions() {
    // Get all ordered list items in main content
    const mainContent = document.querySelector('.main-content');
    if (!mainContent) return;

    const orderedLists = mainContent.querySelectorAll('ol');
    
    orderedLists.forEach(list => {
      // Only target direct children ordered lists (top-level questions)
      if (list.parentElement === mainContent || list.parentElement.classList.contains('main-content')) {
        const items = list.querySelectorAll('li');
        
        items.forEach((item, index) => {
          // Add question-item class for easier styling
          item.classList.add('question-item');
          
          // Add data attribute for question number
          item.setAttribute('data-question-number', index + 1);
          
          // Enhance filename references
          const brElements = item.querySelectorAll('br');
          brElements.forEach(br => {
            const nextNode = br.nextSibling;
            if (nextNode && nextNode.nodeType === Node.TEXT_NODE) {
              const text = nextNode.textContent.trim();
              if (text.startsWith('[Filename')) {
                // Wrap filename in a span for better styling
                const span = document.createElement('span');
                span.className = 'filename-reference';
                span.textContent = text;
                // Insert span and remove original text node
                nextNode.parentNode.insertBefore(span, nextNode);
                nextNode.remove();
              }
            }
          });
        });
      }
    });
  }

  // Add smooth scroll padding for anchor links
  function enhanceAnchorLinks() {
    // Get header height from CSS custom property
    const headerHeightStr = getComputedStyle(document.documentElement)
      .getPropertyValue('--header-height') || '70px';
    const headerHeight = parseInt(headerHeightStr);
    const offset = headerHeight + 10; // Header height + padding
    
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;
        
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
          window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
          });
        }
      });
    });
  }

  // Add scroll progress indicator
  function addScrollProgress() {
    // Get header height from CSS custom property
    const headerHeight = getComputedStyle(document.documentElement)
      .getPropertyValue('--header-height') || '70px';
    
    const progressBar = document.createElement('div');
    progressBar.className = 'scroll-progress';
    progressBar.style.cssText = `
      position: fixed;
      top: ${headerHeight};
      left: 0;
      width: 0%;
      height: 3px;
      background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
      z-index: 1001;
      transition: width 0.1s ease;
    `;
    document.body.appendChild(progressBar);

    window.addEventListener('scroll', () => {
      const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (window.pageYOffset / windowHeight) * 100;
      progressBar.style.width = scrolled + '%';
    });
  }

  // Initialize enhancements when DOM is ready
  function init() {
    enhanceQuestions();
    enhanceAnchorLinks();
    addScrollProgress();
  }

  // Run initialization
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

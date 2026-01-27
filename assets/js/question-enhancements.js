(function() {
  'use strict';

  // Utility function to get header height from CSS
  function getHeaderHeight() {
    const headerHeightStr = getComputedStyle(document.documentElement)
      .getPropertyValue('--header-height') || '70px';
    // Remove 'px' and parse as integer
    return parseInt(headerHeightStr.replace('px', ''), 10) || 70;
  }

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
    const headerHeight = getHeaderHeight();
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
    const headerHeight = getHeaderHeight();
    
    const progressBar = document.createElement('div');
    progressBar.className = 'scroll-progress';
    progressBar.style.top = headerHeight + 'px';
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

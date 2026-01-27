(function() {
  'use strict';

  // Configuration
  const COLLAPSE_STATE_KEY = 'status-table-collapsed';
  const STATUS_TABLE_HEADING = '📘 Status';
  
  // Find the status table heading and its table
  function findStatusTable() {
    const headings = document.querySelectorAll('h1, h2, h3');
    let statusHeading = null;
    
    for (const heading of headings) {
      if (heading.textContent.includes(STATUS_TABLE_HEADING)) {
        statusHeading = heading;
        break;
      }
    }
    
    if (!statusHeading) {
      return null;
    }
    
    // Find the next table after the heading
    let nextElement = statusHeading.nextElementSibling;
    while (nextElement) {
      if (nextElement.tagName === 'TABLE') {
        return { heading: statusHeading, table: nextElement };
      }
      nextElement = nextElement.nextElementSibling;
    }
    
    return null;
  }
  
  // Create collapsible wrapper
  function createCollapsibleWrapper(heading, table) {
    // Create wrapper div
    const wrapper = document.createElement('div');
    wrapper.className = 'collapsible-section';
    
    // Create header button
    const headerButton = document.createElement('button');
    headerButton.className = 'collapsible-header';
    headerButton.setAttribute('aria-expanded', 'false');
    headerButton.setAttribute('aria-label', 'Toggle status table visibility');
    
    const headerText = document.createElement('span');
    headerText.className = 'collapsible-title';
    headerText.textContent = STATUS_TABLE_HEADING;
    
    const headerIcon = document.createElement('span');
    headerIcon.className = 'collapsible-icon';
    headerIcon.textContent = '▼';
    
    headerButton.appendChild(headerText);
    headerButton.appendChild(headerIcon);
    
    // Create content wrapper
    const contentWrapper = document.createElement('div');
    contentWrapper.className = 'collapsible-content';
    contentWrapper.style.maxHeight = '0';
    contentWrapper.style.overflow = 'hidden';
    
    // Create inner content div for proper animation
    const innerContent = document.createElement('div');
    innerContent.className = 'collapsible-inner';
    
    // Move table into wrapper instead of cloning
    innerContent.appendChild(table);
    contentWrapper.appendChild(innerContent);
    
    // Insert wrapper before heading
    heading.parentNode.insertBefore(wrapper, heading);
    wrapper.appendChild(headerButton);
    wrapper.appendChild(contentWrapper);
    
    // Remove original heading (table already moved)
    heading.remove();
    
    return { wrapper, headerButton, contentWrapper, headerIcon };
  }
  
  // Toggle collapse state
  function toggleCollapse(headerButton, contentWrapper, headerIcon, save = true) {
    const isExpanded = headerButton.getAttribute('aria-expanded') === 'true';
    
    if (isExpanded) {
      // Collapse
      contentWrapper.style.maxHeight = '0';
      headerButton.setAttribute('aria-expanded', 'false');
      headerIcon.textContent = '▼';
      headerButton.classList.remove('expanded');
      
      if (save) {
        localStorage.setItem(COLLAPSE_STATE_KEY, 'collapsed');
      }
    } else {
      // Expand
      const innerContent = contentWrapper.querySelector('.collapsible-inner');
      const height = innerContent.scrollHeight;
      contentWrapper.style.maxHeight = height + 'px';
      headerButton.setAttribute('aria-expanded', 'true');
      headerIcon.textContent = '▲';
      headerButton.classList.add('expanded');
      
      if (save) {
        localStorage.setItem(COLLAPSE_STATE_KEY, 'expanded');
      }
    }
  }
  
  // Get saved collapse state
  function getSavedState() {
    return localStorage.getItem(COLLAPSE_STATE_KEY) || 'collapsed';
  }
  
  // Initialize collapsible table
  function initCollapsibleTable() {
    const statusTableData = findStatusTable();
    
    if (!statusTableData) {
      return; // Status table not found
    }
    
    const { heading, table } = statusTableData;
    const { wrapper, headerButton, contentWrapper, headerIcon } = createCollapsibleWrapper(heading, table);
    
    // Add click event
    headerButton.addEventListener('click', function() {
      toggleCollapse(headerButton, contentWrapper, headerIcon, true);
    });
    
    // Keyboard accessibility
    headerButton.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleCollapse(headerButton, contentWrapper, headerIcon, true);
      }
    });
    
    // Apply saved state (default collapsed)
    const savedState = getSavedState();
    if (savedState === 'expanded') {
      // Small delay to ensure DOM is ready
      setTimeout(() => {
        toggleCollapse(headerButton, contentWrapper, headerIcon, false);
      }, 100);
    }
    
    // Handle window resize for expanded state
    window.addEventListener('resize', function() {
      if (headerButton.getAttribute('aria-expanded') === 'true') {
        const innerContent = contentWrapper.querySelector('.collapsible-inner');
        contentWrapper.style.maxHeight = innerContent.scrollHeight + 'px';
      }
    });
  }
  
  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCollapsibleTable);
  } else {
    initCollapsibleTable();
  }
})();

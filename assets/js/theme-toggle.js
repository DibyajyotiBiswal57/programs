(function () {
  "use strict";

  // Theme constants
  const THEME_KEY = "site-theme";
  const THEME_DARK = "dark";
  const THEME_LIGHT = "light";

  // Get elements
  const toggleButton = document.getElementById("theme-toggle");
  if (!toggleButton) {
    console.warn("Theme toggle button not found");
    return;
  }
  const toggleIcon = toggleButton.querySelector(".theme-toggle-icon");

  // Get saved theme or default to dark
  function getSavedTheme() {
    return localStorage.getItem(THEME_KEY) || THEME_DARK;
  }

  // Save theme to localStorage
  function saveTheme(theme) {
    localStorage.setItem(THEME_KEY, theme);
  }

  // Apply theme to document
  function applyTheme(theme, animate = true) {
    const root = document.documentElement;

    // Add transition class for smooth animation
    if (animate) {
      root.classList.add("theme-transitioning");
    }

    // Set data attribute for theme
    root.setAttribute("data-theme", theme);

    // Update toggle icon with animation
    if (toggleIcon) {
      toggleIcon.style.transform = "rotate(360deg)";
      setTimeout(() => {
        toggleIcon.textContent = theme === THEME_DARK ? "🌙" : "☀️";
        toggleIcon.style.transform = "rotate(0deg)";
      }, 150);
    }

    // Remove transition class after animation
    if (animate) {
      setTimeout(() => {
        root.classList.remove("theme-transitioning");
      }, 300);
    }
  }

  // Toggle between themes
  function toggleTheme() {
    const currentTheme =
      document.documentElement.getAttribute("data-theme") || THEME_DARK;
    const newTheme = currentTheme === THEME_DARK ? THEME_LIGHT : THEME_DARK;

    applyTheme(newTheme, true);
    saveTheme(newTheme);
  }

  // Initialize theme on page load
  function initTheme() {
    const savedTheme = getSavedTheme();
    applyTheme(savedTheme, false);
  }

  // Add event listener to toggle button
  toggleButton.addEventListener("click", toggleTheme);

  // Keyboard accessibility
  toggleButton.addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      toggleTheme();
    }
  });

  // Initialize on DOMContentLoaded
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initTheme);
  } else {
    initTheme();
  }

  // Add page load animation
  window.addEventListener("load", function () {
    document.body.classList.add("page-loaded");
  });
})();

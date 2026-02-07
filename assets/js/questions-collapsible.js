(function () {
  "use strict";

  // Configuration
  const COLLAPSE_STATE_PREFIX = "question-collapsed-";
  const REPO_BASE_URL = "https://github.com/DibyajyotiBiswal57/programs/blob/main";

  // Language configuration matching update_status.py
  const LANGUAGES = [
    { folder: "qbasic", name: "QBasic", ext: "bas" },
    { folder: "java", name: "Java", ext: "java" },
    { folder: "python", name: "Python", ext: "py" },
    { folder: "c", name: "C", ext: "c" },
    { folder: "cpp", name: "C++", ext: "cpp" },
    { folder: "csharp", name: "C#", ext: "cs" },
    { folder: "haskell", name: "Haskell", ext: "hs" },
    { folder: "perl", name: "Perl", ext: "pl" },
    { folder: "go", name: "Go", ext: "go" },
    { folder: "elixir", name: "Elixir", ext: "exs" },
    { folder: "asm", name: "Assembly", ext: "asm" },
    { folder: "fortran", name: "Fortran", ext: "f90" },
    { folder: "lua", name: "Lua", ext: "lua" },
    { folder: "ruby", name: "Ruby", ext: "rb" },
    { folder: "vb", name: "Visual Basic", ext: "vb" },
    { folder: "pwsh", name: "PowerShell", ext: "ps1" },
    { folder: "batch", name: "Batch", ext: "bat" },
  ];

  /**
   * Extract question number and filename from a list item
   * @param {HTMLElement} listItem - The list item element
   * @returns {Object|null} - Object with questionNum and filename, or null
   */
  function extractQuestionInfo(listItem) {
    const text = listItem.textContent;

    // Extract question number (format: "1. ", "2. ", etc.)
    const questionMatch = text.match(/^(\d+)\.\s+/);
    if (!questionMatch) return null;

    const questionNum = parseInt(questionMatch[1], 10);

    // Extract filename from [Filename - XXXX_name] pattern
    const filenameMatch = text.match(/\[Filename\s*-\s*(\w+)\]/i);
    if (!filenameMatch) return null;

    const filename = filenameMatch[1];

    return { questionNum, filename };
  }

  /**
   * Check if a file exists by making a HEAD request
   * We'll assume files exist based on common patterns
   * @param {string} folder - Language folder
   * @param {string} filename - Base filename
   * @param {string} ext - File extension
   * @returns {string} - "done", "beta", or "missing"
   */
  function getFileStatus(folder, filename, ext) {
    // This is a simplified version - in reality, we'd need to check
    // In this implementation, we'll assume files exist and check for beta/wip patterns
    // The actual status would be determined by the server
    // For now, we'll just return "done" as a placeholder
    // The real implementation would require server-side data or API
    return "done"; // Placeholder
  }

  /**
   * Generate Shields.io badge URL
   * @param {string} status - Status type ("done", "beta", "missing")
   * @param {string} folder - Language folder
   * @param {string} filename - Base filename
   * @param {string} ext - File extension
   * @returns {string} - HTML for badge
   */
  function generateBadge(status, folder, filename, ext) {
    const badgeConfig = {
      done: { label: "done", color: "brightgreen" },
      beta: { label: "beta", color: "yellow" },
      missing: { label: "missing", color: "lightgrey" },
    };

    const config = badgeConfig[status] || badgeConfig.missing;
    const badgeUrl = `https://img.shields.io/badge/${config.label}-${config.label}-${config.color}`;

    if (status === "missing") {
      return `<img src="${badgeUrl}" alt="${status}" style="display: inline-block; margin: 2px;">`;
    }

    const fileUrl = `${REPO_BASE_URL}/${folder}/${filename}.${ext}`;
    return `<a href="${fileUrl}" target="_blank" rel="noopener noreferrer"><img src="${badgeUrl}" alt="${status}" style="display: inline-block; margin: 2px;"></a>`;
  }

  /**
   * Generate HTML table for a specific question showing all language implementations
   * @param {string} filename - Base filename (e.g., "0001_hello_world")
   * @returns {string} - HTML string for the table
   */
  function generateLanguageTable(filename) {
    let html = `
      <!DOCTYPE html>
      <html>
      <head>
        <meta charset="UTF-8">
        <style>
          * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
          }
          body {
            font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            font-size: 13px;
            background: transparent;
            color: #e3f0ff;
          }
          table {
            width: 100%;
            border-collapse: collapse;
            background: transparent;
          }
          th {
            background: rgba(17, 24, 36, 0.6);
            color: #e8f4ff;
            padding: 8px 10px;
            text-align: center;
            font-weight: 600;
            font-size: 12px;
            border: 1px solid #2d3b54;
            white-space: nowrap;
          }
          td {
            padding: 8px 10px;
            text-align: center;
            border: 1px solid #2d3b54;
            background: rgba(10, 15, 26, 0.4);
          }
          a {
            text-decoration: none;
            transition: opacity 0.2s ease;
          }
          a:hover {
            opacity: 0.8;
          }
          img {
            vertical-align: middle;
            max-width: 100%;
            height: auto;
          }
          @media (prefers-color-scheme: light) {
            body {
              color: #1a2942;
            }
            th {
              background: rgba(240, 246, 255, 0.8);
              color: #1a2942;
              border-color: #c5d5e8;
            }
            td {
              background: rgba(248, 251, 255, 0.6);
              border-color: #c5d5e8;
            }
          }
        </style>
      </head>
      <body>
        <table>
          <thead>
            <tr>`;

    // Add header row with language names
    LANGUAGES.forEach((lang) => {
      html += `<th>${lang.name}</th>`;
    });

    html += `
            </tr>
          </thead>
          <tbody>
            <tr>`;

    // Add data row with badges
    LANGUAGES.forEach((lang) => {
      const status = getFileStatus(lang.folder, filename, lang.ext);
      const badge = generateBadge(status, lang.folder, filename, lang.ext);
      html += `<td>${badge}</td>`;
    });

    html += `
            </tr>
          </tbody>
        </table>
      </body>
      </html>`;

    return html;
  }

  /**
   * Create collapsible wrapper for a question
   * @param {HTMLElement} listItem - The list item to wrap
   * @param {Object} info - Question info (questionNum, filename)
   * @returns {HTMLElement} - The created wrapper
   */
  function createCollapsibleQuestion(listItem, info) {
    const { questionNum, filename } = info;

    // Create wrapper
    const wrapper = document.createElement("div");
    wrapper.className = "question-collapsible";
    wrapper.setAttribute("data-question-num", questionNum);

    // Create header button
    const headerButton = document.createElement("button");
    headerButton.className = "question-collapsible-header";
    headerButton.setAttribute("aria-expanded", "false");
    headerButton.setAttribute(
      "aria-label",
      `Toggle details for question ${questionNum}`
    );

    // Create header content
    const headerContent = document.createElement("div");
    headerContent.className = "question-header-content";

    const questionText = document.createElement("span");
    questionText.className = "question-text";
    // Get the question text (everything before the filename reference)
    const textContent = listItem.textContent;
    const filenameIndex = textContent.indexOf("[Filename");
    questionText.textContent =
      filenameIndex > 0
        ? textContent.substring(0, filenameIndex).trim()
        : textContent.trim();

    const filenameSpan = document.createElement("span");
    filenameSpan.className = "question-filename";
    filenameSpan.textContent = `[Filename - ${filename}]`;

    headerContent.appendChild(questionText);
    headerContent.appendChild(filenameSpan);

    const headerIcon = document.createElement("span");
    headerIcon.className = "question-collapsible-icon";
    headerIcon.textContent = "▼";

    headerButton.appendChild(headerContent);
    headerButton.appendChild(headerIcon);

    // Create content wrapper
    const contentWrapper = document.createElement("div");
    contentWrapper.className = "question-collapsible-content";
    contentWrapper.style.maxHeight = "0";
    contentWrapper.style.overflow = "hidden";

    // Create iframe
    const iframe = document.createElement("iframe");
    iframe.className = "question-language-table";
    iframe.setAttribute("scrolling", "no");
    iframe.setAttribute("frameborder", "0");
    iframe.style.width = "100%";
    iframe.style.border = "none";
    iframe.style.display = "block";

    // Generate and set iframe content
    const tableHtml = generateLanguageTable(filename);
    iframe.srcdoc = tableHtml;

    // Set iframe height after content loads
    iframe.addEventListener("load", function () {
      try {
        const iframeDoc =
          iframe.contentDocument || iframe.contentWindow.document;
        const height = iframeDoc.body.scrollHeight;
        iframe.style.height = height + "px";
      } catch (e) {
        // Fallback height if we can't access iframe content
        iframe.style.height = "80px";
      }
    });

    contentWrapper.appendChild(iframe);

    // Assemble wrapper
    wrapper.appendChild(headerButton);
    wrapper.appendChild(contentWrapper);

    return { wrapper, headerButton, contentWrapper, headerIcon };
  }

  /**
   * Toggle collapse state
   * @param {HTMLElement} headerButton - Header button element
   * @param {HTMLElement} contentWrapper - Content wrapper element
   * @param {HTMLElement} headerIcon - Icon element
   * @param {number} questionNum - Question number for localStorage
   * @param {boolean} save - Whether to save state to localStorage
   */
  function toggleCollapse(
    headerButton,
    contentWrapper,
    headerIcon,
    questionNum,
    save = true
  ) {
    const isExpanded = headerButton.getAttribute("aria-expanded") === "true";

    if (isExpanded) {
      // Collapse
      contentWrapper.style.maxHeight = "0";
      headerButton.setAttribute("aria-expanded", "false");
      headerIcon.textContent = "▼";
      headerButton.classList.remove("expanded");

      if (save) {
        localStorage.setItem(COLLAPSE_STATE_PREFIX + questionNum, "collapsed");
      }
    } else {
      // Expand
      const iframe = contentWrapper.querySelector("iframe");
      // Add some extra height for padding
      const height = iframe.offsetHeight + 20;
      contentWrapper.style.maxHeight = height + "px";
      headerButton.setAttribute("aria-expanded", "true");
      headerIcon.textContent = "▲";
      headerButton.classList.add("expanded");

      if (save) {
        localStorage.setItem(COLLAPSE_STATE_PREFIX + questionNum, "expanded");
      }
    }
  }

  /**
   * Get saved collapse state for a question
   * @param {number} questionNum - Question number
   * @returns {string} - "collapsed" or "expanded"
   */
  function getSavedState(questionNum) {
    return (
      localStorage.getItem(COLLAPSE_STATE_PREFIX + questionNum) || "collapsed"
    );
  }

  /**
   * Initialize collapsible questions
   */
  function initCollapsibleQuestions() {
    // Only run on questions.md page
    if (!document.location.pathname.includes("questions")) {
      return;
    }

    const mainContent = document.querySelector(".main-content");
    if (!mainContent) return;

    const orderedLists = mainContent.querySelectorAll("ol");

    orderedLists.forEach((list) => {
      // Only target direct children ordered lists (top-level questions)
      if (
        list.parentElement === mainContent ||
        list.parentElement.classList.contains("main-content")
      ) {
        const items = Array.from(list.querySelectorAll("li"));

        items.forEach((item) => {
          const info = extractQuestionInfo(item);
          if (!info) return;

          const { wrapper, headerButton, contentWrapper, headerIcon } =
            createCollapsibleQuestion(item, info);

          // Add click event
          headerButton.addEventListener("click", function () {
            toggleCollapse(
              headerButton,
              contentWrapper,
              headerIcon,
              info.questionNum,
              true
            );
          });

          // Keyboard accessibility
          headerButton.addEventListener("keydown", function (e) {
            if (e.key === "Enter" || e.key === " ") {
              e.preventDefault();
              toggleCollapse(
                headerButton,
                contentWrapper,
                headerIcon,
                info.questionNum,
                true
              );
            }
          });

          // Replace original list item with wrapper
          item.parentNode.insertBefore(wrapper, item);
          item.remove();

          // Apply saved state (default collapsed)
          const savedState = getSavedState(info.questionNum);
          if (savedState === "expanded") {
            // Small delay to ensure iframe is loaded
            setTimeout(() => {
              toggleCollapse(
                headerButton,
                contentWrapper,
                headerIcon,
                info.questionNum,
                false
              );
            }, 200);
          }
        });
      }
    });
  }

  // Initialize when DOM is ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initCollapsibleQuestions);
  } else {
    initCollapsibleQuestions();
  }
})();

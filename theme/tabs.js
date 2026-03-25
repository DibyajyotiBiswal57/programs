/* mdBook dual-tab navigation: Programs and Wiki */
(function () {
    "use strict";

    function initTabs() {
        var sidebar = document.querySelector(".sidebar-scrollbox");
        if (!sidebar) return;

        var chapter = sidebar.querySelector(".chapter");
        if (!chapter) return;

        var items = Array.prototype.slice.call(chapter.children);
        var partTitles = items.filter(function (li) {
            return li.classList.contains("part-title");
        });

        if (partTitles.length < 2) return;

        // Group sidebar items by part section
        var parts = [];
        var currentPart = null;
        items.forEach(function (item) {
            if (item.classList.contains("part-title")) {
                currentPart = { title: item, items: [] };
                parts.push(currentPart);
            } else if (currentPart) {
                currentPart.items.push(item);
            }
        });

        // Determine active part: prefer the one containing the currently active link
        var activePart = 0;
        var activeLink = chapter.querySelector("a.active");
        if (activeLink) {
            parts.forEach(function (part, i) {
                if (
                    part.items.some(function (item) {
                        return item.contains(activeLink);
                    })
                ) {
                    activePart = i;
                }
            });
        } else {
            var saved = localStorage.getItem("mdbook-active-tab");
            if (typeof saved === "string" && saved !== "") {
                var idx = parseInt(saved, 10);
                if (!isNaN(idx) && idx >= 0 && idx < parts.length) {
                    activePart = idx;
                }
            }
        }

        // Build tab bar
        var tabBar = document.createElement("div");
        tabBar.className = "tab-bar";

        parts.forEach(function (part, i) {
            var btn = document.createElement("button");
            btn.className = "tab-btn" + (i === activePart ? " active" : "");
            btn.textContent = part.title.textContent.trim();
            btn.dataset.tab = i;

            btn.addEventListener("click", function () {
                var tabIndex = parseInt(this.dataset.tab, 10);
                localStorage.setItem("mdbook-active-tab", tabIndex);

                // Update button states
                tabBar.querySelectorAll(".tab-btn").forEach(function (b) {
                    b.classList.toggle("active", parseInt(b.dataset.tab, 10) === tabIndex);
                });

                // Show/hide part sections
                parts.forEach(function (p, j) {
                    var visible = j === tabIndex;
                    p.title.style.display = visible ? "" : "none";
                    p.items.forEach(function (item) {
                        item.style.display = visible ? "" : "none";
                    });
                });
            });

            tabBar.appendChild(btn);
        });

        // Hide non-active parts on load
        parts.forEach(function (part, i) {
            if (i !== activePart) {
                part.title.style.display = "none";
                part.items.forEach(function (item) {
                    item.style.display = "none";
                });
            }
        });

        // Insert tab bar before the chapter list
        sidebar.insertBefore(tabBar, sidebar.firstChild);
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initTabs);
    } else {
        initTabs();
    }
})();

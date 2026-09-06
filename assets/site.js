(function () {
  const root = document.documentElement;
  const themeButton = document.querySelector("[data-theme-toggle]");
  const menuButton = document.querySelector("[data-menu-toggle]");
  const nav = document.querySelector("[data-site-nav]");

  let storedTheme = null;
  try {
    storedTheme = localStorage.getItem("site-theme");
  } catch (_) {
    // Theme persistence is optional when browser storage is unavailable.
  }
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  if (storedTheme === "dark" || (!storedTheme && prefersDark)) {
    root.dataset.theme = "dark";
  }

  function syncThemeLabel() {
    if (!themeButton) return;
    const dark = root.dataset.theme === "dark";
    themeButton.setAttribute("aria-label", dark ? "Use light theme" : "Use dark theme");
    themeButton.textContent = dark ? "☀" : "◐";
  }

  syncThemeLabel();

  themeButton?.addEventListener("click", function () {
    const dark = root.dataset.theme === "dark";
    if (dark) {
      delete root.dataset.theme;
    } else {
      root.dataset.theme = "dark";
    }
    syncThemeLabel();
    try {
      localStorage.setItem("site-theme", dark ? "light" : "dark");
    } catch (_) {
      // Keep the selected theme for this page even if it cannot be saved.
    }
  });

  const header = document.querySelector(".site-header");
  const toolbar = document.querySelector(".toolbar");

  function syncStickyOffsets() {
    const headerHeight = header?.getBoundingClientRect().height || 0;
    const toolbarHeight = toolbar?.getBoundingClientRect().height || 0;
    root.style.setProperty("--header-height", headerHeight + "px");
    root.style.setProperty("--sticky-offset", headerHeight + toolbarHeight + "px");
  }

  syncStickyOffsets();
  if (typeof ResizeObserver !== "undefined") {
    const stickyObserver = new ResizeObserver(syncStickyOffsets);
    if (header) stickyObserver.observe(header);
    if (toolbar) stickyObserver.observe(toolbar);
  } else {
    window.addEventListener("resize", syncStickyOffsets);
  }

  window.addEventListener("load", function () {
    syncStickyOffsets();
    // Re-align the initial deep link after fonts have set the toolbar height.
    if (!window.location.hash) return;
    let target;
    try {
      target = document.getElementById(decodeURIComponent(window.location.hash.slice(1)));
    } catch (_) {
      return;
    }
    target?.scrollIntoView({ behavior: "instant" });
  });

  function syncMenuState(open) {
    if (!menuButton) return;
    menuButton.setAttribute("aria-expanded", String(open));
    menuButton.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");
  }

  menuButton?.addEventListener("click", function () {
    const open = nav?.classList.toggle("is-open") || false;
    syncMenuState(open);
  });

  nav?.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
      nav.classList.remove("is-open");
      syncMenuState(false);
    });
  });

  document.addEventListener("keydown", function (event) {
    if (event.key !== "Escape" || !nav?.classList.contains("is-open")) return;
    nav.classList.remove("is-open");
    syncMenuState(false);
    menuButton?.focus();
  });

  const filterButtons = Array.from(document.querySelectorAll("[data-filter]"));
  const search = document.querySelector("[data-search]");
  const items = Array.from(document.querySelectorAll("[data-catalog-item]"));
  const empty = document.querySelector("[data-empty-state]");
  const resultsStatus = document.querySelector("[data-results-status]");
  let activeFilter = "all";

  function updateCatalog() {
    const query = (search?.value || "").trim().toLowerCase();
    let visible = 0;

    items.forEach(function (item) {
      const categories = (item.dataset.category || "").split(" ");
      const matchesFilter = activeFilter === "all" || categories.includes(activeFilter);
      const matchesQuery = !query || item.textContent.toLowerCase().includes(query);
      item.hidden = !(matchesFilter && matchesQuery);
      if (!item.hidden) visible += 1;
    });

    document.querySelectorAll("[data-year-group]").forEach(function (group) {
      const hasVisible = Array.from(group.querySelectorAll("[data-catalog-item]")).some(function (item) {
        return !item.hidden;
      });
      group.hidden = !hasVisible;
    });

    if (empty) empty.hidden = visible !== 0;
    if (resultsStatus) {
      resultsStatus.textContent = visible + (visible === 1 ? " result" : " results") + " shown.";
    }
  }

  filterButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      activeFilter = button.dataset.filter || "all";
      filterButtons.forEach(function (candidate) {
        const selected = candidate === button;
        candidate.classList.toggle("is-active", selected);
        candidate.setAttribute("aria-pressed", String(selected));
      });
      updateCatalog();
    });
  });

  search?.addEventListener("input", updateCatalog);
  if (items.length) updateCatalog();

  document.querySelectorAll("[data-copy]").forEach(function (button) {
    button.addEventListener("click", async function () {
      const value = button.dataset.copy || "";
      const original = button.textContent;
      try {
        await navigator.clipboard.writeText(value);
        button.textContent = "Copied";
      } catch (_) {
        button.textContent = "Select";
        const code = button.parentElement?.querySelector("code");
        const selection = window.getSelection();
        if (code && selection) {
          const range = document.createRange();
          range.selectNodeContents(code);
          selection.removeAllRanges();
          selection.addRange(range);
        }
      }
      window.setTimeout(function () {
        button.textContent = original;
      }, 1500);
    });
  });

  document.querySelectorAll("[data-current-year]").forEach(function (node) {
    node.textContent = new Date().getFullYear();
  });
})();

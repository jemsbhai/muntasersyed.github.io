(function () {
  const root = document.documentElement;
  const themeButton = document.querySelector("[data-theme-toggle]");
  const menuButton = document.querySelector("[data-menu-toggle]");
  const nav = document.querySelector("[data-site-nav]");

  const storedTheme = localStorage.getItem("site-theme");
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
      localStorage.setItem("site-theme", "light");
    } else {
      root.dataset.theme = "dark";
      localStorage.setItem("site-theme", "dark");
    }
    syncThemeLabel();
  });

  menuButton?.addEventListener("click", function () {
    const open = nav?.classList.toggle("is-open") || false;
    menuButton.setAttribute("aria-expanded", String(open));
  });

  nav?.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
      nav.classList.remove("is-open");
      menuButton?.setAttribute("aria-expanded", "false");
    });
  });

  const filterButtons = Array.from(document.querySelectorAll("[data-filter]"));
  const search = document.querySelector("[data-search]");
  const items = Array.from(document.querySelectorAll("[data-catalog-item]"));
  const empty = document.querySelector("[data-empty-state]");
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

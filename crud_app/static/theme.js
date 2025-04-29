// This script is maintained for backward compatibility
// and now delegates theme handling to sidebar.js
function toggleTheme() {
  const themeToggleBtn = document.getElementById("themeToggleBtn");
  if (themeToggleBtn) {
    // Trigger click on the new theme toggle button
    themeToggleBtn.click();
  } else {
    // Fallback for pages that might not have the new button
    const htmlElement = document.documentElement;
    const currentTheme = htmlElement.getAttribute("data-bs-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";
    htmlElement.setAttribute("data-bs-theme", newTheme);
    localStorage.setItem("theme", newTheme);
  }
}

function loadTheme() {
  const savedTheme = localStorage.getItem("theme") || "light";
  const htmlElement = document.documentElement;

  // Just set the theme, don't try to find the old icon
  htmlElement.setAttribute("data-bs-theme", savedTheme);

  // Legacy icon handling (if it exists)
  const themeIcon = document.getElementById("theme-icon");
  if (themeIcon) {
    if (savedTheme === "dark") {
      themeIcon.classList.remove("bi-sun");
      themeIcon.classList.add("bi-moon");
    } else {
      themeIcon.classList.remove("bi-moon");
      themeIcon.classList.add("bi-sun");
    }
  }
}

// Load theme on page load
window.addEventListener("DOMContentLoaded", loadTheme);

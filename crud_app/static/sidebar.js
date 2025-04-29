document.addEventListener("DOMContentLoaded", function () {
  // Eliminada la lógica de sidebar desplegable para simplificar

  // Theme toggle functionality
  const themeToggleBtn = document.getElementById("themeToggleBtn");
  const htmlElement = document.documentElement;
  const themeIconLight = document.querySelector(".theme-icon-light");
  const themeIconDark = document.querySelector(".theme-icon-dark");

  // Check saved theme
  const savedTheme = localStorage.getItem("theme") || "light";
  htmlElement.setAttribute("data-bs-theme", savedTheme);

  // Update icons based on current theme
  if (savedTheme === "dark") {
    themeIconLight.classList.add("d-none");
    themeIconDark.classList.remove("d-none");
  } else {
    themeIconLight.classList.remove("d-none");
    themeIconDark.classList.add("d-none");
  }

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener("click", function () {
      const currentTheme = htmlElement.getAttribute("data-bs-theme");
      const newTheme = currentTheme === "dark" ? "light" : "dark";

      htmlElement.setAttribute("data-bs-theme", newTheme);
      localStorage.setItem("theme", newTheme);

      // Toggle visibility of theme icons
      themeIconLight.classList.toggle("d-none");
      themeIconDark.classList.toggle("d-none");
    });
  }
});

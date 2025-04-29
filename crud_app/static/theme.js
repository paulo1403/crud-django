function toggleTheme() {
  const htmlElement = document.documentElement;
  const currentTheme = htmlElement.getAttribute("data-bs-theme");
  const newTheme = currentTheme === "dark" ? "light" : "dark";

  htmlElement.setAttribute("data-bs-theme", newTheme);
  localStorage.setItem("theme", newTheme);

  // Update the theme icon
  const themeIcon = document.getElementById("theme-icon");
  if (newTheme === "dark") {
    themeIcon.classList.remove("bi-sun");
    themeIcon.classList.add("bi-moon");
  } else {
    themeIcon.classList.remove("bi-moon");
    themeIcon.classList.add("bi-sun");
  }
}

function loadTheme() {
  const savedTheme = localStorage.getItem("theme") || "light";
  const htmlElement = document.documentElement;

  htmlElement.setAttribute("data-bs-theme", savedTheme);

  // Set the correct icon on page load
  const themeIcon = document.getElementById("theme-icon");
  if (savedTheme === "dark") {
    themeIcon.classList.remove("bi-sun");
    themeIcon.classList.add("bi-moon");
  } else {
    themeIcon.classList.remove("bi-moon");
    themeIcon.classList.add("bi-sun");
  }
}

window.addEventListener("DOMContentLoaded", loadTheme);

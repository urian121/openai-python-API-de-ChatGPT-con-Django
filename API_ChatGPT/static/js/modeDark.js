const darkModeToggler = document.querySelector(".btn-toggle");
const body = document.body;

// Obtiene el estado del modo oscuro del almacenamiento local
let darkModeEnabled = localStorage.getItem("darkMode") === "true";
updateDarkMode();

// Agrega un event listener al botón de alternar modo oscuro
darkModeToggler.addEventListener("click", function () {
  darkModeEnabled = !darkModeEnabled;
  updateDarkMode();
});

function updateDarkMode() {
  // Toma en cuenta que aquí se maneja el cambio de clases en el elemento body
  if (darkModeEnabled) {
    body.classList.add("dark-mode");
  } else {
    body.classList.remove("dark-mode");
  }

  // Almacena el estado del modo oscuro en el almacenamiento local
  localStorage.setItem("darkMode", darkModeEnabled);
}

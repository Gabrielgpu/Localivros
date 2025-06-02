document.addEventListener("DOMContentLoaded", function () {
  const button = document.getElementById("dropdown-button");
  const menu = document.getElementById("dropdown-menu");
  const selected = document.getElementById("selected-unit");
  const stockInput = document.getElementById('stock-input');

  stockInput.value = selected.textContent

  button.addEventListener("click", (e) => {
    e.stopPropagation();
    menu.classList.toggle("hidden");
  });


  menu.querySelectorAll("a[data-value]").forEach(item => {
    item.addEventListener("click", function (e) {
      e.preventDefault();
      const value = this.getAttribute("data-value");
      selected.textContent = value;
      stockInput.value = value
      menu.classList.add("hidden");
    });
  });


  document.addEventListener("click", function (e) {
    if (!button.contains(e.target) && !menu.contains(e.target)) {
      menu.classList.add("hidden");
    }
  });
});
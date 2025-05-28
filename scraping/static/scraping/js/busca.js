document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form[role="search"]');
  const button = document.getElementById('search-button');
  const spinner = document.getElementById('loading-spinner');

  if (form && button && spinner) {
    form.addEventListener('submit', function () {
      button.disabled = true;
      button.innerText = 'Buscando...';
      spinner.style.display = 'block';
    });
  }
});
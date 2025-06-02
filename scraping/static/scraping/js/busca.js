document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form[role="search"]');
  const input = document.getElementById('id_isbn');
  const spinner = document.getElementById('loading-spinner');

  if (form && input && spinner) {
    form.addEventListener('submit', function (event) {
      input.classList.remove('opacity-0');
      input.classList.add('opacity-50');
      spinner.classList.remove('hidden');

    });
  }
});
document.addEventListener('DOMContentLoaded', function () {
  const dropdownItems = document.querySelectorAll('.dropdown-item');
  const selectedUnit = document.getElementById('selected-unit');
  const submitButton = document.getElementById('submit-button');
  const stockInput = document.getElementById('stock-input');


  dropdownItems.forEach(item => {
    item.addEventListener('click', function (event) {
      event.preventDefault();
      const value = this.getAttribute('data-value');
      selectedUnit.textContent = value + ' ' + (value === '1' ? 'Unidade' : 'Unidades');
      stockInput.value = value;
      submitButton.style.display = 'inline-block';
    });
  });
});

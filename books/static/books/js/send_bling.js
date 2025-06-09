document.addEventListener("DOMContentLoaded", function () {
  const blingInputSpinner = document.getElementById('loading-spinner');
  const blingForm = document.querySelector('form[role="send"]');
  const sendButton = document.getElementById('send-button')

  blingForm.addEventListener('submit', function(event) {
    sendButton.classList.add('hidden')
    blingInputSpinner.classList.remove('hidden')
  })

});
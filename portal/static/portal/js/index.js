function customUserIcon() {
    let modal = document.getElementById('customUserModal');
    modal.style.display = 'block';
    window.addEventListener('click', closeModalOutside);
}

function closeModalOutside(event) {
    let modal = document.getElementById('customUserModal');
    if (!event.target.closest('#customUserModal') && !event.target.closest('#customUserIcon')) {
      modal.style.display = 'none';
      window.removeEventListener('click', closeModalOutside);
    }
}
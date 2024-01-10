function callback_like(json) {
    let element = document.getElementById('like' + json.id);
    element.textContent = json.like;
}

function like(article_id) {
    fetch('/quiz/api/articles/' + article_id + '/like')
    .then(response => response.json())
    .then(callback_like)
}

function answer(article_id) {
    fetch('/quiz/api/articles/' + article_id + '/answer')
    .then()
}

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
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
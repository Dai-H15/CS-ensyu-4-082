function callback_like(json) {
    let element = document.getElementById('like' + json.id);
    element.textContent = json.like;
}

function like(article_id) {
    fetch('/quiz/api/articles/' + article_id + '/like')
    .then(response => response.json())
    .then(callback_like)
}

function callback_result(json) {
    let element = document.getElementById('result' + json.id);
    element.textContent = json.result;
}

function result(article_id) {
    fetch('/quiz/api/articles/' + article_id + '/result')
    .then(response => response.json())
    .then(callback_result)
}
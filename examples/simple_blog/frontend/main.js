const API_URL = "http://localhost:8000";

function registerUser() {
  const email = document.getElementById('email').value;
  const name = document.getElementById('name').value;
  fetch(`${API_URL}/users/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, name })
  })
    .then(res => res.json())
    .then(data => alert('User registered: ' + JSON.stringify(data)));
}

function createPost() {
  const title = document.getElementById('title').value;
  const content = document.getElementById('content').value;
  const author_id = parseInt(document.getElementById('author_id').value);
  fetch(`${API_URL}/posts/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, content, author_id })
  })
    .then(res => res.json())
    .then(data => alert('Post created: ' + JSON.stringify(data)));
}

function fetchPosts() {
  fetch(`${API_URL}/posts/`)
    .then(res => res.json())
    .then(posts => {
      const list = document.getElementById('posts-list');
      list.innerHTML = '';
      posts.forEach(post => {
        const li = document.createElement('li');
        li.textContent = `${post.title} by ${post.author_id}`;
        list.appendChild(li);
      });
    });
}

function exportGDPR() {
  const user_id = parseInt(document.getElementById('gdpr_user_id').value);
  fetch(`${API_URL}/gdpr/export?user_id=${user_id}`)
    .then(res => res.json())
    .then(data => {
      document.getElementById('gdpr-data').textContent = JSON.stringify(data, null, 2);
    });
}

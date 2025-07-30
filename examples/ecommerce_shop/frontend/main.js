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

function addProduct() {
  const name = document.getElementById('product_name').value;
  const description = document.getElementById('product_desc').value;
  const price = parseFloat(document.getElementById('product_price').value);
  fetch(`${API_URL}/products/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, description, price })
  })
    .then(res => res.json())
    .then(data => alert('Product added: ' + JSON.stringify(data)));
}

function placeOrder() {
  const user_id = parseInt(document.getElementById('order_user_id').value);
  const product_id = parseInt(document.getElementById('order_product_id').value);
  const quantity = parseInt(document.getElementById('order_quantity').value);
  fetch(`${API_URL}/orders/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ user_id, product_id, quantity })
  })
    .then(res => res.json())
    .then(data => alert('Order placed: ' + JSON.stringify(data)));
}

function fetchProducts() {
  fetch(`${API_URL}/products/`)
    .then(res => res.json())
    .then(products => {
      const list = document.getElementById('products-list');
      list.innerHTML = '';
      products.forEach(product => {
        const li = document.createElement('li');
        li.textContent = `${product.name} - $${product.price}`;
        list.appendChild(li);
      });
    });
}

function fetchOrders() {
  fetch(`${API_URL}/orders/`)
    .then(res => res.json())
    .then(orders => {
      const list = document.getElementById('orders-list');
      list.innerHTML = '';
      orders.forEach(order => {
        const li = document.createElement('li');
        li.textContent = `Order #${order.id} by User ${order.user_id} for Product ${order.product_id} x${order.quantity}`;
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

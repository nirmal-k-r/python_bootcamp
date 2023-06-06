function addToCart(productName, price) {
    const cart = document.getElementById("cart");
    const cartItem = document.createElement("li");
    cartItem.classList.add("cart-item");
    cartItem.textContent = productName + " - $" + price;
    cart.appendChild(cartItem);
  }
  
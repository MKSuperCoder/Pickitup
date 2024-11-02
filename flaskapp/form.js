document.getElementById('foodForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const foodItem = document.getElementById('foodItem').value;
    const quantity = document.getElementById('quantity').value;
    const pickupTime = document.getElementById('pickupTime').value;

    const foodList = document.getElementById('foodList');
    const foodDiv = document.createElement('div');
    foodDiv.textContent = `${foodItem} - Quantity: ${quantity} - Pickup: ${pickupTime}`; // Use backticks for template literals
    foodList.appendChild(foodDiv);

    // Clear the form
    this.reset();
});

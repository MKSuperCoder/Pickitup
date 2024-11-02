document.getElementById('foodForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const foodItem = document.getElementById('foodItem').value.trim();
    const quantity = document.getElementById('quantity').value;
    const pickupTime = document.getElementById('pickupTime').value.trim();
    const feedback = document.getElementById('formFeedback');

    // Validate the inputs
    if (!foodItem || !quantity || !pickupTime || isNaN(quantity) || quantity <= 0) {
        feedback.textContent = "Please fill in all fields correctly.";
        feedback.style.color = "red";
        feedback.style.display = "block";
        return;
    }

    // Prepare the data to be sent to the server
    const data = {
        foodItem: foodItem,
        quantity: quantity,
        pickupTime: pickupTime
    };

    // Make a POST request to the server
    fetch('http://localhost:5000/api/food', { // Ensure the URL matches your server's endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Assuming the server returns a success message
        feedback.textContent = "Food posted successfully!";
        feedback.style.color = "green";
        feedback.style.display = "block";

        // Update the food list display
        const foodList = document.getElementById('foodList');
        const foodDiv = document.createElement('div');
        foodDiv.textContent = `${foodItem} - Quantity: ${quantity} - Pickup: ${pickupTime}`;
        foodList.appendChild(foodDiv);

        // Clear the form
        this.reset();
    })
    .catch(error => {
        feedback.textContent = "Failed to post food. Please try again.";
        feedback.style.color = "red";
        feedback.style.display = "block";
        console.error('Error:', error);
    });
});

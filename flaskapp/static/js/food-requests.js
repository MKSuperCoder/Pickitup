function handleRequest(action) {
    // Get the values from the input fields
    const foodItem = document.getElementById('foodItem').value.trim();
    const quantity = document.getElementById('quantity').value;
    const pickupTime = document.getElementById('pickupTime').value.trim();
    const feedback = document.getElementById('formFeedback');

    // Input validation
    if (!foodItem || !quantity || !pickupTime || isNaN(quantity) || quantity <= 0) {
        feedback.innerText = "Please fill in all fields correctly.";
        feedback.style.color = "red";
        feedback.style.display = 'block';
        return; // Stop further execution if validation fails
    }

    if (action === 'post') {
        // Make the POST request to the server
        fetch('http://localhost:5000/api/food', { // Ensure the URL matches your server's endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ foodItem, quantity, pickupTime })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Parse the JSON response
        })
        .then(data => {
            // Handle success: update feedback and the food list
            feedback.innerText = "Food posted successfully!";
            feedback.style.color = "green";
            feedback.style.display = 'block';

            // Optionally, update the food list display
            const foodList = document.getElementById('foodList');
            const foodDiv = document.createElement('div');
            foodDiv.textContent = `${foodItem} - Quantity: ${quantity} - Pickup: ${pickupTime}`;
            foodList.appendChild(foodDiv);

            // Clear the form fields after successful submission
            document.getElementById('foodForm').reset();
        })
        .catch((error) => {
            console.error('Error:', error);
            feedback.innerText = "Failed to post food.";
            feedback.style.color = "red";
            feedback.style.display = 'block';
        });
    }
}

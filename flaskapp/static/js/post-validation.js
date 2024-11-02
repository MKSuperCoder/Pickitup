document.getElementById('foodForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const foodItem = document.getElementById('foodItem').value.trim();
    const quantity = document.getElementById('quantity').value;
    const pickupTime = document.getElementById('pickupTime').value.trim();
    const feedback = document.getElementById('formFeedback');

    const validFoodItems = ['Chips', 'Water', 'Soda', 'Sandwich', 'Pizza', 'Granola Bar'];

    // Validate the form data
    if (validFoodItems.includes(foodItem) && quantity > 0 && pickupTime) {
        // Prepare data to send to the server
        const data = {
            foodItem: foodItem,
            quantity: quantity,
            pickupTime: pickupTime
        };

        // Send the data to your server endpoint
        fetch('http://localhost:5000/api/food', {  // Adjust the URL to your server's endpoint
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
            return response.json(); // Assuming your server returns JSON
        })
        .then(data => {
            feedback.textContent = "Food posted successfully!";
            feedback.style.color = "green";
            feedback.style.display = "block";
            // Optionally update the food list here
            addFoodToList(foodItem, quantity, pickupTime);
        })
        .catch((error) => {
            feedback.textContent = "Failed to post food. Please try again.";
            feedback.style.color = "red";
            feedback.style.display = "block";
            console.error('Error:', error);
        });
    } else {
        feedback.textContent = "Please fill in all fields correctly.";
        feedback.style.color = "red";
        feedback.style.display = "block";
    }
});

// Function to add food entry to the list on the frontend
function addFoodToList(item, qty, time) {
    const foodList = document.getElementById('foodList');
    const foodEntry = document.createElement('div');
    foodEntry.textContent = `${item} - ${qty} available for pickup at ${time}`;
    foodList.appendChild(foodEntry);
}

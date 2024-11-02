function handleRequest(action) {
    // Get the values from the input fields
    const foodItem = document.getElementById('foodItem').value.trim();
    const quantity = document.getElementById('quantity').value;
    const cunyId = document.getElementById('cunyId').value.trim();
    const date = document.getElementById('date').value;
    const clubName = document.getElementById('clubName').value.trim();
    const location = document.getElementById('location').value.trim();
    const startTime = document.getElementById('startTime').value;
    const pickupTime = document.getElementById('pickupTime').value.trim();
    const feedback = document.getElementById('formFeedback');

    // Input validation
    if (!foodItem || !quantity || !cunyId || !date || !clubName || !location || !startTime || !pickupTime || isNaN(quantity) || quantity <= 0) {
        feedback.innerText = "Please fill in all fields correctly.";
        feedback.style.color = "red";
        feedback.style.display = 'block';
        return; // Stop further execution if validation fails
    }

    if (action === 'post') {
        // Create the data object for the POST request
        const postData = {
            foodItem,
            quantity,
            cunyId,
            date,
            clubName,
            location,
            startTime,
            pickupTime
        };

        // Make the POST request to the server
        fetch('http://localhost:5000/event', { // Ensure the URL matches your server's endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(postData)
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
            foodDiv.textContent = `${foodItem} - Quantity: ${quantity} - Pickup: ${pickupTime} - Club: ${clubName}`;
            foodList.appendChild(foodDiv);

            // Clear the form fields after successful submission
            document.getElementById('foodForm').reset();

            // Optionally display server response in a modal
            document.getElementById('modal-heading').innerText = 'Server Response';
            document.getElementById('res-code').innerText = JSON.stringify(data, null, 2);
            document.getElementById('responseModal').style.display = 'block';
        })
        .catch((error) => {
            console.error('Error:', error);
            feedback.innerText = "Failed to post food.";
            feedback.style.color = "red";
            feedback.style.display = 'block';
        });
    }
}

function closeModal() {
    document.getElementById('responseModal').style.display = 'none';
}

document.getElementById('foodForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    const foodItem = document.getElementById('foodItem').value.trim();
    const quantity = document.getElementById('quantity').value;
    const pickupTime = document.getElementById('pickupTime').value.trim();
    const feedback = document.getElementById('formFeedback');

    // Define valid food items
    const validFoodItems = ['Chips', 'Water', 'Soda', 'Sandwich', 'Pizza', 'Granola Bar'];

    // Check if the food item is valid and if quantity is a positive number
    if (validFoodItems.includes(foodItem) && quantity > 0 && pickupTime) {
        feedback.textContent = "Food posted successfully!";
        feedback.style.color = "green";
        feedback.style.display = "block";
        
        // Call the function to add food to the list
        addFoodToList(foodItem, quantity, pickupTime);

        // Clear the form fields after successful submission
        document.getElementById('foodForm').reset(); 
    } else {
        feedback.textContent = "Please fill in all fields correctly.";
        feedback.style.color = "red";
        feedback.style.display = "block";
    }
});

// Function to add food item to the display list
function addFoodToList(item, qty, time) {
    const foodList = document.getElementById('foodList');
    const foodEntry = document.createElement('div');
    foodEntry.textContent = `${item} - ${qty} available for pickup at ${time}`;
    foodList.appendChild(foodEntry);
}

document.getElementById('foodForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const foodItem = document.getElementById('foodItem').value.trim();
    const quantity = document.getElementById('quantity').value;
    const pickupTime = document.getElementById('pickupTime').value.trim();
    const feedback = document.getElementById('formFeedback');

    const validFoodItems = ['Chips', 'Water', 'Soda', 'Sandwich', 'Pizza', 'Granola Bar'];

    if (validFoodItems.include(foodItem) && quantity > 0 && pickupTime) {
        feedback.textContent = "Food posted successfully!";
        feedback.style.color = "green";
        feedback.style.display = "block";
        addFoodToList(foodItem, quantity, pickupTime);
    } else {
        feedback.textContent = "Please fill in all fields correctly.";
        feedback.style.color = "red";
        feedback.style.display = "block";
    }
});


//Change to Add to Database
function addFoodToList(item, qty, time) {
    const foodList = document.getElementById('foodList');
    const foodEntry = document.createElement('div');
    foodEntry.textContent = `${item} - ${qty} available for pickup at ${time}`;
    foodList.appendChild(foodEntry);
}

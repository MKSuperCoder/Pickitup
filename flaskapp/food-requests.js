
const categorySelect = document.getElementById('category');
const foodSelect = document.getElementById('foods');
const postFoodButton = document.getElementById('postFoodButton');

// Filter food options based on selected category
categorySelect.addEventListener('change', function() {
const selectedCategory = this.value;
        
Array.from(foodSelect.options).forEach(option => {
    option.style.display = (selectedCategory === 'all' || option.getAttribute('data-category') === selectedCategory) 
           ? 'block' 
           : 'none';
    });
        
        // Reset the food dropdown to the default option after filtering
    foodSelect.value = "";
     checkFoodSelection(); // Check if a valid selection is made
    });

    // Enable the Post Food button only if a valid food is selected
    foodSelect.addEventListener('change', checkFoodSelection);

    function checkFoodSelection() {
        postFoodButton.disabled = (foodSelect.value === "");
    }
//Category Dropdown
document.getElementById("category").addEventListener("change", function() {
    const selectedCategory = this.value;
    const foodOptions = document.getElementById("foods").options;
  
    // Loop through the food options and show/hide based on category
    for (let i = 0; i < foodOptions.length; i++) {
      const option = foodOptions[i];
      const optionCategory = option.getAttribute("data-category");
  
      // Display options if they match the selected category or if "All" is selected
      if (selectedCategory === "all" || optionCategory === selectedCategory) {
        option.style.display = "block";
      } else {
        option.style.display = "none";
      }
    }
  
    // Reset the selection to the first visible option
    document.getElementById("foods").selectedIndex = 0;
  });
  




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
  




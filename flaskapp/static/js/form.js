function postFood() {
    // Collect form data and send it to the server
    const foodData = {
        item: document.getElementById('foodItem').value,  // Get food item name
        quantity: document.getElementById('quantity').value,  // Get food item quantity
        pickup_time: document.getElementById('pickupTime').value,  // Get pickup time
        event_id: document.getElementById('eventId').value,  // Get event ID
        cuny_id: document.getElementById('cunyId').value,  // Get CUNY ID
        date: document.getElementById('date').value,  // Get date
        club_name: document.getElementById('clubName').value,  // Get club name
        status: document.getElementById('status').value,  // Get food item status
        location: document.getElementById('location').value,  // Get pickup location
        start_time: document.getElementById('startTime').value,  // Get event start time
        end
    }};
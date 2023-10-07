//// JavaScript for opening and populating the edit modal
//  $(document).ready(function () {
//    $('.edit').on('click', function () {
//      var customerId = $(this).data('customer-id');
//
//      // Send an AJAX request to your Django view
//      $.ajax({
//        url: `edit_customer/${customerId}/`,  // Construct the URL dynamically
//        method: 'POST',
//        success: function (data) {
//          $('#edit-accountID').val(data.accountID);
//          $('#edit-firstname').val(data.firstname);
//          $('#edit-lastname').val(data.lastname);
//          $('#edit-email').val(data.email);
//          $('#edit-phone_number').val(data.phone_number);
//          $('#edit-address').val(data.address);
//          $('#edit-state').val(data.state);
//          $('#edit-city').val(data.city);
//          $('#edit-zipcode').val(data.zipcode);
//          $('#edit-birthdate').val(data.birthdate);
//
//      // Show the modal
//      $('#editModal').modal('show');
//        },
//        error: function (error) {
//          // Handle errors if any
//        }
//      });
//    });
//  });
//
//
//$(document).ready(function () {
//  // Handle click event on the "Edit" button
//  $('.edit').click(function () {
////    var userIdentifier = '{{ user_identifier }}';
//    var accountID = $(this).data('id');
//    console.log('Clicked Edit for accountID:', accountID); // Debug
//    console.log('Clicked Edit for user:', userIdentifier ); // Debug
//    var firstname = $(this).closest('td').find('[data-field="firstname"]').text();
//    var lastname = $(this).closest('td').find('[data-field="lastname"]').text();
//    var email = $(this).closest('td').find('[data-field="email"]').text();
//    var phoneNumber = $(this).closest('td').find('[data-field="phone_number"]').text();
//    var address = $(this).closest('td').find('[data-field="address"]').text();
//    var state = $(this).closest('td').find('[data-field="state"]').text();
//    var city = $(this).closest('td').find('[data-field="city"]').text();
//    var zipcode = $(this).closest('td').find('[data-field="zipcode"]').text();
//    var birthdate = $(this).closest('td').find('[data-field="birthdate"]').text();
//    // ... (Your existing code to populate the modal fields)
//  });
//
//  // Handle save changes button click event
//  $('#saveChanges').click(function () {
////    $('#edit-accountID').val(accountID);
//    $('#edit-firstname').val(firstname);
//    $('#edit-lastname').val(lastname);
//    $('#edit-email').val(email);
//    $('#edit-phone_number').val(phoneNumber); // Populate phone number field
//    $('#edit-address').val(address); // Populate address field
//    $('#edit-state').val(state); // Populate state field
//    $('#edit-city').val(city); // Populate city field
//    $('#edit-zipcode').val(zipcode); // Populate zipcode field
//    $('#edit-birthdate').val(birthdate); // Populate birthdate field
//    // Get values of other fields as needed
//
//    // Create a data object to send in the AJAX request
//    var data = {
//      accountID: accountID,
//      firstname: firstname,
//      lastname: lastname,
//      email: email,
//      phone_number: phoneNumber, // Include phone number
//      address: address, // Include address
//      state: state, // Include state
//      city: city, // Include city
//      zipcode: zipcode, // Include zipcode
//      birthdate: birthdate // Include birthdate
//      // Include other fields here
//    };
//
//    // Send an AJAX POST request to update the customer data
//    $.ajax({
//      type: 'POST',
//      url: '/welcome/' + user_identifier + '/customers' + accountID + '/',
//      data: data,
//      success: function(response) {
//        // Handle the success response (e.g., show a success message)
//        console.log('Data updated successfully:', response.message);
//        // Close the modal after saving
//        $('#editModal').modal('hide');
//      },
//      error: function(error) {
//        // Handle any errors that occur during the AJAX request
//        console.error('Error updating data:', error.responseJSON.error);
//      }
//    });
//  });
//});
//
//





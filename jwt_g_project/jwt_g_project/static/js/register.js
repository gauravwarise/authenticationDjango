function performAction() {
    const action = $('#action').val();
    const username = $('#username').val();
    const password = $('#password').val();

    console.log(action, username, password);

    let data = {
        action: action,
        username: username,
        password: password
    };
    console.log(data);

    // Include email for registration
    if (action === 'register') {
        const email = $('#email').val();
        data['email'] = email;
        const first_name = $('#first_name').val();
        data['first_name'] = first_name;
        const last_name = $('#last_name').val();
        data['last_name'] = last_name;

    }

    // AJAX request to your API endpoint
    $.ajax({
        type: 'POST',
        url: '/api/auth/',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function(response) {
            $('#result').text(JSON.stringify(response));
        },
        error: function(error) {
            $('#result').text(JSON.stringify(error.responseJSON));
        }
    });
}

// Show additional fields for registration
// $('#action').change(function() {
//     if ($(this).val() === 'register') {
//         $('#additionalFields').show();
//     } else {
//         $('#additionalFields').hide();
//     }
// });

$(document).ready(function() {
    // Your other code here
});
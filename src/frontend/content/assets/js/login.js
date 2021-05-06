﻿// initialize validation messages variable
$.validation = {
    messages: {}
};

// add validation templates to show fancy icons with message text
$.extend($.validation.messages, {
    required: '<i class="fa fa-exclamation-circle"></i> required.',
    username: '<i class="fa fa-exclamation-circle"></i> Please enter a valid username.',
});

// call our 'validateLoginForm' function when page is ready
$(document).ready(function () {
    validateLoginForm();
});

// bind jQuery validation event and form 'submit' event
var validateLoginForm = function () {
    var form_login = $('#form_login');
    var login_result = $('#login_result');

    // bind jQuery validation event
    form_login.validate({
        rules: {
            login_username: {
                required: true     // username field is required
                //username: true      // validate username
            },
            login_password: {
                required: true      // password field is required
            }
        },
        messages: {
            login_username: {
                required: $.validation.messages.required,
                username: $.validation.messages.username
            },
            login_password: {
                required: $.validation.messages.required
            }
        },
        errorPlacement: function (error, element) {
            // insert error message after invalid element
            error.insertAfter(element);

            // hide error message on window resize event
            $(window).resize(function () {
                error.remove();
            });
        },
        invalidHandler: function (event, validator) {
            var errors = validator.numberOfInvalids();
            if (errors) {
            } else {
            }
        }
    });

    var login_username = $('#login_username');
    var login_password = $('#login_password');
    var login_remember = $('#login_remember');

    // bind form submit event
    form_login.on('submit', function (e) {
        var remember = login_remember.is(':checked') ? 1 : 0;

        // if form is valid then call AJAX script
        if (form_login.valid()) {
            var ajaxRequest = $.ajax({
                //url: 'ajax/login.php',
                url: 'http://localhost:8000/api/v1/auth/login/',
                type: "POST",
                dataType: "application/json",
                data: {
                    username: login_username.val(),
                    password: login_password.val()
                },
                beforeSend: function () {
                }
            });

            ajaxRequest.fail(function (data, status, errorThrown) {
                // error
                var $message = data.responseText;
                login_result.html('<div class="alert alert-danger">' + $message + '</div>');
            });

            ajaxRequest.done(function (response) {
                console.log(JSON.stringify(response));

                // done
                var $response = $.parseJSON(response);
                login_result.html('<div class="alert alert-success">' + $response.key + '</div>');

                // save token session value
                var $session_key = $response.key;
                console.log($session_key);
            });
        }

        // stop default submit event of form
        e.preventDefault();
        e.stopPropagation();
    });
}
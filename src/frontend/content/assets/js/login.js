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

        if (form_login.valid()){
            var ajaxRequest = $.ajax({
                url: env.BACKEND_ENDPOINT + '/api/v1/auth/login/',
                type: "POST",
                //contentType: "application/json",
                dataType: "json",
                data: {
                    username: login_username.val(),
                    password: login_password.val()
                },
                beforeSend: function(){
                    //xhr.setRequestHeader("Authorization", "Token " + window.sessionStorage.getItem("Token"));
                }
            })
            .fail(function (data, status, errorThrown) {
                //var $message = data.responseText;
                var $message = 'Authentication failed. Please check your username and password.'
                login_result.html('<div class="alert alert-danger">' + $message + '</div>');
            })
            .done(function (data, textStatus, xhr) {
                //var $result = $.parseJSON(data);
                var $session_key = data.key;
                console.log("session_key: " + $session_key);

                if  ($session_key){
                    // save authentication token to session
                    window.sessionStorage.setItem("Token", $session_key);

                    // get user info
                    $.ajax({
                        url: env.BACKEND_ENDPOINT + '/api/v1/auth/user/',
                        type: "GET",
                        //contentType: "application/json",
                        dataType: "json",
                        data: {
                        },
                        beforeSend: function(xhr){
                            xhr.setRequestHeader("Authorization", "Token " + window.sessionStorage.getItem("Token"));
                        }
                    })
                    .fail(function (data, status, errorThrown) {
                        var $message = data.responseText;
                        login_result.html('<div class="alert alert-danger">' + $message + '</div>');
                    })
                    .done(function (data, textStatus, xhr) {
                        var $user_id = data.pk;
                        console.log("user_id: " + $user_id);
                        window.sessionStorage.setItem("user_id", $user_id);

                        //login_result.html('<div class="alert alert-success">' + data.key + '</div>');
                        window.location.href = "./main.html";
                    });
                } else  {
                    login_result.html('<div class="alert alert-danger">System error occured. Please try again.</div>');
                }
            });
        }

        // stop default submit event of form
        e.preventDefault();
        e.stopPropagation();
    });
}
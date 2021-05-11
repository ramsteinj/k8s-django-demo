// get user_id
var $user_id = window.sessionStorage.getItem("user_id");
var $forum_id = "1"; // hard-code for now
console.log("user_id: " + $user_id);
console.log("forum_id: " + $forum_id);

// form info
var $topic = "";

// initialize validation messages variable
$.validation = {
    messages: {}
};

// add validation templates to show fancy icons with message text
$.extend($.validation.messages, {
    required: '<i class="fa fa-exclamation-circle"></i> required.',
    username: '<i class="fa fa-exclamation-circle"></i> Please enter a valid username.',
});

// retrieve datas
$(document).ready(function () {
    retrieveForum();
    retrieveDiscussions();
    postDiscussForm();
});

// retrieve forum info
var retrieveForum = function () {
    console.log("retrieveForum() invoked...");
    var forum_topic = $('#forum_topic');

    $.ajax({
        url: env.BACKEND_ENDPOINT + '/api/v1/forum/list/',
        type: "GET",
        dataType: "json",
        data: {
        },
        beforeSend: function(xhr){
            xhr.setRequestHeader("Authorization", "Token " + window.sessionStorage.getItem("Token"));
        }
    })
    .fail(function (data, status, errorThrown) {
        var $message = data.responseText;
        console.log($message);
    })
    .done(function (data, textStatus, xhr) {
        /*
        $.each(data, function() {
            $.each(this, function(key, value) {
                console.log("key: " + key);
                console.log("value: " + value);

                if  (key == "forum_id"){
                    if  (value == "1"){
                        console.log("found forum_id=1...");
                        if  (key == "topic"){
                            $topic = value;
                        }
                        if  (key == "description"){
                            $description = value;
                        }

                        return false;   // break the loop
                    }
                }
            });
          });
          */

          $topic = data[0].topic;
          console.log("topic: " + $topic);
          forum_topic.html('<div id="forum_topic" class="page-header"><h2>' + $topic + '</h2><br></div>');
        });
}


// retrieve discussions in a forum
var retrieveDiscussions = function () {
    console.log("retrieveDiscussions() invoked...");
    var $discussions = "";
    var discussion_list = $('#discussion_list');

    $.ajax({
        url: env.BACKEND_ENDPOINT + '/api/v1/forum/' + $forum_id + '/',
        type: "GET",
        dataType: "json",
        data: {
        },
        beforeSend: function(xhr){
            xhr.setRequestHeader("Authorization", "Token " + window.sessionStorage.getItem("Token"));
        }
    })
    .fail(function (data, status, errorThrown) {
        var $message = data.responseText;
        console.log(message);
    })
    .done(function (data, textStatus, xhr) {
        console.log("data.length: " + data.length);

        for (var i=0; i<data.length; i++){
            $discussions += '<tr>';
            $discussions += ' <td>' + Number(i+1) + '</td>';
            $discussions += ' <td>' + data[i].username + '</td>';
            $discussions += ' <td>' + data[i].discuss + '</td>';
            $discussions += ' <td>' + data[i].created + '</td>';
            $discussions += '</tr>';
        }

        var table_header = '<table id="discussion_list" class="table table-hover"><thead><tr><th>#</th><th>User</th><th>Discussion</th><th>Date</th></tr></thead><tbody>';
        var table_footer = '</tbody></table>';
        discussion_list.html(table_header + $discussions + table_footer);
    });
}

// bind jQuery validation event and form 'submit' event
var postDiscussForm = function () {
    console.log("postDiscussForm() invoked...");
    var form_discuss = $('#form_discuss');
    var input_discussion = $('#input_discussion');

    // bind form submit event
    form_discuss.on('submit', function (e) {
        if (form_discuss.valid()){
            var ajaxRequest = $.ajax({
                url: env.BACKEND_ENDPOINT + '/api/v1/forum/discussion/',
                type: "POST",
                dataType: "json",
                data: {
                    user_id: $user_id,
                    forum_id: $forum_id,
                    discuss: input_discussion.val()
                },
                beforeSend: function(xhr){
                    xhr.setRequestHeader("Authorization", "Token " + window.sessionStorage.getItem("Token"));
                }
            })
            .fail(function (data, status, errorThrown) {
                var $message = data.responseText;
                console.log($message);
            })
            .done(function (data, textStatus, xhr) {
                console.log("successfully posted a discussion...");

                // refresh window
                location.reload();
            });
        }

        // stop default submit event of form
        e.preventDefault();
        e.stopPropagation();
    });
}
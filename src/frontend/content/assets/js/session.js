$(document).ready(function(){
    validateSession();
});

var validateSession = function(){
    var $session_token;

    try {
        //$session_token = $.session.get($SESSION_KEY_NAME);
        $session_token = window.sessionStorage.getItem("Token")
        console.log("session_token: " + $session_token);

        if  (!$session_token){
            window.location.href = "./index.html";
        }
    }
    catch (error){
        // redirect to login page
        window.location.href = "./index.html";
    }
}
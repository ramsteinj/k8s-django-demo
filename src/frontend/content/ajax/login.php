<?php
$email = $_POST['email'];
$password = $_POST['password'];
$remember = $_POST['remember'];

echo json_encode( array(
                            'status' => 'success',
                            'message' => sprintf( 'login successful. You entered<br />Email: %1$s<br />Password: %2$s<br />Remember: %3$s', 
                                                   $email, 
                                                   $password, 
                                                   $remember == 0 ? 'NO' : 'YES'
                                                ),
                       )
                );
?>
<?php

$db = mysqli_connect('localhost', 'root', '1234', 'web_libros') or die('Error de conexión a la base de datos');

//Obtener los datos de formulario: 
$email_posted = $_POST['email'];
$password1 = $_POST['password1'];
$password2 = $_POST['password2'];
$nombre = $_POST['nombre'];
$apellidos = $_POST['apellidos'];

echo $email_posted; exit;
//Comprobar campo vacio y contraseñas
if(empty ($email_posted) || empty($password1) || empty($password2) || empty($nombre) || empty($apellidos)) {
    echo '<p>Todos los campos son obligatorios</p>';
}else if ($password1 !== $password2) {
        echo '<p>Las contraseñas no coinciden</p>';
}else{
        //Comprobar si el email ya está registrado
        $query ="SELECT id from tUsuarios where email = '$email_posted'";
        $result = mysqli_query($db, $query) or die ('ERROR');
        echo var_dump($result);
    }
    

?>


<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<body>
<h1>Conexión establecida</h1>
<?php
// Lanzar una query
$query = 'SELECT * FROM tLibros';
$result = mysqli_query($db, $query) or die('Query error');

// Recorrer el resultado
while ($row = mysqli_fetch_array($result)) {
    echo $row['nombre'] . '<br>';
    echo $row['fecha_publicacion'] . '<br>';
    echo $row['autor'] . '<br>';
    echo '<img src="' . $row['url_imagen'] . '" style="width:100px; height:100px;"><br>';
    echo '<a href="http://localhost:8083/detail.php?id=' . $row['id'] . '">Ver más.</a><br><br>';
}
mysqli_close($db);
?>
</body>
</html>


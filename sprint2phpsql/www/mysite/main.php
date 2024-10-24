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
echo $row['nombre'];
echo '<br>';
echo $row['fecha_publicacion'];
echo '<br>';
echo $row['autor'];
echo '<br>';
echo '<img src="'.$row[2].'"style="width:100px; height:100px;">';
echo '<br>';
echo '<a href="detail.php">Ver más.</a>';
echo '<br>';
}
?>
</body>
</html>

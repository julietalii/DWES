<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<body>
<?php
if (!isset($_GET['id'])) {
    die('No se ha especificado un libro');
}
$id = $_GET['id'];
$query = 'SELECT * FROM tLibros WHERE id='.$id;
$result = mysqli_query($db, $query) or die('Query error');
$only_row = mysqli_fetch_array($result);

if (!$only_row) {
    die('No se encontró el libro con el ID especificado.');
}

$libro_id = $id;

// Mostrar detalles del libro
echo '<h1>' . $only_row['nombre'] . '</h1>';
echo '<img src="' . $only_row['url_imagen'] . '" alt="' . $only_row['nombre'] . '" style="width:200px;height:auto;">';
echo '<h2>Autor: ' . $only_row['autor'] . '</h2>';
echo '<h3>Fecha de Publicación: ' . $only_row['fecha_publicacion'] . '</h3>';
?>
<h3>Comentarios:</h3>
<ul>
<?php
// Consultar los comentarios asociados al libro
$query2 = 'SELECT comentario, fecha FROM tComentarios WHERE libro_id='.$id;
$result2 = mysqli_query($db, $query2) or die('Query error');
while ($row = mysqli_fetch_array($result2)) {
    echo '<li>' . $row['comentario'] . ' <em>(' . $row['fecha'] . ')</em></li>';
}
mysqli_close($db);
?>
</ul>
<!--Comentarios -->
<p>Deja un nuevo comentario:</p>
<form action="/comment.php" method="post">
<textarea rows="4" cols="50" name="new_comment"></textarea><br>
<input type="hidden" name="libro_id" value="<?php echo $libro_id; ?>">
<input type="submit" value="Comentar">
</form>

</body>
</html>

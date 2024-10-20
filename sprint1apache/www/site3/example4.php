<html>
<body>
<h1>Jubilación</h1>
<?php

function edad_en_7_años($age) {
return $age + 7;
}
function mensaje($edad) {
if (edad_en_7_años($edad) > 65) {
return "En 7  años tendrás edad de jubilación";
} else {
return "¡Disfruta de tu tiempo!";
}
}
?>
<table>
<tr>
<th>Edad</th>
<th>Info</th>
</tr>
<?php
$lista = array(50,55,60,61,62);
foreach ($lista as $valor) {
echo "<tr>";
echo "<td>".$valor."</td>";
echo "<td>".mensaje($valor)."</td>";
echo "</tr>";
}
?>
</table>
</body>
</html>

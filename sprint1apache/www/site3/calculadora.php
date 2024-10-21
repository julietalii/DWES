<html>
<body>
<h1>Calculadora</h1>
<p>Operaciones disponibles: suma, resta, multiplicacion, division</p>
<p>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $v_1 = $_POST["fnum1"];
    $v_2 = $_POST["fnum2"];
    $operacion = $_POST["f2"];

    if (is_numeric($v_1) && is_numeric($v_2)) {
        switch ($operacion) {
            case "suma":
                $resultado = $v_1 + $v_2;
                break;
            case "resta":
                $resultado = $v_1 - $v_2;
                break;
            case "multiplicacion":
                $resultado = $v_1 * $v_2;
                break;
            case "division":
                if ($v_2 != 0) {
                    $resultado = $v_1 / $v_2;
                } else {
                    $resultado = "Error: No se puede dividir entre cero.";
                }
                break;
            default:
                $resultado = "Operación no válida.";
                break;
        }
        echo "<p>Resultado: $resultado</p>";
    } else {
        echo "<p>Números no válidos.</p>";
    }
}
?>
<form action="/calculadora.php" method ="post">
	<label for="numero1_input">Numero 1:</label><br>
	<input type="text" id="numero1_input" name="fnum1"><br>
	<label for="numero2_input">Numero 2:</label><br>
        <input type="text" id="numero2_input" name="fnum2"><br>

<label for="cantidad_input">Menú:</label><br>
<input type="radio" id="suma_input" name="f2" value="suma">
<label for="pulgada_input">SUMA</label><br>
<input type="radio" id="resta_input" name="f2" value="resta">
<label for="resta_input">RESTA</label><br>
<input type="radio" id="multiplicacion_input" name="f2" value="multiplicacion">
<label for="resta_input">MULTIPLICACION</label><br>
<input type="radio" id="division_input" name="f2" value="division">
<label for="division_input">DIVISION</label><br>
	<input type="submit" value="OK">
</form>


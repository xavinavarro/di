<html>
	<head meta charset=utf-8 />
	<body>
		<table border=1 >
			<?php
				define ("TAM", 4);  
				function potencia ($variable1, $variable2){  
					$resultado = pow($variable1, $variable2);
					return $resultado;
				}
				$fila = 1; 
				$numero = 1; 
				while ($fila <= TAM){
					print "<tr>";
					for ($j = 1; $j <= TAM; $j++){ 
						print "<td>" . potencia($numero, $j) . "</td>";
					}
					$numero++;
					print "</tr>";
					$fila++;
				}
			?>
		</table>
	</body>
</html>

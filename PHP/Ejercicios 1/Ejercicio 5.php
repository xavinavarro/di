<html>
	<head meta charset=utf-8 />
	<body>
		<table border=1 >
			<?php
				define ("TAM", 10);
				$fila = 1; 
				$numero = 1;
				while ($fila <= TAM){  
					print "<tr>";
					for ($j = 1; $j <= TAM; $j++){ 
						if ($j % 2 != 0)
							print "<td style = background-color:lightgrey;>" . $numero . "</td>";
						else
							print "<td>" . $numero . "</td>";
						$numero++;
					}
					print "</tr>";
					$fila++;
				}
			?>
		</table>
	</body>
</html>

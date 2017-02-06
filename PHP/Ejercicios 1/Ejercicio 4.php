<html>
	<head meta charset=utf-8 />
	<body>
		<table border=1 >
			<?php
				$fila = 1; 
				$numero = 1;
				while ($fila <= 10){ 
					print "<tr>";
					for ($j = 1; $j <= 10; $j++){
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

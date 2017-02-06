<html>
	<head meta charset=utf-8 />
	<body>
		<table border=1 >
			<?php
				chdir('fotos'); 
				define ("TAM", 4);  
				$fila = 1; 
				$numero = 1; 
				while ($fila <= TAM){  
					print "<tr>";
					for ($j = 1; $j <= TAM; $j++){ 
						print "<td>" . '<img src="/PHP/fotos/'.$numero.'.jpg"/>' . "</td>";
						$numero++;
					}
					print "</tr>";
					$fila++;
				}
			?>
		</table>
	</body>
</html>

<?php
	define ("TAM", 4);  
	function extension(){
		chdir('fotos'); 
		$directorio = getcwd();
		$gestor_dir = opendir($directorio);
		while (false !== ($nombre_fichero = readdir($gestor_dir))) { 
		    $ficheros[] = $nombre_fichero; 
		}
		$bucle = count($ficheros); 
		$i = 0;
		while ($i < $bucle){  
			$comprobar = $ficheros[$i];
			$trozo = explode (".", $comprobar);
			$extensio = end($trozo);
			if ($extensio == "jpg"){
				$validas[] = $ficheros[$i];
			}else if ($extensio == "gif"){
				$validas[] = $ficheros[$i];
			}else if ($extensio == "bmp"){
				$validas[] = $ficheros[$i];
			}else if ($extensio == "png"){
				$validas[] = $ficheros[$i];
			}
			$i++;
			$comprobar = ""; 
		}
		return $validas;
	}
	$valida = extension(); 
	$numero = 0;
	$bucle2 = count($valida);  
	$fila = 1;
	echo "<table border=1>"; 
	while ($fila <= TAM){ 
		print "<tr>";
		for ($j = 1; $j <= TAM; $j++){  
			print "<td>" . '<a href=fotos/'.$valida[$numero].'><img src="fotos/minifotos/MINI-'.$valida[$numero].'"/></a>' . "</td>";
			$numero++;
		}
		print "</tr>";
		$fila++;
	}
	echo "</table>";
?>

<?php
	$numero = 1;
	$cont = 0;
	while ($cont < 10){
		if ($numero % 2 == 0){
			$array[$cont] = $numero;
			print "<br>".$array[$cont]."</br>";
			$cont++;
		}
		$numero++;
	}
?>

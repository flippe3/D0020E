<?php
	$link = mysqli_connect("localhost", "root", "hackerman", "keyregistry");
 
	// Check connection
	if($link === false){
		die("ERROR: Could not connect. " . mysqli_connect_error());
	}
	 
	// Escape user inputs for security
	$pk = mysqli_real_escape_string($link, $_REQUEST['PublicKey']);
	$name = mysqli_real_escape_string($link, $_REQUEST['Name']);

	// Attempt insert query execution
	$sql = "INSERT INTO users (Name, PublicKey) VALUES ('$name', '$pk')";

	if(mysqli_query($link, $sql)){
		echo "Records added successfully.";
	} 
	else{
		echo "ERROR: Could not able to execute $sql.". mysqli_error($link);
	}
	 
	// Close connection
	mysqli_close($link);
?>
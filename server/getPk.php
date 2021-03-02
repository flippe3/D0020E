<?php
	$json = file_get_contents('php://input');
	$data = json_decode($json);
	$search_val = $data->search_value;

	if (isset($search_val) && $search_val != ""){
		$link = mysqli_connect("localhost", "root", "hackerman", "keyregistry");
		$id = $search_val;

		$request = "SELECT * FROM users WHERE ID='$id'";
		$result = mysqli_query($link, $request);
		
		if(mysqli_num_rows($result)>0){
			$row = mysqli_fetch_assoc($result);
			$pk = $row['PublicKey'];
			$name = $row['Name'];
			echo $pk;
			header("HTTP/1.1 200 OK");
			mysqli_close($link);
		}
		else{
			header("HTTP/1.1 200 OK");
			echo "No record found";
		}
		
	}
	else{
		header("HTTP/1.1 400 Bad Request");
		echo "Invalid request";
	}
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<body>
	<?php
	
		$hostname = "localhost";
		$username = "root";
		$password = "hackerman";
		$db = "keyregistry";

		$dbconnect=mysqli_connect($hostname,$username,$password,$db);

		if ($dbconnect->connect_error){
			die("Database connection failed: " . $dbconnect->connect_error);
		}
	?>
	
	<h1>Complete database table</h1>
	<table border="1" align="center">
		<tr>
			<td>ID</td>
			<td>Public Key</td>
			<td>Name</td>
		</tr>

		<div>
			<?php	
				$query = mysqli_query($dbconnect, "SELECT * FROM users")
					or die (mysqli_error($dbconnect));

				while ($row = mysqli_fetch_array($query)){
					echo
					"<tr>
					<td>{$row['ID']}</td>
					<td>{$row['PublicKey']}</td>
					<td>{$row['Name']}</td>
					</tr>\n";

				}
			?>
		</div>

	</table>
	<form action='http://fnilsson.com/insert.php'>
		<input type='submit' value='Insert data' />
	</form>

</body>
</html>

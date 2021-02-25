<?php
 if (isset($_GET['PK']) && $_GET['PK']!="") {
 $link = mysqli_connect("localhost", "root", "hackerman", "keyregistry");
 $pk = $_GET['PK'];
 $request = "SELECT * FROM users WHERE PublicKey='$pk'";
 #echo $request, "<br>";
 $result = mysqli_query($link, $request);
 if(mysqli_num_rows($result)>0)
 {
 $row = mysqli_fetch_assoc($result);
 $id = $row['ID'];
 $name = $row['Name'];
 response($id, $pk, $name, NULL, NULL);
 mysqli_close($link);
 } else {
   echo "No record found<br>";
   response($id, $pk, NULL, 200,"No Record Found");
 }
} else{
     response(NULL, NULL, NULL, 400,"Invalid Request");  
}

function response($id,$pk,$name, $code, $msg){
 $response['ID'] = $id;
 $response['PublicKey'] = $pk;
 $response['Name'] = $name; 
 $json_response = json_encode($response);
 echo $json_response;
}
?>

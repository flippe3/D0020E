<?php
if (isset($_GET['ID']) && $_GET['ID']!="") {
 $link = mysqli_connect("localhost", "root", "hackerman", "keyregistry");
 $id = $_GET['ID'];
 $request = "SELECT * FROM users WHERE ID='$id'";
 $result = mysqli_query($link, $request);
 if(mysqli_num_rows($result)>0)
 {
 $row = mysqli_fetch_assoc($result);
 $pk = $row['PublicKey'];
 #echo $pk;
 $name = $row['Name'];
 response($id, $pk, $name, NULL, NULL);
 mysqli_close($link);
 } else {
   echo "No record found<br>";
   response($id, NULL, NULL, 200,"No Record Found");
   }
}else{
   response($id, NULL, NULL, 400,"Invalid Request");
}

function response($id,$pk,$name, $code, $msg){
 $response['ID'] = $id;
 $response['PublicKey'] = $pk;
 $response['Name'] = $name; 
 $json_response = json_encode($response);
 echo $json_response;
}
?>
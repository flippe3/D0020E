<?php
if (isset($_GET['ID']) && $_GET['ID']!="") {
 $link = mysqli_connect("localhost", "root", "hackerman", "keyregistry");
 $id = $_GET['ID'];
 $request = "SELECT * FROM users WHERE ID='$id'";
 $result = mysqli_query($link, $request);
 if(mysqli_num_rows($result)>0)
 {
 response($id, 200, "Verified ID");
 mysqli_close($link);
 }else{
  response($id, 200, "Unverified ID"); 
 }
 }else{
   response($id, 400,"Invalid request");
}

function response($id, $code, $msg){
 $response['ID'] = $id;
 $response['code'] = $code;
 $response['msg'] = $msg;
 $json_response = json_encode($response);
 echo $json_response;
}

?>
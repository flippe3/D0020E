<?php
if (isset($_GET['PK']) && $_GET['PK']!="") {
 $link = mysqli_connect("localhost", "root", "hackerman", "keyregistry");

 $pk = $_GET['PK'];
 $request = "SELECT * FROM users WHERE PublicKey='$pk'";
 $result = mysqli_query($link, $request);

 if(mysqli_num_rows($result)>0)
 {
 response($pk, 200, "Verified Public Key");
 mysqli_close($link);
 }else {
  response($pk, 200, "Unverified Public Key");       
 }}
 else{
   response($pk, 400,"Invalid request");
}


function response($pk, $code, $msg){
 $response['PK'] = $pk;
 $response['code'] = $code;
 $response['msg'] = $msg;
 $json_response = json_encode($response);
 echo $json_response;
}

?>
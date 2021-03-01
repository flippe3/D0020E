<?php
$json = file_get_contents('php://input');
$data = json_decode($json);
$search_val = $data->search_value;

if (isset($search_val) && $search_val != "") {
 $link = mysqli_connect("localhost", "root", "hackerman", "keyregistry");
 $id = $search_val;

 $request = "SELECT * FROM users WHERE ID='$id'";
 $result = mysqli_query($link, $request);
 if(mysqli_num_rows($result)>0)
 {
 $row = mysqli_fetch_assoc($result);
 $pk = $row['PublicKey'];
 $name = $row['Name'];
 response($id, $pk, $name, NULL, NULL);
 mysqli_close($link);
 }
 else {
   echo "No record found<br>";
   response($id, NULL, NULL, 200,"No Record Found");
}
}
else{
   echo "Invalid request";
   #response($id, NULL, NULL, 400,"Invalid Request");
}

function response($id,$pk,$name, $code, $msg){
 $response['ID'] = $id;
 $response['PublicKey'] = $pk;
 $response['Name'] = $name; 
 $json_response = json_encode($response);
 #echo $json_response;
 if ($code == NULL){
    echo $pk;
 }
}
?>
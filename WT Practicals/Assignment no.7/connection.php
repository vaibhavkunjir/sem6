<?php
$username=$_POST['username'];
$password=$_POST['password'];
$email=$_POST['email'];

$conn=new mysqli('localhost','root','root','registration');
if($conn->connect_error){
	die('Connection Failed:'.$conn->connect_error);

}else{
	$stmt=$conn->prepare("insert into register(username,password,email)values(?,?,?)");
	$stmt->bind_param("sss",$username,$password,$email);
	$stmt->execute();
	echo "You have successfully registered!";
}
<?php
$yourname=$_POST['yourname'];
$yournumber=$_POST['yournumber'];
$yourorder=$_POST['yourorder'];
$addfood=$_POST['addfood'];
$yourmuch=$_POST['yourmuch'];
$date=$_POST['date'];
$youradd=$_POST['youradd'];
$yourmsg=$_POST['yourmsg'];

$conn=new mysqli('localhost','root','root','food_web');
if($conn->connect_error){
    die('Connection Filed:'.$_conn->connect_error);

}else{
    $stmt=$conn->prepare("insert into order(yourname,yournumber,yourorder,addfood,yourmuch,date,youradd,yourmsg)values(?,?,?,?,?,?,?,? ");
    $stmt->bind_param("ssssssss",$yourname,$yournumber,$yourorder,$addfood,$yourmuch,$date,$youradd,$yourmsg);
    $stmt->execute();
    echo "You have successfully placed your order";
}
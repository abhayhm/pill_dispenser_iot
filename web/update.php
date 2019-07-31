<?php
//reading data to variables from input page
$nopill1m=$_POST['numberpills1m'];
$time1m=$_POST['hour1m'];
$nopill1a=$_POST['numberpills1a'];
$time1a=$_POST['hour1a'];
$nopill1n=$_POST['numberpills1n'];
$time1n=$_POST['hour1a'];

$nopill2m=$_POST['numberpills2m'];
$time2m=$_POST['hour2m'];
$nopill2a=$_POST['numberpills2a'];
$time2a=$_POST['hour2a'];
$nopill2n=$_POST['numberpills2n'];
$time2n=$_POST['hour2a'];

//storing data in text file for further usuage
$file = fopen("data.txt", "w") or die("Unable to open file!");
fwrite($file,$nopill1m." ".$time1m."\n");
fwrite($file,$nopill2m." ".$time2m."\n");

fwrite($file,$nopill1a." ".$time1a."\n");
fwrite($file,$nopill2a." ".$time2a."\n");

fwrite($file,$nopill1n." ".$time1n."\n");
fwrite($file,$nopill2n." ".$time2n."\n");
?>
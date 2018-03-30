<?php
$connect = mysql_connect("localhost", "root", "" ) or die(mysql_error());
$database = mysql_select_db("hackthon") or die(mysql_error());

if($connect){
	echo 'success';
}else{
	echo 'not success';
}

?>
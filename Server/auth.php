<?php
	include 'weibo_auto_auth.class.php';
	include 'config.php';


	$userid = isset($_POST['userid'])?$_POST['userid']:die("未设置userid");
	$password = isset($_POST['password'])?$_POST['password']:die("未设置password");
	$app_key = isset($_POST['app_key'])?$_POST['app_key']:die("未设置app_key");
	$app_secret = isset($_POST['app_secret'])?$_POST['app_secret']:die("未设置app_secret");
	$call_back =  isset($_POST['callback_uri'])?$_POST['callback_uri']:die("未设置callback_uri");

	$automatic_machine = new SaeTOAuthV2Auto($userid,$password,$app_key,$app_secret);

	$automatic_machine->automaticAuth($call_back);
?>
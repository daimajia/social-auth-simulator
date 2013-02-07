<?php
	include 'weibo_auto_auth.class.php';
	include 'config.php';

	//处理认证过程可能出现的错误。
	function error_handler($error_level, $error_message){
		if($error_level == E_USER_WARNING){
			die(json_encode(array("error_msg"=>$error_message)));
		}
	}

	set_error_handler("error_handler");

	$userid = isset($_POST['userid'])?$_POST['userid']:trigger_error("未设置userid",E_USER_WARNING);
	$password = isset($_POST['password'])?$_POST['password']:trigger_error("未设置password",E_USER_WARNING);
	$app_key = isset($_POST['app_key'])?$_POST['app_key']:trigger_error("未设置app_key",E_USER_WARNING);
	$app_secret = isset($_POST['app_secret'])?$_POST['app_secret']:trigger_error("未设置app_secret",E_USER_WARNING);
	$call_back =  isset($_POST['callback_uri'])?$_POST['callback_uri']:trigger_error("未设置callback_uri",E_USER_WARNING);

	try{
		$automatic_machine = new SaeTOAuthV2Auto($userid,$password,$app_key,$app_secret);
		$automatic_machine->automaticAuth($call_back);
	}catch(Exception $e){
		trigger_error("你的用户名和密码可能有误，也有可能是回调地址填写错误，请你再认真检查",E_USER_WARNING);
	}
?>

<?php
include 'saetv2.ex.class.php';
class SaeTOAuthV2Auto extends SaeTOAuthV2{

	public $userid;
	public $password;

	

	public $AUTH_URL = 'https://api.weibo.com/oauth2/authorize';
	public $TOKEN_URL = "https://api.weibo.com/oauth2/access_token";
	public $redirect_uri;
	function __construct($userid, $password, $client_id, $client_secret, $access_token = NULL, $refresh_token = NULL){
		parent::__construct($client_id,$client_secret,$access_token,$refresh_token);
		$this->userid = $userid;
		$this->password = $password;
		$this->debug = false;
	}

	function automaticAuth($callback_uri){
		$authorize_url = $this->getAuthorizeURL($callback_uri);
		$this->redirect_uri = $callback_uri;
		$post_data = array(
			"client_id"=>$this->client_id,
			"redirect_uri"=>$callback_uri,
			"userId"=>$this->userid,
			"passwd"=>$this->password,
			"isLoginSina"=>"0",
			"action"=>"submit",
			"response_type"=>"code"
			);
		$header_data = array(
			"User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0",
			"Host:api.weibo.com",
			"Referer:".$authorize_url
			);
		$reponse = $this->post_data($this->AUTH_URL,http_build_query($post_data),$header_data);
		$code = $this->getCode($reponse['header']);
		
		print_r(json_encode($this->getAccessToken($code)));
	}

	function post_data($url,$post_data,$header_data = NULL){
		$curl = curl_init($url);

		if(empty($header_data) == false)
			curl_setopt($curl, CURLOPT_HTTPHEADER, $header_data);

		curl_setopt($curl,CURLOPT_POST,true);
		curl_setopt($curl, CURLOPT_POSTFIELDS, $post_data);
		curl_setopt($curl,CURLOPT_USERAGENT,"Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0");
		curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, $this->ssl_verifypeer);
		curl_setopt($curl,CURLOPT_FOLLOWLOCATION,true);
		curl_setopt($curl, CURLOPT_COOKIEJAR, "cookie.txt");
    	curl_setopt($curl, CURLOPT_COOKIEFILE, "cookie.txt");
		curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);
		curl_setopt($curl,CURLOPT_HEADER,true);

		if(($response = curl_exec($curl)) == false){
			throw new Exception("<h3>curl_exec出错".curl_error($curl)."</h3>");
		}else{
			$header_size = curl_getinfo($curl,CURLINFO_HEADER_SIZE);
			$header = substr($response,0,$header_size);

			$total_size = curl_getinfo($curl,CURLINFO_CONTENT_LENGTH_DOWNLOAD);
			$body = substr($response,$header_size,$total_size);

			if($this->debug){
				echo "<br/><h3>Header:</h3><hr>";
				echo $header;
				echo "<br/><h3>Body:</h3><hr>";
				echo $body;
			}
			curl_close($curl);
			return array("header"=>$header,"body"=>$body);
		}

	}

	function getAccessToken($code){
		$post_data = array("code"=>$code,"redirect_uri"=>$this->redirect_uri);
		return parent::getAccessToken("code",$post_data);
	}

	function getCode($response_header){
		$pattern = "/code=.+/";
		preg_match($pattern, $response_header,$matches);
		if(!empty($matches)){
			$result = explode("=", $matches[0]);
			return trim($result[1]);
		}else{
			return false;
		}
	}
}

?>
<?php
if ($_SERVER["REMOTE_ADDR"]=="127.0.0.1") {
	if ($_GET["execute"]) {
		$updir = "..";
		if (strpos($_SERVER["DOCUMENT_ROOT"], "_vhosts.zmwsc") !== FALSE) $updir .= "\..\..";
		switch ($_GET["execute"]) {
			case "dostats": 
				chdir($updir);
				exec("dostats.bat");
				header("Location: /stats");
				exit();
				break;
			case "opendocroot":
				exec("start explorer \"".$_SERVER["DOCUMENT_ROOT"]."\"");
				break;
			case "phpinfo":
				phpinfo();
				exit();
			case "stopall":
				chdir($updir);
				exec("mysql_stop.bat");
				header("Location: /_stopServer.zmwsc");
				exit();
				break;
			case "mysqlstart":
				chdir($updir);
				if (version_compare(PHP_VERSION, "5.0.0") == -1) {
					$WShell = com_load("WScript.Shell");
				} else {
					$WShell = new COM("WScript.Shell");
				}
				if ($WShell) {
					$WShell->Run("mysql_start.bat", 0, false);
				} else {
					die("Impossible d'initialiser COM");
				}
				break;
			case "mysqlstop":
				chdir($updir);
				exec("mysql_stop.bat");
				break;
		}
		header("Location: ".$_SERVER["HTTP_REFERER"]."#".$_GET["execute"]);
	}
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="fr">
    <head>		
        <title>ZMWS - Page de Lancement</title>
		<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=iso-8859-1" />
		<link rel="stylesheet" type="text/css" href="css/general.css" media="screen" />
		<link rel="shortcut icon" type="image/x-icon" href="css/images/icones/favicon.ico" />		
		<link rel="icon" type="image/png" href="css/images/icones/favicon.png"/>
	</head>

	<body>
		<div id="header">
			<div id="logo"><h1 class="hidden">ZazouMiniWebServer</h1></div>
			<div id="header_droit">
			<div id="pub"></div>
			<h4 class="hidden">Menu General</h4>
			<!--<ul id="menu_general">
			<li id="link_accueil"><a href="http://www.zmws.com/">Accueil</a></li>
			<li id="link_doc"><a href="http://www.zmws.com/doc/">Documentation</a></li>
			<li id="link_dl"><a href="http://www.zmws.com/dl/">T&eacute;l&eacute;chargements</a></li>
			<li id="link_forum"><a href="http://www.zmws.com/forum/">Communaut&eacute;</a></li>   -->
			</ul>
			</div>
		</div>

		<div id="menu_habillage"></div>
		
	<?php $langue=$_GET['lang'];
		switch ($langue) {
default:
include("francais.php");
   break;
   case "fr":
include("francais.php");
   break;
case "en":
include("english.php");
   break;
}?>
	</body>
</html>

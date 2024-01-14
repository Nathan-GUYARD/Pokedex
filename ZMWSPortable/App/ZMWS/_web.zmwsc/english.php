	<div id="contenu">
		<ul id="cont_menu_sub">
    		<li><span class="nav">Langues</span>		
    		<ul class="menu_sub">		
    		<li><a href="?lang=en" title="English language" ><span class="linker">English</span> <span class="linker_desc">This overview page in your language</span></a></li>		
    		<li><a href="?lang=fr" title="Langue française" ><span class="linker">Français</span> <span class="linker_desc">Voir cette page en français</span></a></li>
    		      </ul>
    		</li>
    		
            <li><span class="nav">Directories</span>
            <ul class="menu_sub">
            <?php
            $rep=opendir('.');
            $bAuMoinsUnRepertoire = false;
            while ($file = readdir($rep)) {
               if($file != '..' && $file !='.' && $file !='') {
                   if (is_dir($file)){
                       if (FALSE === strstr ($file, ".zmwsc") &&
                           $file<>"css" &&
                           $file<>"protected" &&
                           $file<>"icons") {
                           $bAuMoinsUnRepertoire = true;
                           print("<li><span class='linker'><a href='$file/'>$file</a></span>");
                       }
                   }
                }
            }
            if ($bAuMoinsUnRepertoire == false) {
               print("<li><span >");
               print("-&nbsp; No directories &nbsp;-");
               print("</span>");
            }
            closedir($rep);
            clearstatcache();
            ?>
            </ul>
            </li>
            <li><span class="nav">Virtual Hosts</span>
            <ul class="menu_sub">
            <?php
    		$port = $_SERVER["SERVER_PORT"];
    		
            $rep = opendir('_vhosts.zmwsc');
            $bAuMoinsUnRepertoire = false;
            while ($file = readdir($rep)) {
                if ($file != '..' && $file !='.' && $file !='') {
                    if (is_dir('_vhosts.zmwsc/'.$file)){
                        if (FALSE === strstr ($file, ".zmwsc")) {
                            $bAuMoinsUnRepertoire = true;
                            if ($port==80)
                                print("<li><span class='linker'><a href='http://$file/'>$file</a></span>");
                            else
                                print("<li><span class='linker'><a href='http://$file:$port/'>$file</a></span>");
                        }
                    }
                }
            }
            if ($bAuMoinsUnRepertoire == false) {
               print("<li><span >");
               print("-&nbsp; No directories &nbsp;-");
               print("</span>");
            }
            closedir($rep);
            clearstatcache();
            ?>
            </ul>
            </li>
		</ul>
		
		<div id="dr"><h1>First Start</h1>
		
		
		<p id="chapeau_accueil" >
		<strong>Zazouminiwebserver is started now ! And it works ! Congratulations !!!</strong><br /><br />
		You are using now the following version <?php echo $_SERVER["SERVER_SOFTWARE"]."/php-".PHP_VERSION; ?><br />last update 25/08/2020 by E. Blot<br />
		To help you doing your first steps using your new server, here there is a little guide that will surely answer to the 1000 questions you are asking right now ...
		</p>
		<h3>Folders of your website</h3>
		<p class="descriptif">Where shall i put the files of my website ?</p>
		<p class="chapeau" >
		<strong>The files of your website must be placed here :</strong>
		<?php
		$docroot = str_replace("/", "\\", $_SERVER["DOCUMENT_ROOT"]);
		echo "<a class=\"fichiers\" href=\"".$_SERVER["PHP_SELF"]."?execute=opendocroot\">$docroot</a>\n";
		?><br /><br />
		You can rename or delete this file : <?php echo str_replace("/", "\\", $_SERVER["SCRIPT_FILENAME"]); ?> (this page) and you'll get a listing of your files<br /><br />
	</p>
	<h2>Tools</h2>
		<h3>Php Version</h3>
		<p class="descriptif">Which php version is installed ?</p>
		<p class="chapeau">You can read information about your <strong>php version</strong> <a href="<?php echo $_SERVER["PHP_SELF"]."?execute=phpinfo"; ?>">just here</a></p>
		<h3>Databases</h2>
		<p class="descriptif">How do i access and administrate my databases ?</p>
		<p class="chapeau"><a class="hidden" name="mysqlstart"></a><a  class="hidden" name="mysqlstop"></a>-<strong>MySql </strong><?php echo "<i><a href=\"".$_SERVER["PHP_SELF"]."?execute=mysqlstart\" class=\"demarrer\">Start</a> <a href=\"".$_SERVER["PHP_SELF"]."?execute=mysqlstop\" class=\"arreter\">Stop</a></i>\n"; ?><br />	
		you can administrate your databases here : <a href="/phpMyAdmin-4.9.5/">http://localhost<?php if ($port!=80) echo ":$port"; ?>/phpmyadmin/</a><br /><br />	
		
          <h3>Protected folder</h3>
		<p class="descriptif">How can i protect a folder ?</p>
		<p class="chapeau">
		To see an example of a <strong>protected folder</strong>, here there is (login: user1, password: pass1) : <a  class="fichiers" href="/protected/">http://localhost<?php if ($port!=80) echo ":$port"; ?>/protected/</a>.<br /><br />
		<strong>Note</strong>: The protection of this folder is made by the file _access.zmwsc . Just because it's there this folder is protected. The first line is the name of this protection (the one you'll see in the login window), following lines are just pairs of logins and keywords, keywords are separated by the sign  ':'.
		</p>
		<h3>Stats</h3>
		<p class="descriptif">Who visits my website ?</p>
		<p class="chapeau">
		To generate your <strong>stats</strong>, double click on do_stats. Stats will be able to be seen here : <a href="/stats/">http://localhost<?php if ($port!=80) echo ":$port"; ?>/stats/</a>.<br /><br />
		Adding to that you can use <a href="<?php echo $_SERVER["PHP_SELF"]."?execute=dostats"; ?>">this link</a> to <strong>generate and view your awsome stats</strong>.<br /><br />
		<strong>Note</strong>: files of the _conf folder are used to set the look of yours stats.
		</p>
		<h3>Stop server</h3>
		<p class="descriptif">How to stop my server ?</p>
		<p class="chapeau">
		<strong>Stop MySQL and ZazouMiniWebServer</strong><a class="arreter" href="<?php echo $_SERVER["PHP_SELF"]."?execute=stopall"; ?>">Stop it</a>.
		</p>
          <!--
		<h2>Informations</h2>
		
		
		<h3>The Website</h3>
		<p class="chapeau">
		Pay a visit to the website : <a href="http://www.zmws.com">http://www.zmws.com</a><br /><br />
		Wanna know more about your options ? you have <a href="http://www.zmws.com/doc/">a documentation(but in french :/ )</a><br /><br />
		on the site you'll find a <a href="http://www.zmws.com/forum/">forum</a>.
		</p>
		<h3>E-mail</h3>
		<p class="chapeau">
		To send me an e-mail, ask me a question, make me know about options that could be great, say me that you're using the server and more, you can write to <a href="mailto:xavier@xgarreau.org">xavier@xgarreau.org</a>.	
		</p>	-->	
		</div>
		
		
		</div>

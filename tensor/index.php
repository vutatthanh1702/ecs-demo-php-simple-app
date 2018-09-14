<html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <?php 
$command = escapeshellcmd('python test.py Yamazaki3.jpg');
$output = shell_exec($command);
$oparray = preg_split("#[\r\n]+#", $output);
echo $oparray[1];
?> 
 </body>
</html>

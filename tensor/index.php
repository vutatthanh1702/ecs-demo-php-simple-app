<?php
if(isset($_POST['name'])){
$comment = $_POST['name'];
echo $comment;
$command = escapeshellcmd('python test.py Yamazaki3.jpg');
$output = shell_exec($command);
$oparray = preg_split("#[\r\n]+#", $output);
echo $oparray;
}
?>
<!DOCTYPE html>
<html lang = “ja”>
<head>
<meta charset = “UFT-8”>
<title>フォームからデータを受け取る</title>
</head>
<body>
<h1>フォームデータの送信</h1>
	<form action="index.php" method="POST">
    <input type="text" name="name" placeholder="ダルビッシュと入力してください">
    <input type="submit" value="submit">
</form>
</body>
</html>
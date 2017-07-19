
<?php
header("Content-type: text/html");

//call side

$fullPath ='python C:/xampp/htdocs/u-22apitest/testWatson.py';
//$fullPath ='python /home/boku/callpythontest.py'; //vps

header( "Content-Type: application/json; charset=utf-8" );
exec($fullPath,$outpara);//外部コマンドを実行
//print_r ($outpara);

$outjson=json_decode(implode($outpara),true);

$kni=$outjson["images"][0]["classifiers"][0]["classes"];

foreach ($kni as $key => $value ){

    print "class :".$value["class"]."\n";
    print "score :".$value["score"]."\n";
}

?>

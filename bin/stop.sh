 netstat -antpl | grep 9090 | awk '{print $7}' | awk -F '/' '{print $1}' | xargs kill -9

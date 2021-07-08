for i in {1..16}
do
	./load_katran.sh k$i
    cp ~/log.txt ~/log_$i.txt
    pkill katran; sleep 20; ps -ef | grep katran;
done
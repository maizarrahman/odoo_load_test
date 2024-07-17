pid=`ps -eo 'pid,command' | grep odoo-bin | grep -v grep | awk '{print $1}'`
pids=`ps -eo 'pid,command' | grep postgres | grep odoo16 | awk '{print $1}'`
for i in {1..29}
do
    /usr/bin/top -p $pid -b -n 1 | grep $pid | grep -v grep | awk -v date="$(date +'%H:%M:%S')" '{OFS=","; print date,$1,$9,$6}' >> /home/maizar/odoo/odoo14/odoo_stat.csv
    for p in $pids
    do
        /usr/bin/top -p $p -b -n 1 | grep $p | grep -v grep | awk -v date="$(date +'%H:%M:%S')" '{OFS=","; print date,$1,$9,$6}' >> /home/maizar/odoo/odoo14/pg_stat.csv
    done
    sleep 2
done

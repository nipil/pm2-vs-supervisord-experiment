# pm2/supervisor experiment

# with pm2

Prepare

    apt-get update
    apt-get install -y -qq --no-install-recommends nodejs python3 npm
    npm install pm2
    node_modules/pm2/bin/pm2 init simple

Configure

    unix socket : 


Run

    node_modules/pm2/bin/pm2 start
    node_modules/pm2/bin/pm2 status
    node_modules/pm2/bin/pm2 logs
    node_modules/pm2/bin/pm2 stop example
    node_modules/pm2/bin/pm2 del all

# with supervisord (4.2.5 deb 12)
 
Prepare

    apt-get update
    apt-get install -y -qq --no-install-recommends python3 supervisor

Configure

    # show sample documented configuration
    # echo_supervisord_conf

    # simple config
    cp ./supervisord-travail.conf /etc/supervisor/conf.d/

Run

    supervisord -n -c /etc/supervisor/supervisord.conf

    ls -l /var/log/supervisor/

Manage

    $ supervisorctl stop travail:*
    travail:travail_00: stopped
    travail:travail_01: stopped
    travail:travail_02: stopped
    travail:travail_03: stopped
    
    $ supervisorctl status
    travail:travail_00               STOPPED   Nov 12 02:45 PM
    travail:travail_01               STOPPED   Nov 12 02:45 PM
    travail:travail_02               STOPPED   Nov 12 02:45 PM
    travail:travail_03               STOPPED   Nov 12 02:45 PM

    $ supervisorctl start travail:*
    travail:travail_00: started
    travail:travail_01: started
    travail:travail_02: started
    travail:travail_03: started
    
    $ supervisorctl status
    travail:travail_00               RUNNING   pid 12572, uptime 0:00:03
    travail:travail_01               RUNNING   pid 12573, uptime 0:00:03
    travail:travail_02               RUNNING   pid 12574, uptime 0:00:03
    travail:travail_03               RUNNING   pid 12575, uptime 0:00:03

    $ supervisorctl tail -f travail:travail_00 stderr
    ==> Press Ctrl-C to exit <==
    24-11-12 14:56:57,658 INFO: PID 16200: Processing item
    2024-11-12 14:56:59,657 INFO: PID 16200: Processing item
    2024-11-12 14:57:03,658 INFO: PID 16200: Processing item
    2024-11-12 14:57:04,658 INFO: PID 16200: Processing item
    2024-11-12 14:57:08,659 INFO: PID 16200: Processing item
    2024-11-12 14:57:09,659 INFO: PID 16200: Processing item
    2024-11-12 14:57:13,660 INFO: PID 16200: Processing item
    2024-11-12 14:57:16,660 INFO: PID 16200: Processing item
    2024-11-12 14:57:19,661 INFO: PID 16200: Processing item
    2024-11-12 14:57:19,661 INFO: PID 16200: Processing item
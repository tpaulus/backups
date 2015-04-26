#!/usr/bin/python

import os
import subprocess
import time


current_date = time.strftime('%Y%m%d-%H%M')


def mySQL():
    backup_dir = '/backups/db'
    if not os.path.isdir(backup_dir):
        os.mkdir(backup_dir)

    username = '<mySQL Admin Username>'
    password = '<mySQL Admin Password>'

    call = 'mysql'
    call_args = '--user=%s  --password=%s -e "SHOW DATABASES;" | tr -d "| " | grep -v Database' % (username, password)


    all_dbs = str(subprocess.check_output(call + ' ' + call_args, shell=True))

    try:
        os.system('rm -rf %s/tmp' % backup_dir)
    except IOError:
        pass
    except Exception:
        pass

    os.mkdir(backup_dir + '/tmp')

    for db in all_dbs.split():
        if db[:2] == 'wp':
            path = backup_dir + '/tmp/' + db + '.sql'
            os.system(
                'mysqldump --force --opt --user=$%s --password=%s --databases %s > %s' % (username, password, db, path))
        else:
            # Non-WP Database
            pass

    os.system('zip -qmr %s.zip %s/tmp' % (backup_dir + '/' + current_date, backup_dir))


def svr(path='<Folder to Backup>'):
    backup_dir = '/backups/sites'
    if not os.path.isdir(backup_dir):
        os.mkdir(backup_dir)

    os.system('zip -qr %s.zip %s' % (backup_dir + '/' + current_date, path))


def clean():
    backup_locations = ['/backups/db', '/backups/sites']

    for loc in backup_locations:
        backups_list = os.listdir(loc)
        backups_list.sort(reverse=True)

        if len(backups_list) > 5:
            for i in range(len(backups_list)):
                if i <= 5:
                    continue
                else:
                    os.remove(loc + '/' + backups_list[i])


if __name__ == "__main__":
    mySQL()
    svr()
    clean()
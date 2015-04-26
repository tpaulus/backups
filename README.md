# Backup
Python Script that backups mySQL Database and Website Files

## Usage Notes
In order for the script to work properly, some fillers need to be replaced.

* Replace <mySQL Admin Username> (line 16) with the username of the Root user on the instance of mySQL, or alternatively a user who has access to __ALL__ databases.
* Replace <mySQL Admin Password> (line 17) with the corresponding users password.
* Finally, replace <Folder to Backup> (line 45) with the root web folder, commonly `/var/www`.

I run the script daily, and it will only keep the last 5-6 copies in folder at `/backups`; should something go wrong, you can simply roll back the websites bu unzipping the folders and restoring the mySQL DBs. 
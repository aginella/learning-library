# Listener Operations

## Introduction

This lab shows how to perform listener operations, such as starting and stopping the listener, checking the listener status, and so on, using the listener control utility.

Estimated Time: 10 minutes

### Objectives

Check the listener status, stop the listener, restart the listener, and view listener configuration from the command line. 

### Prerequisites

This lab assumes you have -
- A Free Tier, Paid or LiveLabs Oracle Cloud account
- Completed all previous labs successfully.

## Task 1: Set the Environment

To connect to Oracle Database and run SQL commands, set the environment first.

1. Log in to your host as *oracle*, the user who can perform database administration.

1. Open a terminal window and run the command *oraenv* to set the environment variables.

	```
	$ <copy>. oraenv</copy>
	```

1. Enter the Oracle SID *orcl*.

	```
	ORACLE_SID = [oracle] ? <copy>orcl</copy>
	The Oracle base has been set to /u01/app/oracle
	```

	This command also sets the Oracle home path to `/u01/app/oracle/product/21.0.0/dbhome_1`.

1. Change the current working directory to `$ORACLE_HOME/bin`. This is the directory where the listener control utility is located.

	```
	$ <copy>cd /u01/app/oracle/product/21.0.0/dbhome_1/bin</copy>
	```

You have set the environment variables for the active terminal session. You can now connect to Oracle Database and run the commands.

> **Note:** Every time you open a new terminal window, you must set the environment variables to connect to Oracle 	Database from that terminal. Environment variables from one terminal do not apply automatically to other terminals.

Alternatively, you may run the script file `.set-env-db.sh` from the home location and enter the number for `ORACLE_SID`, for example, *3* for `orcl`. It sets the environment variables automatically. 

## Task 2: View the Listener Configuration

Run the `lsnrctl status` command to check whether the listener is up and running and to view the listener configuration. 

1. From `$ORACLE_HOME/bin`, view the listener configuration and the status. 

	```
	$ <copy>./lsnrctl status</copy>
	```

	## Output 

	```
	LSNRCTL for Linux: Version 21.0.0.0.0 - Production on 17-OCT-2021 07:19:03

	Copyright (c) 1991, 2021, Oracle.  All rights reserved.

	Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost.example.com)(PORT=1521)))
	STATUS of the LISTENER
	------------------------
	Alias                     LISTENER
	Version                   TNSLSNR for Linux: Version 21.0.0.0.0 - Production
	Start Date                03-AUG-2021 13:50:41
	Uptime                    74 days 17 hr. 28 min. 21 sec
	Trace Level               off
	Security                  ON: Local OS Authentication
	SNMP                      OFF
	Listener Parameter File   /u01/app/oracle/homes/OraDB21Home1/network/admin/listener.ora
	Listener Log File         /u01/app/oracle/diag/tnslsnr/localhost/listener/alert/log.xml
	Listening Endpoints Summary...
	  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=localhost.example.com)(PORT=1521)))
	  (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC1521)))
	  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=localhost.example.com)(PORT=5500))(Security=(my_wallet_directory=/u01/app/oracle/homes/OraDB21Home1/admin/orcl/xdb_wallet))(Presentation=HTTP)(Session=RAW))
	  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=localhost.example.com)(PORT=5502))(Security=(my_wallet_directory=/u01/app/oracle/homes/OraDB21Home1/admin/orcl/xdb_wallet))(Presentation=HTTP)(Session=RAW))
	Services Summary...
	Service "c48242c6976e2430e0532b83e80aa553.us.oracle.com" has 1 instance(s).
	  Instance "orcl", status READY, has 1 handler(s) for this service...
	Service "orcl.us.oracle.com" has 1 instance(s).
	  Instance "orcl", status READY, has 1 handler(s) for this service...
	Service "orclXDB.us.oracle.com" has 1 instance(s).
	  Instance "orcl", status READY, has 1 handler(s) for this service...
	Service "orclpdb.us.oracle.com" has 1 instance(s).
	  Instance "orcl", status READY, has 1 handler(s) for this service...
	The command completed successfully
	```

	> The Listener Control Utility displays a summary of listener configuration settings, listening protocol addresses, and the services registered with the listener.

If Oracle Database has configured the PDB, you will see a service for each PDB running on the Oracle Database instance.

## Task 3: Stop and Start the Listener

The listener starts automatically when the host system turns on. If a problem occurs in the system or if you manually stop the listener, then you can restart the listener from the command line. 

1. From `$ORACLE_HOME/bin`, stop the listener first, if it is already running. 

	```
	$ <copy>./lsnrctl stop</copy>
	```

	## Output 

	```
	LSNRCTL for Linux: Version 21.0.0.0.0 - Production on 17-OCT-2021 07:27:47

	Copyright (c) 1991, 2021, Oracle.  All rights reserved.


	Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost.example.com)(PORT=1521)))
	The command completed successfully
	```

	Now that you have stopped the listener, run the following steps to check if you can still connect to your Oracle Database.

2. From `$ORACLE_HOME/bin`, log in to SQL Plus as the *SYSTEM* user using the service name *orcl*.

	```
	$ <copy>./sqlplus system@orcl</copy>
	```
	
	## Output
	
	```
	SQL*Plus: Release 21.0.0.0.0 - Production on Mon Jul 12 13:47:41 2021
	Version 21.3.0.0.0

	Copyright (c) 1982, 2021, Oracle. All rights reserved.
	Enter password:
	ERROR:
	ORA-12541: TNS:no listener
	```

	This error indicates that the listener is not running. You can exit the prompt by pressing **Ctrl + C** followed by **Enter**. 

	> **Note:** If the listener is not running on the host, Oracle Enterprise Manager Cloud Control (Oracle EMCC) returns an I/O error indicating failure while establishing connection with your Oracle Database.

3. Restart the listener from the $ORACLE_HOME/bin directory.

	```
	$ <copy>./lsnrctl start</copy>
	```

	## Output.

	```
	LSNRCTL for Linux: Version 21.0.0.0.0 - Production on 17-OCT-2021 07:31:52

	Copyright (c) 1991, 2021, Oracle.  All rights reserved.

	Starting /u01/app/oracle/product/21.0.0/dbhome_1//bin/tnslsnr: please wait...

	TNSLSNR for Linux: Version 21.0.0.0.0 - Production
	System parameter file is /u01/app/oracle/homes/OraDB21Home1/network/admin/listener.ora
	Log messages written to /u01/app/oracle/diag/tnslsnr/localhost/listener/alert/log.xml
	Listening on: (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=localhost.example.com)(PORT=1521)))
	Listening on: (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC1521)))

	Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost.example.com)(PORT=1521)))
	STATUS of the LISTENER
	------------------------
	Alias                     LISTENER
	Version                   TNSLSNR for Linux: Version 21.0.0.0.0 - Production
	Start Date                17-OCT-2021 07:31:52
	Uptime                    0 days 0 hr. 0 min. 0 sec
	Trace Level               off
	Security                  ON: Local OS Authentication
	SNMP                      OFF
	Listener Parameter File   /u01/app/oracle/homes/OraDB21Home1/network/admin/listener.ora
	Listener Log File         /u01/app/oracle/diag/tnslsnr/localhost/listener/alert/log.xml
	Listening Endpoints Summary...
	  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=localhost.example.com)(PORT=1521)))
	  (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC1521)))
	The listener supports no services
	The command completed successfully
	```

	You have restarted the listener on the host again.

	> **Note:** To access Oracle Database, the listener must be up and running. 

4. Check the status of the listener as explained in *Task 2: View the Listener Configuration* of this lab.

	```
	$ <copy>./lsnrctl status</copy>
	```

	You will see an output indicating that the listener service is running.

5. Once again log in to SQL Plus as *SYSTEM* using the service name *orcl*.

	```
	$ <copy>./sqlplus system@orcl</copy>
	```

	## Output

	```
	SQL*Plus: Release 21.0.0.0.0 - Production on Sun Oct 17 07:37:44 2021
	Version 21.3.0.0.0

	Copyright (c) 1982, 2021, Oracle.  All rights reserved.

	Enter password: 
	Last Successful login time: Wed Aug 11 2021 05:52:24 +00:00

	Connected to:
	Oracle Database 21c Enterprise Edition Release 21.0.0.0.0 - Production
	Version 21.3.0.0.0

	SQL> 
	```

Verify that you can now connect to Oracle Database.

Congratulations! You have successfully completed this workshop on *Network Environment Configuration for Oracle Database 21c*. 

In this workshop, you have learned how to configure the https port for CDB and PDB, start and stop the listener, and view the listener configuration. 

## Acknowledgements

- **Author**: Manish Garodia, Principal User Assistance Developer, Database Technologies

- **Contributors**: Suresh Rajan, Prakash Jashnani, Malai Stalin, Subhash Chandra, Dharma Sirnapalli, Subrahmanyam Kodavaluru, Manisha Mati

- **Last Updated By/Date**: Manish Garodia, January 2022


 

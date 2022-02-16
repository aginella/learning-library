# HTTPS Port for CDB and PDB

## Introduction

This lab walks you through the steps to view and set the HTTPS port number for both Container Database (CDB) and Pluggable Database (PDB).

When you create a CDB, Oracle Database Configuration Assistant (Oracle DBCA) automatically assigns it with a unique port number. The listener uses this port to connect to the CDB. You can use the default ports or set new port numbers of your choice for CDB and PDBs using the dynamic protocol registration method.  

Estimated Time: 15 minutes

**Note:** While connecting to Oracle Database, you do not require a password in the following scenarios.
 - The Oracle Database resides on the localhost.
 - The current user (for this lab, it is *oracle* user) is a member of the OSDBA group.

### Objectives

View the dispatcher configuration, check the default HTTPS port numbers for CDB and PDB, and modify the port numbers.

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

1. Change the current working directory to `$ORACLE_HOME/bin`. 

	```
	$ <copy>cd /u01/app/oracle/product/21.0.0/dbhome_1/bin</copy>
	```

You have set the environment variables for the active terminal session. You can now connect to Oracle Database and run the commands.

> **Note:** Every time you open a new terminal window, you must set the environment variables to connect to Oracle Database from that terminal. Environment variables from one terminal do not apply automatically to other terminals.

Alternatively, you may run the script file `.set-env-db.sh` from the home location and enter the number for `ORACLE_SID`, for example, *3* for `orcl`. It sets the environment variables automatically. 

## Task 2: View the Dispatcher Configuration

A dispatcher starts automatically on the TCP/IP protocol. Log in to Oracle Database and view the default dispatcher configuration.

1. From `$ORACLE_HOME/bin`, log in to SQL Plus as `SYSDBA`.

	```
	$ <copy>./sqlplus / as sysdba</copy>
	```
	```
	SQL*Plus: Release 21.0.0.0.0 - Production on Mon Jun 15 16:23:10 2021
	Version 21.3.0.0.0

	Copyright (c) 1982, 2021, Oracle.  All rights reserved.

	Connected to:
	Oracle Database 21c Enterprise Edition Release 21.0.0.0.0 - Production
	Version 21.3.0.0.0
    
    SQL>
	```

2. View the `DISPATCHERS` parameter in the initialization parameter file.

	```
	SQL> <copy>show parameter dispatchers</copy>
	```
	```
	NAME                  TYPE        VALUE
	--------------------- ----------- ------------------------------
	dispatchers           string      (PROTOCOL=TCP) (SERVICE=orclXD
									  B)
	max_dispatchers       integer
	```

	Verify that it includes the `PROTOCOL=TCP` attribute.

## Task 3: Set the HTTPS Port for CDB

The default port for CDB is `5500`. For this lab, change the port to, say, *5501*.

1. 	Verify that the container shows the CDB name, *CDB$ROOT*.

	```
	SQL> <copy>show con_name</copy>
	```
	```
	CON_NAME
	------------------------------
	CDB$ROOT
	```

2. View the current port number of CDB.

	```
	SQL> <copy>select dbms_xdb_config.gethttpsport() from dual;</copy>
	```
	```
	DBMS_XDB_CONFIG.GETHTTPSPORT()
	------------------------------
							  5500
	```

3. Change the HTTPS port number of CDB to *5501*.

	```
	SQL> <copy>exec DBMS_XDB_CONFIG.SETHTTPSPORT(5501);</copy>

	PL/SQL procedure successfully completed.
	```

5. Check the new port number of CDB.

	```
	SQL> <copy>select dbms_xdb_config.gethttpsport() from dual;</copy>
	```
	```
	DBMS_XDB_CONFIG.GETHTTPSPORT()
	------------------------------
							  5501
	```

You have modified the port number for CDB successfully.  

## Task 4: Set the HTTPS Port for PDB

The default port for PDB is `0`. For this lab, change the port to, say, *5502*.

1. View the existing PDBs in your Oracle Database.

	```
	SQL> <copy>show pdbs</copy>
	```
	```
		CON_ID NAME                      OPEN_MODE
	---------- ------------------------- ----------
			 2 PDB$SEED                  READ ONLY
			 3 ORCLPDB                   READ WRITE
	```

2. Change the container to the PDB, for this lab it is *orclpdb*.

	```
	SQL> <copy>alter session set container=orclpdb;</copy>

	Session altered.
	```
	
3.	Verify that the container shows the PDB name you entered.
	
	```
	SQL> <copy>show con_name</copy>
	```
	```
	CON_NAME
	------------------------------
	ORCLPDB
	```

	Open the PDB, if not already open.

	```
	SQL> <copy>alter pluggable database orclpdb open;</copy>

	Pluggable database altered.
	```

	**Note:** If the PDB is in `open` state, the above command returns an error message that the PDB is already open. 

5. View the current port number of PDB.

	```
	SQL> <copy>select dbms_xdb_config.gethttpsport() from dual;</copy>
	```
	```
	DBMS_XDB_CONFIG.GETHTTPSPORT()
	------------------------------
								 0
	```

6. Change the HTTPS port number of PDB to *5502*.

	```
	SQL> <copy>exec DBMS_XDB_CONFIG.SETHTTPSPORT(5502);</copy>

	PL/SQL procedure successfully completed.
	```

7. Check the new port number of PDB.

	```
	SQL> <copy>select dbms_xdb_config.gethttpsport() from dual;</copy>
	```
	```
	DBMS_XDB_CONFIG.GETHTTPSPORT()
	------------------------------
							  5502
	```

You have modified the port number for PDB successfully. You can close from the SQL prompt with the `EXIT` command.

In this lab, you learned how to view the dispatcher configuration and set the https port for CDB and PDB.

You may now **proceed to the next lab**.

## Acknowledgements

- **Author**: Manish Garodia, Principal User Assistance Developer, Database Technologies

- **Contributors**: Suresh Rajan, Prakash Jashnani, Malai Stalin, Subhash Chandra, Dharma Sirnapalli, Subrahmanyam Kodavaluru, Manisha Mati

- **Last Updated By/Date**: Manish Garodia, January 2022


 

## How do you access the database after you connect from the terminal?

1. Log in as opc and then sudo to the grid user.
    login as: opc

    [opc@ed1db01 ~]$ sudo su - grid

2. List all the databases on the system.
    root@ed1db01 ]# srvctl config database -v

    cdbm01 /u02/app/oracle/product/12.1.0/dbhome_2 12.1.0.2.0
    exadb /u02/app/oracle/product/11.2.0/dbhome_2 11.2.0.4.0
    mmdb /u02/app/oracle/product/12.1.0/dbhome_3 12.1.0.2.0

3. Connect as the oracle user and get the details about one of the databases by using the srvctl command.
    [root@ed1db01 ~]# su - oracle
    [oracle@ed1db01 ~]$ . oraenv
    ORACLE_SID = [oracle] ? cdbm01
    The Oracle base has been set to /u02/app/oracle
    [oracle@ed1db01 ~]$ srvctl config database -d cdbm01
    Database unique name: cdbm01 <<== DB unique name
    Database name:
    Oracle home: /u02/app/oracle/product/12.1.0/dbhome_2
    Oracle user: oracle
    Spfile: +DATAC1/cdbm01/spfilecdbm01.ora
    Password file: +DATAC1/cdbm01/PASSWORD/passwd
    Domain: data.customer1.oraclevcn.com
    Start options: open
    Stop options: immediate
    Database role: PRIMARY
    Management policy: AUTOMATIC
    Server pools:
    Disk Groups: DATAC1,RECOC1
    Mount point paths:
    Services:
    Type: RAC
    Start concurrency:
    Stop concurrency:
    OSDBA group: dba
    OSOPER group: racoper
    Database instances: cdbm011,cdbm012 <<== SID
    Configured nodes: ed1db01,ed1db02
    Database is administrator managed

4. Set the ORACLE_SID and ORACLE_UNIQUE_NAME using the values from the previous step.
    [oracle@ed1db01 ~]$ export ORACLE_UNIQUE_NAME=cdbm01
    [oracle@ed1db01 ~]$ export ORACLE_SID=cdbm011
    [oracle@ed1db01 ~]$ sqlplus / as sysdba

    SQL*Plus: Release 12.1.0.2.0 Production on Wed Apr 19 04:10:12 2017

    Copyright (c) 1982, 2014, Oracle. All rights reserved.

    Connected to:
    Oracle Database 12c EE Extreme Perf Release 12.1.0.2.0 - 64bit Production
    With the Partitioning, Real Application Clusters, Automatic Storage Management, Oracle Label Security,
    OLAP, Advanced Analytics and Real Application Testing options



## Acknowledgements
* **Author** - Thea Lazarova, Solution Engineer Santa Monica
* **Contributors** -  Andrew Hong, Solution Engineer Santa Monica


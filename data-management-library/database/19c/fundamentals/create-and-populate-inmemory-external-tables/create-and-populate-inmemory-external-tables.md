# Create and Populate In-memory external tables

## About this Workshop
This 15-minute tutorial shows you how to create and populate in-memory external tables.

Oracle Database 19c enables the population of data from external tables into the In-Memory column store (IM column store). This allows the population of data that is not stored in Oracle Database but in source data files. Nevertheless, the population must be completed manually by executing the `DBMS_INMEMORY.POPULATE` procedure.

In Oracle Database 19c, querying an in-memory enabled external table automatically initiates the population of the external data into the IM column store.

Estimated Lab Time: 15 minutes


### Objectives

In this lab, you will:
- Configure the IM Column Store Size
- Create the Logical Directories for the External Source Files
- Create the In-Memory External Table
- Query the In-Memory External Table
- Find How Data In In-Memory External Table Is Accessed
- Clean Up the Environment


### Prerequisites

- Oracle Database 19c installed
- A CDB and a PDB
- The source data file for the external table: [cent20.dat](https://docs.oracle.com/en/database/oracle/oracle-database/19/tutorial-create-populate-partitions-in-inmemory-external-tables/files/CENT20/cent20.dat). Download the .dat file to the labs directory created on your server in its associated subdirectory, /home/oracle/labs/CENT20

## Prepare your environment

1. Open a terminal window on the desktop.

2. Set the Oracle environment variables. At the prompt, enter **CDB1**.

    ```
    $ <copy>. oraenv</copy>
    CDB1
    ```

## Task 1: Configure the IM Column Store Size

1.  Log in to the CDB root as SYS.
  ```
  <copy>sqlplus / AS SYSDBA</copy>

  ```
  ```
  <copy>ALTER SYSTEM SET inmemory_SIZE = 800M SCOPE=SPFILE; </copy>
  ```

2.  Restart the instance and open the database.
  ```
  <copy>SHUTDOWN IMMEDIATE</copy>
  ```
  ```
  <copy>STARTUP</copy>
  ```
  ```
  <copy>ALTER PLUGGABLE DATABASE pdb1 OPEN;</copy>
  ```

## Task 2: Create the Logical Directories for the External Source Files

In this section, you create the logical directory to store the source data files for external data files of the external table.

1. Log in to the PDB as SYSTEM.
  ```
  <copy>CONNECT system@PDB1
  Enter password: Ora4U_1234 </copy>
  ```

2.  Create the logical directory CENT20 to store the source data file cent20.dat for the CENT20 external source data file.
  ```
  <copy>CREATE DIRECTORY cent20 AS '/home/oracle/labs/CENT20'; </copy>
  ```

## Task 3: Create the In-Memory External Table

1. Create the user that owns the in-memory hybrid partitioned table.
  ```
  <copy>CREATE USER hypt IDENTIFIED BY password;</copy>
  ```

2. Grant the read and write privileges on the directory that stores the source data file, to the table owner.
  ```
  <copy>GRANT read, write ON DIRECTORY cent20 TO hypt;</copy>
  ```

3. Grant the CREATE SESSION, CREATE TABLE, and UNLIMITED TABLESPACE privileges to the table owner.
  ```
  <copy>GRANT create session, create table, unlimited tablespace TO hypt;</copy>
  ```
4. Create the in-memory external table INMEM_EXT_TAB with the following attributes:
  - The table is partitioned by range on the `TIME_ID` column.
  - The default tablespace for external source data files is CENT20.
  - The fields in the records of the external files are separated by comma ','.
  - The in-memory compression is `FOR CAPACITY HIGH`.
  ```
  <copy>CREATE TABLE hypt.inmem_ext_tab (history_event NUMBER, time_id DATE)
   ORGANIZATION EXTERNAL    
      (TYPE ORACLE_LOADER DEFAULT DIRECTORY cent20
       ACCESS PARAMETERS  (FIELDS TERMINATED BY ',')
       LOCATION ('cent20.dat'))
   INMEMORY MEMCOMPRESS FOR CAPACITY HIGH;</copy>
  ```
5. Display the in-memory attributes of the external table.
  ```
  <copy>SELECT * FROM dba_external_tables WHERE owner='HYPT';</copy>
  ```
  Read the Results
  ```
    OWNER   TABLE_NAME      TYP
  ------- --------------- ---
  TYPE_NAME
  ----------------------------------------------------------------
  DEF
  ---
  DEFAULT_DIRECTORY_NAME
  ----------------------------------------------------------------
  REJECT_LIMIT                             ACCESS_
  ---------------------------------------- -------
  ACCESS_PARAMETERS
  ----------------------------------------------------------------
  PROPERTY   INMEMORY INMEMORY_COMPRESS
  ---------- -------- -----------------
  HYPT    INMEM_EXT_TAB   SYS
  ORACLE_LOADER
  SYS
  CENT20
  0                                        CLOB
  FIELDS TERMINATED BY ','
  ALL        ENABLED  FOR CAPACITY HIGH
  ```

## Task 4: Query the In-Memory External Table

1. Query the table. Queries of in-memory external tables must have the QUERY_REWRITE_INTEGRITY initialization parameter set to stale_tolerated.
  ```
  <copy>ALTER SESSION SET query_rewrite_integrity=stale_tolerated;</copy>
  ```
  ```
  <copy>SELECT * FROM hypt.inmem_ext_tab ORDER BY 1;</copy>
  ```
  Read the results
  ```
    HISTORY_EVENT TO_CHAR(TIME_ID,'DD-
  ------------- --------------------
              1 01-JAN-1976
              2 01-JAN-1915
              3 01-JAN-1928
              4 01-JAN-1937
              5 01-JAN-1949
              6 01-FEB-1959
              7 01-FEB-1996
              8 01-FEB-1997
              9 01-FEB-1998
             10 01-FEB-1998

  10 rows selected.
  ```
2. Verify that the data is populated into the IM column store.
    ```
      <copy>SELECT segment_name, tablespace_name, populate_status
  FROM   v$im_segments;</copy>

  SEGMENT_NAME   TABLESPACE_NAME          POPULATE_STAT
  -------------- ------------------------ -------------
  INMEM_EXT_TAB  SYSTEM                   COMPLETED
    ```

    Note: Querying the in-memory external table initiates the population into the IM column store in the same way that it does for an internal table. Executing the DBMS_INMEMORY.POPULATE procedure is not required.

## Task 5: Find How Data In In-Memory External Table Is Accessed

1. Display the execution plan for a query on the in-memory external table with a degree of parallelism of 2.
  ```
  <copy> EXPLAIN PLAN FOR SELECT /*+ PARALLEL(2) */ * FROM hypt.inmem_ext_tab; </copy>
  ```
  ```
  <copy>SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);  
</copy>
  ```
Read the result from the result2 text file. The EXTERNAL TABLE ACCESS INMEMORY FULL operation shows that the external data was accessed from the IM column store after having been populated automatically during the query.
  ```
    PLAN_TABLE_OUTPUT
  ---------------------------------------------------------------------------------------------------------------------
  | Id | Operation                             |Name         |Rows|Bytes|Cost (%CPU)|Time    |   TQ |IN-OUT|PQ Distrib
  ---------------------------------------------------------------------------------------------------------------------
  |   0| SELECT STATEMENT                      |             |102K|2193K|  197   (5)|00:00:01|      |      |            
  |   1| PX COORDINATOR                        |             |    |     |           |        |      |      |            
  |   2|  PX SEND QC (RANDOM)                  |:TQ10000     |102K|2193K|  197   (5)|00:00:01| Q1,00| P->S |QC (RAND)  
  |   3|   PX BLOCK ITERATOR                   |             |102K|2193K|  197   (5)|00:00:01| Q1,00| PCWC |            
  |   4|    EXTERNAL TABLE ACCESS INMEMORY FULL|INMEM_EXT_TAB|102K|2193K|  197   (5)|00:00:01| Q1,00| PCWP |            
  ---------------------------------------------------------------------------------------------------------------------
  Note
  -----
     - Degree of Parallelism is 2 because of hint
  ```

## Task 6: Clean Up the Environment

1. Drop the external table `HYPT.INMEM_EXT_TAB`.
  ```
  <copy>DROP TABLE hypt.inmem_ext_tab PURGE;</copy>
  ```
2. Quit the session.
  ```
  <copy>Quit the session.</copy>
  ```


  ## Acknowledgements
  - **Last Updated By/Date** - Blake Hendricks, Austin Specialist Hub, January 10 2021

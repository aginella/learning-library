# Deinstall Oracle Database

## Introduction

This lab walks you through the steps for stopping and removing the Oracle Database software and deleting the database.  

Estimated Time: 10 minutes

### Objectives

Remove the Oracle Database software, delete Oracle Database, and remove Oracle home from your host system using the *deinstall* command.

> **Note:** If you have any user data in Oracle base or Oracle home locations, then `deinstall` deletes this data. Move your data and files outside Oracle base and Oracle home before running `deinstall`.  

### Prerequisites
This lab assumes you have -
- An Oracle Cloud Account - Please view this workshop's LiveLabs landing page to see which environments are supported.
- Oracle Database 21c installed and configured.
- Completed all previous labs successfully.

## **Task 1:** Remove Oracle Database

To remove Oracle Database from your host system, do the following. 

1.  Log in to your host as *oracle*, the user who can remove Oracle Database.

2.  Change the current working directory to `$ORACLE_HOME/deinstall`. This is the directory where `deinstall` is located.  

    ```
	$ <copy>cd /u01/app/oracle/product/21.0.0/dbhome_1/deinstall</copy>
	```

	> **Note:** Do not shut down the Oracle Database or stop any database processes before running `deinstall`.

3.  Start the Oracle Database deinstallation process with this command.  

    ```
	$ <copy>./deinstall</copy>
	```

    > **Note:** For every step, `deinstall` displays the default input values in brackets \[\]. You can either specify the values manually or press **Enter** to leave the default values and proceed. 

	Output:

    ```
    Checking for required files and bootstrapping ...
    Please wait ...
    Location of logs /tmp/deinstall2021-06-27_09-39-16AM/logs/

    ############ ORACLE DECONFIG TOOL START ############


    ######################### DECONFIG CHECK OPERATION START #########################
    ## [START] Install check configuration ##


    Checking for existence of the Oracle home location /u01/app/oracle/product/21.0.0/dbhome_1
    Oracle Home type selected for deinstall is: Oracle Single Instance Database
    Oracle Base selected for deinstall is: /u01/app/oracle
    Checking for existence of central inventory location /u01/app/oraInventory

    ## [END] Install check configuration ##

    ## [START] GIMR check configuration ##
    Checking for existence of GIMR
    GIMR Home not detected
    ## [END] GIMR check configuration ##

    Network Configuration check config START

    Network de-configuration trace file location: /tmp/deinstall2021-06-27_09-39-16AM/logs/netdc_check2021-06-27_09-39-40AM.log
    ```

4.  The `deinstall` command prompts to specify all single instance listeners that you want to deconfigure.  

    ```
	Specify all Single Instance listeners that are to be de-configured. Enter .(dot) to deselect all.
	[LISTENER]: **Enter**
	```

    Press **Enter** to remove the current listener.

	Output:

    ```
    Network Configuration check config END

    Database Check Configuration START

    Database de-configuration trace file location: /tmp/deinstall2021-06-27_09-46-33AM/logs/databasedc_check2021-06-27_09-46-44AM.log
    ```

5.  If you have multiple Database Instances in your Oracle home, then you can either delete specific database instances or remove all instances together using `deinstall`.   

    > **Note:** To enter specific instance names that you want to delete, use comma as the separator. To remove all the instances, press **Enter**.

    ```
	Use comma as separator when specifying list of values as input
    Specify the list of database names that are configured in this Oracle home [orcl]: **Enter**
	```

    For this lab, press **Enter** to remove the default single instance database.

	Output:

    ```
	###### For Database 'orcl' ###### Single Instance Database The diagnostic destination location of the database: /u01/app/oracle/diag/rdbms/orcl Storage type used by the Database: FS Database file location: /u01/app/oracle/oradata/ORCL,/u01/app/oracle/recovery_area/ORCL Fast recovery area location: /u01/app/oracle/recovery_area/ORCL database spfile location: /u01/app/oracle/dbs/spfileorcl.ora
	```

6.  The `deinstall` command prompts you to modify the details of the discovered databases. The default value is *n* which means no.

    ```
	The details of database(s) orcl have been discovered automatically.
	Do you still want to modify the details of orcl database(s)? [n]: **Enter**
	```

    > **Note:** If you enter `y` in this prompt, `deinstall` allows you to specify the details of your Oracle Database. You can manually enter each detail, such as the type of database, the diagnostic destination location, the storage type, the fast recovery area location, the spfile location, whether Archive Mode is enabled, and so on.  

    For this lab, press **Enter** to select the default value and `deinstall` automatically discovers the details of your Oracle Database.

	Output:

    ```
    Database Check Configuration END

    ######################### DECONFIG CHECK OPERATION END #########################


    ####################### DECONFIG CHECK OPERATION SUMMARY #######################
    Oracle Home selected for deinstall is: /u01/app/oracle/product/21.0.0/dbhome_1
    Inventory Location where the Oracle home registered is: /u01/app/oraInventory
    Following Single Instance listener(s) will be de-configured: LISTENER
    The following databases were selected for de-configuration. The databases will be deleted and will not be useful upon de-configuration : orcl
    Database unique name : orcl
    Storage used : FS
    ```

7.  The `deinstall` command prompts you to confirm removing your Oracle Database. 

    ```
    Do you want to continue (y - yes, n - no)? [n]: y
    ```

    Enter ***y*** to initiate the removal process.

	> **Note:** The default value is **n** which means no. If you directly press Enter or specify **n** here, then `deinstall` exits without removing the Oracle Database.   

    The deconfiguration clean operation creates log files and completes removing the database.

	Output:

    ```
    A log of this session will be written to: '/tmp/deinstall2021-06-27_09-52-56AM/logs/deinstall_deconfig2021-06-27_09-53-03-AM.out'
    Any error messages from this session will be written to: '/tmp/deinstall2021-06-27_09-52-56AM/logs/deinstall_deconfig2021-06-27_09-53-03-AM.err'

    ######################## DECONFIG CLEAN OPERATION START ########################
    ## [START] GIMR configuration update ##
    ## [END] GIMR configuration update ##
    Database de-configuration trace file location: /tmp/deinstall2021-06-27_09-52-56AM/logs/databasedc_clean2021-06-27_09-53-05AM.log
    Database Clean Configuration START orcl
    This operation may take few minutes.

    ######################## DEINSTALL CLEAN OPERATION START ########################
    ## [START] Preparing for Deinstall ##
    Setting LOCAL_NODE to host01
    Setting CRS_HOME to false
    Setting oracle.installer.invPtrLoc to /tmp/deinstall2021-06-27_09-52-56AM/oraInst.loc
    Setting oracle.installer.local to false

    Removing directory '/u01/app/oracle/homes/OraDB21Home1' on node(s) 'host01'
    Checking if Oracle Autonomous Health Framework(AHF)/Oracle Trace File Analyzer(TFA) is configured
    AHF/TFA is not configured
    ## [END] Preparing for Deinstall ##

    Oracle Universal Installer clean START

    Detach Oracle home 'OraDB21Home1' from the central inventory on the local node : Done

    Delete directory '/u01/app/oracle/product/21.0.0/dbhome_1' on the local node : Done

    Delete directory '/u01/app/oraInventory' on the local node : Done

    Delete directory '/u01/app/oracle' on the local node : Done

    You can find a log of this session at:
    '/tmp/deinstall2021-06-27_09-52-56AM/logs//Cleanup2021-06-27_10-03-36AM.log'

    Oracle Universal Installer clean END


    ## [START] Oracle install clean ##


    ## [END] Oracle install clean ##


    ######################### DEINSTALL CLEAN OPERATION END #########################


    ####################### DEINSTALL CLEAN OPERATION SUMMARY #######################
    Successfully detached Oracle home 'OraDB21Home1' from the central inventory on the local node.
    Successfully deleted directory '/u01/app/oracle/product/21.0.0/dbhome_1' on the local node.
    Successfully deleted directory '/u01/app/oraInventory' on the local node.
    Successfully deleted directory '/u01/app/oracle' on the local node.

    Run rm -r /etc/oraInst.loc as root on node(s) host01 at the end of the session.

    Oracle Universal Installer cleanup was successful.

    Run 'rm -r /opt/ORCLfmap' as root on node(s) 'host01' at the end of the session.
    Run 'rm -r /etc/oratab' as root on node(s) 'host01' at the end of the session.
    Oracle deinstall tool successfully cleaned up temporary directories.
    #######################################################################


    ############# ORACLE DEINSTALL TOOL END #############
    ```

    The above message confirms that you have completed the deinstallation and deleted Oracle Database from your host. You can close the terminal window.

> **Note:** The `deinstall` command deletes Oracle Database configuration files, user data, and fast recovery area (FRA) files even if they are located outside of the Oracle base directory path.

You have successfully completed this workshop on *Oracle Database 21c Deinstallation*. 

In this workshop, you have learned how to remove the database software, delete Oracle home and the database components, and remove Oracle Database from your host system.

## Acknowledgements

- **Author** - Manish Garodia, Principal User Assistance Developer, Database Technologies

- **Contributors** - Subrahmanyam Kodavaluru, Suresh Rajan, Prakash Jashnani, Malai Stalin, Subhash Chandra, Dharma Sirnapalli

- **Last Updated By/Date** - Manish Garodia, February 2022

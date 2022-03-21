# OCI Data Flow in the Data Lake

## Introduction

Data is constantly growing being enhanced, validated and updated. That is why once you have the data assets you need to make sure that processing continues to manage the data assets and provide updated values you data lake.

OCI Data Flows handles these processes by loading new data or updating.

Estimated time: 20 minutes

Watch the video below for a quick walk through of the lab.

[](youtube:arWzMjy5-y8)

### Objectives

* Learn how to create OCI Data Flow App
* Learn how to create OCI Data Load 
* Learn how to schedule to automate OCI Data Flow Apps

## Task 1: Create an OCI Data Flow app

You have several choices on how to create applications and languages. You can choose something that makes sense for your environment. First, we are going to take a look at the OCI Data Flow and create an application to read through files in the object storage or data lake.

We have created a python script for you to use as part of your OCI Data Flow application. It requires a little bit of editing to get your ADB ID, user name and password added to script and then uploaded to object storage. We are going to use Cloud Shell to do the editing and upload to our object storage bucket.

Start Cloud Shell

![Start Cloud Shell](./images/cloudshell-open.png " ")

From the current directory (your home directory of your user in Cloud Shell), create a file called livelabs_example.py

```
<copy>
vi live_labs_example.py
</copy>
```
Copy the following script and insert it into the live\_labs\_example.py file you are currently editing in Cloud Shell:

```
<copy>
from pyspark.sql import SparkSession
import sys

def oracle_datasource_example(spark):
    # Wallet  information.
    properties = {"adbId": "replacewithADBID","user" : "replacewithUSER","password": "replacewithPASSWORD"}

    print("Reading data from autonomous database.")
    df = spark.read.format("oracle").option("dbtable", SRC_TABLE).options(**properties).load()

    df.printSchema()

    print("Filtering recommendation.")
    df.filter(df.RECOMMENDED == "Y")

    print("Writing to autonomous database.")
    df.write.format("oracle").mode("overwrite").option("dbtable",TARGET_TABLE).options(**properties).save()

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Python Spark Oracle Datasource Example") \
        .getOrCreate()

    # TODO: PROVIDE THE ARGUMENTS 
    ABD_ID = "replacewithADBID"
    SRC_TABLE = "ADMIN.EXPORT_STREAM_2020_UPDATED" 
    TARGET_TABLE = "ADMIN.MOVIE_GENRE" 
    USERNAME = "replacewithUSER"
    PASSWORD = "replacewithPASSWORD"

    oracle_datasource_example(spark)

    spark.stop()
</copy>
```

After pasting the above script, replace the ADB ID with your autonomous database ocid, replace the username and password for your autonomous database, probably ADMIN, where it stats replacewithXXXX. If you are unsure of your ADB ID, with Cloud Shell still open you can navigate to your ADW database from the hamburger menu to Autonomous Database and **Copy** the OCID to be pasted in the script in Cloud Shell in both places where it states "replacewithADBID".

![Get the ADB ID](./images/getadbid.png " ")

Edit the replacewithXXXXX text with the correct information (paste with right click between the quotation marks:

![Paste ADB ID](./images/editfilepaste.png " ")

![Edited File](./images/editedfile.png " ")

See the edited file for the two places there are edits. When finished editing press **esc** **:wq** to save the file and your changes.

Upload this edited file to your object storage using the command line in Cloud Shell after replacing REPLACEYOURNAME with your actual namespace name (Namespace name can be found in OCI tenancy:

```
<copy>
oci os object put --file live_labs_example.py --namespace REPLACEYOURNAMESPACE --bucket-name dataflow-warehouse
</copy>
```

![Upload File](./images/cloudshellupload.png " ")

Navigate from the hamburger memu to storage and select buckets. And you should see your python script in your dataflow-warehouse bucket ready for you to use in your application.

![Storage Buckets](./images/showbuckets.png " ")

Now, navigate to the OCI Data Flow and click on Create Application.

![Create Data Flow](./images/nav_dataflow.png " ")

For creating the application, you need to have the python code and we are providing an example one. Also you will need to have access to the data files. Enter a name for the application and if you would like a description. Take the other defaults for the first part of the form.

![Create Data Flow](./images/createsparkapp.png " ")

For this example, choose python. Select Object Storage dataflow-warehouse, and then choose the file you just uploaded live\_labs\_example.py

![Create Data Flow](./images/createappconfigure.png " ")

Click on Show advanced options. And enter in the Spark configuration properties the key: spark.oracle.datasource.enabled and the value: true

![Advanced Options](./images/createappadvoptions.png " ")

Click on Create Application.

Now we can run the application by selecting the more option dots and selecting Run from the menu.

![Run Data Flow](./images/runappmanual.png " ")

It of course depends on how big your data file is but this sample takes about two minutes to return successfully. This job has filtered out the data and populated the movie_genre table with the job.

![Completed Data Flow](./images/runappresults.png " ")

You can also monitor your applications in the Spark UI. Click on the application name and click on the Spark UI button.

![Create Data Flow](./images/df_sparkui1.png " ")

And there are additional views to see the details about the jobs and applications running and completed.

![Create Data Flow](./images/df_sparkui2.png " ")

Now let's go back to OCI Data Integrations because we setup some other data sources to load as part of our data integration into the Data Lakehouse and use for additional queries as par of our analysis.

## Task 2: Create OCI Data Integration - Load

First we want to download the customer sales csv file that we can put into our object storage. This will show how you can do integrations from your object storage directly into your ADW or we can use the object storage to filter and change the files and stora back into our object storage without even going to the database.

Download the CSV file:

```
<copy>
https://objectstorage.us-ashburn-1.oraclecloud.com/n/c4u04/b/data_lakehouse/o/custsales_custsales-2020-01.csv
</copy>
```

Upload this file to your object storage bucket dataflow-warehouse:

![Upload to object storage](./images/upload-object-storage.png " ")

Select the custsales_custsales-2020-01.csv file from your downloaded folder and click upload.

Navigate from the Hamburger menu to Analytics & AI, select Data Integration, and from the left menu select **Workspaces**. Here we will see our Workspace Lakehouse that we created as part of our configuration. We are going to then create a data loader task.

![Load Data Task](./images/load-data-task.png " ")

Lets give this task the name of LoadCustomerCSV, and before we create we need to select the project - Project_lakehouse.

![Create Load Data Task](./images/create-load-data-task.png " ")


## Task 3: Create an application for automation

Now you are going to navigate back to the data integration workspace, and click on Application. Click on create application.

![Create Application](./images/create_app.png " ")

Click on Save and Close. It is just a shell of an application where you can now publish tasks to be scheduled and run through the application.

![Create Application](./images/create_app.png " ")

## Task 4: Create and schedule OCI Data Flow apps for automation

Now you are going to navigate back to the project. Click on Task under Details and click on Create Task and choose Integration Task. This task is going to be included in the application.

![Create Data Flow](./images/integrationtask_a.png " ")

Under Data Flow, you are going to click Select and add the Data Flow that you just finished creating in the previous task. Then click Save and Close.

![Create Data Flow](./images/integrationtask.png " ")

Click on the menu for the task and select Publish to Application.

![Add Task](./images/add_task.png " ")

Choose the application that was just created in Task 2.

![Add Task](./images/publish_to_app.png " ")

After the task has been added you will see run task or schedule, and you can navigate to the application. For regular loads of this data and automation, you are going to want to schedule the job to run. Again, to see how this is working now, click on Run.

![Run App](./images/run_app.png " ")

You may now proceed to the next lab.

## Acknowledgements

* **Author** - Michelle Malcher, Database Product Management, Massimo Castelli, Senior Director Product Management
* **Contributors** - 
* **Last Updated By/Date** - Michelle Malcher, Database Product Management, September 2021

# OCI Data Flow in the Data Lake

## Introduction

Data is constantly growing being enhanced, validated and updated. That is why once you have the data assets you need to make sure that processing continues to manage the data assets and provide updated values you data lake.

OCI Data Flows handles these processes by loading new data or updating.

Estimated time: 20 minutes

Watch the video below for a quick walk through of the lab.

[](youtube:arWzMjy5-y8)

### Objectives

* Learn how to create an OCI Data Flow App
* Learn how to create OCI Data Flow from OCI Data Integration
* Learn how to schedule to automate OCI Data Flow Apps

## Task 1: Create an OCI Data Flow app

You have several choices on how to create applications and languages. You can choose something that makes sense for your environment. First, we are going to take a look at the OCI Data Flow and create an application to read through files in the object storage or data lake.

This is just an example of how you can use your already created scripts to run as an application and schedule using OCI Data Flow. This currently only reads the data from a csv file which can be used to populate a table or put the output into the bucket.

First navigate to the OCI Data Flow and click on Create Application.

![Create Data Flow](./images/nav_dataflow.png " ")

For creating the application, you need to have the java jar file and we are providing an example one. Also you will need to have access to the data files. Enter a name for the application and if you would like a description. Take the other defaults for the first part of the form.

![Create Data Flow](./images/df_createapp.png " ")

For this example, choose Java, and check the box for entering the URL manually. Copy and paste from the following into the form. 

![Create Data Flow](./images/df_app_details1.png " ")

```
<copy>
oci://dataflow_sample_apps@bigdatadatasciencelarge/dataflow-java-sample-1.0-SNAPSHOT.jar
</copy>
```
```
<copy>
com.oracle.oci.dataflow.samples.DataFlowJavaSample
</copy>
```
And for the arguments:
```
<copy>
${input} ${output}
</copy>
```
Click on Create Application.

![Create Data Flow](./images/df_app_details2.png " ")

Now we can run the application. Copy and paste the following into the input and output arguments and click run.
Input
```
<copy>
https://objectstorage.us-ashburn-1.oraclecloud.com/n/c4u04/b/data_lakehouse/o/custsales_custsales-2020-01.csv
</copy>
```
Output
You will need to supply the namespace of your tenancy for your dataflow-warehouse bucket, and use this as the output for the process.
```
<copy>
oci://dataflow-warehouse@NAMESPACE
</copy>
```

![Create Data Flow](./images/df_run_app.png " ")

It of course depends on how big your data file is but this sample takes about a minute to return successfully.

![Create Data Flow](./images/df_validate_run.png " ")

You can also monitor your applications in the Spark UI. Click on the application name and click on the Spark UI button.

![Create Data Flow](./images/df_sparkui1.png " ")

And there are additional views to see the details about the jobs and applications running and completed.

![Create Data Flow](./images/df_sparkui2.png " ")

Now let's go back to OCI Data Integrations because we export our data flows from here into an application to run for OCI Data Flows.

## Task 2: Create OCI Data Flow from Data Integration

In this step, we are going to use again Quick Actions to click on Create Data Flow and then use the designer to setup the source and target along with any other filters we would like.

![Create Data Flow](./images/Create_dataflow.png " ")

By default, at the bottom of the designer,  you want to enter the name for the New Data Flow, DataFlow_UploadGenre, and Select the Project that was created in the last lab.

![Create Data Flow](./images/dataflow1.png " ")

Then click Create. This way you can save as you go along to in order not to lose any changes.

From the toolbar, there are sources, targets, filters, joins and other options. You are going to drag the source icon over to the design area. Then start to fill out the details for the source by clicking on Select, and then choose the ADW asset that was created in the first lab. Select the Default Connection, and in Schema, ADMIN. For the Entity choose the MOVIE_GENRE table. 

![Create Data Flow](./images/dataflow2.png " ")

Next you want to filter the data in order not to pull in the entire data set. If this was streaming it or large files this would be an important step.

![Create Data Flow](./images/dataflowfilter.png " ")

Now you are going to drag the Target icon over to the designer area. Target is going to be defined as the Object Storage that was created for the dataflow-warehouse. You can insert, overwrite or merge data with the existing data, and even create a new file or table here. This lab, you are just going to insert data, and choose one file which will overwrite the file each time.

![Create Data Flow](./images/dataflow3.png " ")

Then click on the Data Entity and in the next menu type the name of the folder **File_output**. Choose JSON file. This will put the file based on the data and joins that you create into the data lake and allow other processes to use the data.

![Create Data Flow](./images/dataflow5.png " ")

Save at this step, since you now have your source and target. Now you need to connect the source to the target. Drag the icon onto the designer area between the source and the target.
After Saving the dataflow, click on Validate, and the Snapshot should show 0s for Errors and Warnings.

![Create Data Flow](./images/dataflow6.png " ")

## Task 2: Create an application for automation

Now you are going to navigate back to the data integration workspace, and click on Application. Click on create application.

![Create Application](./images/create_app.png " ")

Click on Save and Close. It is just a shell of an application where you can now publish tasks to be scheduled and run through the application.

![Create Application](./images/create_app.png " ")

## Task 3: Create and schedule OCI Data Flow apps for automation

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

# Add Navigation and Data to Your Web App

## Introduction

This lab shows you how to how to set up navigation between pages in a web app. It also demonstrates other ways of adding data to your app.

Estimated Time: 10 minutes

### Background

Now that you've created the Department and Employee pages, you'll need to make sure users can navigate between these pages in your web app. You can do this by adding buttons that perform specific *actions* when you click them. In Visual Builder, this sequence of actions is known as an *action chain*. You can use and customize predefined actions or define your own. In this lab, you'll add buttons that take you from the Departments page to the Employees pages and back again. Each button is associated with an event that sets off a navigation action chain.

You'll also populate your app's business objects by importing data from a file. You did this for the Location business object in a previous lab; you'll do the same for the Department and Employee business objects in this lab.

## Task 1: Create an Action Chain to Navigate from the Departments Page to the Employees Page

1.  Click the **Web Applications** ![Web Applications icon](./images/vbcsnd_webapp_icon.png) tab in the Navigator, and click **main-departments** under the **hrwebapp** and **main** nodes.

2.  From the Components palette, drag a **Button** from the **Common** components to the **Toolbar**, to the right of the **Create Department** button.

    ![](./images/vbcsnd_cse_s2.png)

3.  In the **General** tab of the Button's Properties pane, change the **Text** field to `Display Employees`.

4.  Click the **Events** tab for the button, then click the **\+ New Event** button. From the menu, select **On 'ojAction'**, the default action suggested for a button click.

    ![](./images/vbcsnd_cse_s4.png)

    An empty action chain with the ID **ButtonActionChain** is created.

5.  From the **Navigation** section of the Actions palette, drag the **Navigate** action to the **+** sign pointed to by the **Start** arrow.

6.  In the Navigate action's Properties pane, select **main-employees** from the **Page** drop-down list.

    ![](./images/vbcsnd_cse_s6.png)

    The action now has the label `Navigate main-employees`.

7.  Click **Preview** ![Preview icon](./images/vbcsnd_run_icon.png) in the header to see how the pages will appear to the user. The application opens in another browser tab.

8. Click **Create Department** and add another department (`IT` on `Floor 2`, for example), then click **Save**. A success message is displayed briefly.

9.  Click **Display Employees**, then click **Create Employee**. Add another employee, specifying the new department, and click **Save**. You'll notice there's no way to get back to the main-departments page from the main-employees page. Close the browser tab.

## Task 2: Create an Action Chain to Navigate from the Employees Page to the Departments Page

1.  In the Web Apps pane, click **main-employees** under the **hrwebapp** and **main** nodes. If necessary, click **Reload page** ![Reload page icon](./images/vbcsnd_refresh_icon.png) to display the new employee you created.

2.  Drag a **Button** component from the Components palette into the **Toolbar**, to the right of the **Create Employee** button.

3.  In the Properties pane, change the **Text** field to `Display Departments`.

4.  Click the **Events** tab for the button, then click the **+ New Event** button and select **On 'ojAction'**.

    Another empty action chain with the ID **ButtonActionChain** is created. Because this action chain is for a different page, it doesn't matter that it has the same name as the one for the main-departments page.

5.  Drag the **Navigate** action from the **Navigation** section of the Actions palette to the **+** sign pointed to by the **Start** arrow.

6.  In the Navigate action's Properties pane, select **main-departments** from the **Page** drop-down list.

    The action now has the label `Navigate main-departments`.

7.  Click **Preview** ![Preview icon](./images/vbcsnd_run_icon.png) to test the pages and navigation. The application opens in another browser tab. Make sure you can get to the Departments page from the Employees page. Close the browser tab.

8. Click **main**, then **Diagram** to view the application's modified page flow. Click the main-departments page to see two navigation icons (![Green navigation icon](images/diagram-navigation-icon-green.png) ![Black navigation icon](images/diagram-navigation-icon-black.png)) appear on the main-employees page, indicating that you can now navigate from main-departments to main-employees and back.

    ![](./images/vbcsnd_cpc_s9.png)

## Task 3: Import Data for the Business Objects

Let's now add data for the Department and Employee business objects. Instead of using the Data Manager to import data, this time you'll use each business object's **Data** tab to do the same thing.

1.  Click [this link](https://objectstorage.us-ashburn-1.oraclecloud.com/p/1Mz1ckG1ORhQmDHfpV7bZofGoCI3zOieZfUeYVcqkVFFifJO6muyWFTaz-4xQ7kH/n/c4u03/b/oci-library/o/WMS4121Department.csv) and save the `Department.csv` file. The file contains six departments for the application.

2.  Click [this link](https://objectstorage.us-ashburn-1.oraclecloud.com/p/CuAsioap8QTLRdQviVqKgkH-D5kFa0q3X45vTu1R0sMw9IPsKFzyXQz5T4d919vS/n/c4u03/b/oci-library/o/WMS4121Employee.csv) and save the `Employee.csv` file. The file contains nine employees for the application.

3.  In the Navigator, click the **Business Objects** ![Business Objects icon](./images/vbcsnd_bo_icon.png) tab, then click the **Objects** tab.

4.  Click **Department**, then click the **Data** tab. The departments you created are displayed.

5.  Click **Import from File** ![Import from File icon](./images/vbcsnd_import_icon_transp.png).

6.  In the Import Data dialog box, select the **Replace** option for **Row Handling** if it's not already selected. Then click the upload box, browse to select the `Department.csv` file, and click **Import**.

  If you run into an error, delete the new department and the new employee you created in the previous task, then try the import again.

  Click **Close** after the file has been successfully imported. Six departments are displayed in the table.
    ![](./images/vbcsnd_imp_s7.png)

7.  Click **Employee** under Business Objects, then click the **Data** tab.

8.  Click **Import from File** ![Import from File icon](./images/vbcsnd_import_icon_transp.png).

9.  In the Import Data dialog box, select the **Replace** option for **Row Handling** if it's not already selected. Then click the upload box, browse to select the `Employee.csv` file, and click **Import**.

  Click **Close** after the file has been successfully imported. Nine employees are displayed in the table.

    ![](./images/vbcsnd_imp_s11.png)

## Acknowledgements

* **Author** - Sheryl Manoharan, Visual Builder User Assistance
* **Last Updated By** - November 2021

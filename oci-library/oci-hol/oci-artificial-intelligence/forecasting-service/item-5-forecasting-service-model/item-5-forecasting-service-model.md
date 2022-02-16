# Lab 3: Train Model and Forecast

## Introduction

In this session, we will show you how to use our create and get forecast APIs. 

*Estimated Time*: 30 minutes

### Objectives

In this lab, you will:
- Learn to use forecast API 
- Learn to get forecasts and predictions intervals for the forecast horizon


### Prerequisites
- A Free tier or paid tenancy account in OCI
- You have completed all the tasks in Lab 2 

## Task 1: Create a Forecast model

Creating a model requires 3 actions to kick off training the forecasting model.

  * Pass the inline data in the payload of the forecast train settings
  * Set other training parameters as show in below code snippet
  * Create Forecast API Call using the /forecasts url

  We pre-define some the parameters of the payload based on the example input data (the one we uploaded in previous lab session)
      ```Python 
      date_col_primary = 'date'
      date_col_add = 'date'
      target_col = 'sales'
      id_col_primary = 'item_id'
      id_col_add = 'item_id'
      data_frequency = 'DAY'
      forecast_frequency = 'DAY'
      forecast_horizon  = 14
        
      ```

In the example below we show how to create the payload for calling create forecast API. 
- "compartmentId": same as tenancy id (refer Task 5 : Create Project ID in Lab 2)
- "projectId": the one you get after creating a project (refer Task 5 : Create Project ID in Lab 2)
- "targetVariables": name of the column in primary data having the target values
- models: models selected for training. Here we are showing some the models implemented in our service.Our AutoML service selects the best model out of all the models selected for training. 
- "forecastHorizon": number of future timesteps for which to forecast 
- "forecastFrequency": 'DAY', 'WEEK', 'MONTH' or 'YEAR' depending on forecast frequency required 
- "isDataGrouped": True if data is grouped or having additional data. False if using only one series with no additional data
- "columnData": inline data (Please refer Task 4: Inline Data preparation in Lab 2)
- "columnSchema": provide column name and data type for each column in the data source
- "dataFrequency": 'DAY', 'WEEK', 'MONTH' or 'YEAR' depending on frequency of input data
- "tsColName": name of the timestamp column 
- "additionalDataSource": column schema for additional data to be provided if using additional data.This field should be removed if there is no additional data.

    ```Python
    %%time

    url = "https://forecasting---------------------.oraclecloud.com/20220101/forecasts"

    payload = json.dumps({
      "compartmentId": compartment_id,
      "displayName": "Forecast Model",
      "description": "Training Forecast Model",
      "projectId": project_id,
      "forecastCreationDetails": {
        "targetVariables": [
          target_col
        ],
        "modelTrainingDetails": {
          "modelType": "UNIVARIATE",
          "models": [
            "SMA",
            "DMA",
            "HWSA",
            "HWSM",
            "SES",
            "DES",
            "SA",
            "SM",
            "UAM",
            "UHM",
            "ARIMA",
            "PROPHET"
          ]
        },
        "forecastHorizon": forecast_horizon,
        "confidenceInterval": "CI_5_95",
        "errorMeasure": "RMSE",
        "forecastTechnique": "ROCV",
        "forecastFrequency": forecast_frequency,
        "isForecastExplanationRequired": True,
        "dataSourceDetails": {
          "type": "INLINE",
          "dataSources": {
            "primaryDataSource": {
              "isDataGrouped": True,
              "columnData": prim_load,
              "columnSchema": [
                {
                  "columnName": date_col_primary,
                  "dataType": "DATE"
                },
                {
                  "columnName": target_col,
                  "dataType": "INT"
                },
                {
                  "columnName": id_col_primary,
                  "dataType": "STRING"
                },
              ],
              "tsColName": date_col_primary,
              "tsColFormat": "yyyy-MM-dd HH:mm:ss",
              "dataFrequency": data_frequency
            },
            "additionalDataSource": {
              "isDataGrouped": True,
              "columnData": add_load,
              "columnSchema": [
                {
                  "columnName": date_col_add,
                  "dataType": "DATE"
                },
                {
                  "columnName": "onpromotion",
                  "dataType": "INT"
                },
                {
                  "columnName": id_col_add,
                  "dataType": "STRING"
                },
              ],
              "tsColName": date_col_add,
              "tsColFormat": "yyyy-MM-dd HH:mm:ss",
              "dataFrequency": data_frequency
            }
          }
        }
      }
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload, auth=auth)
    ```

  We store the response and get forecast id 
    ```Python
    create_forecast_response = json.loads(response.text)
    create_forecast_response
    ```
    The above code snippet give below response :
    ```json
    {'description': 'Training Forecast Model',
    'id': 'ocid1.....................',
    'responseType': None,
    'compartmentId': 'ocid1...................',
    'projectId': 'ocid1..................',
    'displayName': 'Forecast Model',
    'createdBy': None,
    'timeCreated': '2021-12-14T09:17:09.525Z',
    'timeUpdated': '2021-12-14T09:17:09.525Z',
    'lifecyleDetails': None,
    'lifecycleState': 'CREATING',
    'failureMessage': None,
    'forecastCreationDetails': {'targetVariables': ['sales'],
      'modelTrainingDetails': {'modelType': 'UNIVARIATE',
      'models': ['SMA',
        'DMA',
        'HWSA',
        'HWSM',
        'SES',
        'DES',
        'SA',
        'SM',
        'UAM',
        'UHM',
        'ARIMA',
        'PROPHET']},
      'dataSourceDetails': {'type': 'INLINE',
      'dataSources': {'primaryDataSource': {'dataAssetId': None,
        'isDataGrouped': True,
        'tsColName': 'date',
        'dataFrequency': 'DAY',
        'tsColFormat': 'yyyy-MM-dd HH:mm:ss',
        'columnSchema': [{'columnName': 'date', 'dataType': 'DATE'},
          {'columnName': 'sales', 'dataType': 'INT'},
          {'columnName': 'item_id', 'dataType': 'STRING'}],
        'columnData': [['2013-01-01 00:00:00',
          '2013-01-02 00:00:00',
          '2013-01-03 00:00:00',
          '2013-01-04 00:00:00',
          '2013-01-05 00:00:00',
          ...],
          ['0',
          '767',
          '987',
          '652',
          '1095',
          '724',
          ...],
          ['13_BEVERAGES',
          '13_BEVERAGES',
          '13_BEVERAGES',
          '13_BEVERAGES',
          '13_BEVERAGES',
          ...]]},
          'additionalDataSource': {'dataAssetId': None,
        'isDataGrouped': True,
        'tsColName': 'date',
        'dataFrequency': 'DAY',
        'tsColFormat': 'yyyy-MM-dd HH:mm:ss',
        'columnSchema': [{'columnName': 'date', 'dataType': 'DATE'},
          {'columnName': 'onpromotion', 'dataType': 'INT'},
          {'columnName': 'item_id', 'dataType': 'STRING'}],
        'columnData': [['2013-01-01 00:00:00',
          '2013-01-02 00:00:00',
          '2013-01-03 00:00:00',
          '2013-01-04 00:00:00',
          '2013-01-05 00:00:00',
          ...],
          ['0',
          '0',
          '0',
          '0',
          '0',
          ...],
          ['13_BEVERAGES',
          '13_BEVERAGES',
          '13_BEVERAGES',
          '13_BEVERAGES',
          '13_BEVERAGES',
          ...]]}}},
          'forecastHorizon': 14,
      'confidenceInterval': 'CI_5_95',
      'errorMeasure': 'RMSE',
      'forecastTechnique': 'ROCV',
      'forecastFrequency': 'DAY',
      'isForecastExplanationRequired': True},
    'forecastResult': None,
    'freeformTags': {},
    'definedTags': {'Oracle-Tags': {'CreatedBy': 'demo_user',
      'CreatedOn': '2021-12-14T09:17:08.153Z'}},
    'systemTags': {}}

    ```

## Task 2: Get forecast and Prediction Intervals
- Take the forecast ID from response above and create a *Get forecast API* call using below code snippet
- Once the results are produced, the  'lifecycleState' changes to 'ACTIVE'. If it is 'CREATING', then you need to re-run the code below after sometimes.
- The ```forecastResult``` key in the below ```get_forecast_response``` gives us the forecast for the given horizon  
- We also get Prediction Intervals from ```predictionInterval``` key in the response

    It can take sometime to create the forecast depending on the models selected and the size of the input data.  For the dataset we have taken, it should take around 10-15 minutes to give results. Till then you can take a break or focus on other task.

    ```Python
    create_forecast_id = create_forecast_response['id']
    create_forecast_id
    url = "https://forecasting-------------------------.oci.oraclecloud.com/20220101/forecasts/{}".format(create_forecast_id)

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload, auth=auth)
    get_forecast_response = json.loads(response.text)
    get_forecast_response
    ```  
    Forecast Response below :
    ```Json
    {'description': 'Training Forecast Model',
    'id': 'ocid1.....................',
    'responseType': None,
    'compartmentId': 'ocid1...................',
    'projectId': 'ocid1..................',
    'displayName': 'Forecast Model',
    'createdBy': None,
    'timeCreated': '2021-12-14T09:17:09.525Z',
    'timeUpdated': '2021-12-14T09:17:09.525Z',
    'lifecyleDetails': None,
    'lifecycleState': 'ACTIVE',
    'failureMessage': None,
    'forecastCreationDetails': None,
    'forecastResult': {'dataSourceType': 'INLINE',
      'forecast': [{'targetColumn': '13_BEVERAGES',
        'dates': ['2017-08-02 00:00:00',
        '2017-08-03 00:00:00',
        '2017-08-04 00:00:00',
        '2017-08-05 00:00:00',
        '2017-08-06 00:00:00',
        '2017-08-07 00:00:00',
        '2017-08-08 00:00:00',
        '2017-08-09 00:00:00',
        '2017-08-10 00:00:00',
        '2017-08-11 00:00:00',
        '2017-08-12 00:00:00',
        '2017-08-13 00:00:00',
        '2017-08-14 00:00:00',
        '2017-08-15 00:00:00'],
        'forecast': [1609.5647,
        1343.6483,
        1546.2831,
        2087.823,
        1794.3483,
        1497.6057,
        1382.0226,
        1461.8567,
        1259.3473,
        1504.2533,
        1968.2959,
        1646.6401,
        1511.9377,
        1445.6711],
        'predictionInterval': [{'upper': 2086.9155, 'lower': 1128.2715},
        {'upper': 1839.9146, 'lower': 912.95483},
        {'upper': 2013.9352, 'lower': 1082.0677},
        {'upper': 2535.684, 'lower': 1612.1564},
        {'upper': 2251.6038, 'lower': 1325.7798},
        {'upper': 1958.7988, 'lower': 1043.9397},
        {'upper': 1870.6536, 'lower': 925.10504},
        {'upper': 1920.7454, 'lower': 977.78406},
        {'upper': 1715.7109, 'lower': 792.765},
        {'upper': 1948.4724, 'lower': 1027.3519},
        {'upper': 2423.6401, 'lower': 1531.121},
        {'upper': 2116.753, 'lower': 1183.1195},
        {'upper': 1980.629, 'lower': 1068.0222},
        {'upper': 1902.9133, 'lower': 979.5294}]}],
      'metrics': {'trainingMetrics': {'numberOfFeatures': 1,
        'totalDataPoints': 1670},
      'targetColumns': [{'targetColumn': '13_BEVERAGES',
        'bestModel': 'ProphetModel',
        'errorMeasureValue': 248.34917,
        'errorMeasureName': 'RMSE',
        'numberOfMethodsFitted': 13,
        'seasonality': 7,
        'seasonalityMode': 'ADDITIVE',
        'preprocessingUsed': {'aggregation': 'NONE',
          'outlierDetected': 14,
          'missingValuesImputed': 0,
          'transformationApplied': 'NONE'}}]}},
    'freeformTags': {},
    'definedTags': {'Oracle-Tags': {'CreatedBy': 'fc-mcs-team',
      'CreatedOn': '2021-12-14T09:17:08.153Z'}},
    'systemTags': {}}

    ```

Using below code, we can save the forecast as tabular data in a csv file with prediction intervals.


```Python
df_forecasts = pd.DataFrame({'forecast_dates':[],'upper':[],'lower':[],'forecast':[], 'series_id':[]})
for i in range(len(get_forecast_response['forecastResult']['forecast'])):
    
    group = get_forecast_response['forecastResult']['forecast'][i]['targetColumn']
    point_forecast = get_forecast_response['forecastResult']['forecast'][i]['forecast']
    pred_intervals = pd.DataFrame(get_forecast_response['forecastResult']
                              ['forecast'][i]['predictionInterval'],dtype=float)
    out = pred_intervals
    out['forecast'] = point_forecast
    forecast_dates = pd.DataFrame({'forecast_dates':get_forecast_response['forecastResult']['forecast'][i]['dates']})
    forecasts = pd.concat([forecast_dates,out],axis=1)
    forecasts['series_id'] = group
    df_forecasts = df_forecasts.append(forecasts, ignore_index = False)
file_name = 'forecast.csv'
df_forecasts.to_csv(file_name, index = None)          
```
The forecast.csv will be saved in the same folder as the notebook file.

![](images/lab3_task2.png " ")


## Task 3: Get Training Metrics report from the response

* We can also retrieve training metrics report from the response which shows the best model selected using AutoML based on performance on selected error metric. Eg. RMSE in this example. 
* We also get seasonality, outlier detected and other preprocessing methods applied to the series


    ```Python
    get_forecast_response['forecastResult']['metrics']['targetColumns']
    ```

    ```Json
    [{'targetColumn': '13_BEVERAGES',
      'bestModel': 'ProphetModel',
      'errorMeasureValue': 248.34917,
      'errorMeasureName': 'RMSE',
      'numberOfMethodsFitted': 13,
      'seasonality': 7,
      'seasonalityMode': 'ADDITIVE',
      'preprocessingUsed': {'aggregation': 'NONE',
      'outlierDetected': 14,
      'missingValuesImputed': 0,
      'transformationApplied': 'NONE'}}]
    ```

**Congratulations on completing this lab!**

You may now proceed to the next lab

## Acknowledgements

* **Authors**
    * Ravijeet Kumar - Senior Data Scientist - Oracle AI Services
    * Anku Pandey - Data Scientist - Oracle AI Services
    * Sirisha Chodisetty - Senior Data Scientist - Oracle AI Services
    * Sharmily Sidhartha - Principal Technical Program Manager - Oracle AI Services
    * Last Updated By/Date: Ravijeet Kumar, 19th-January 2022

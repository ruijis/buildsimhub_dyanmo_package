"""
This example file demonstrates three features of the API library:
1. retrieve hourly data
2. post-process hourly data
3. Plot the hourly data with plotly package in heat map or line chart
"""

import BuildSimHubAPI as bshapi
import BuildSimHubAPI.postprocess as pp

# project_key can be found in every project (click the information icon next to project name)
project_api_key = 'f98aadb3-254f-428d-a321-82a6e4b9424c'
# model_key can be found in each model information bar
model_api_key = '60952acf-bde2-44fa-9883-a0a78bf9eb56'

# initialize the client
bsh = bshapi.BuildSimHubAPIClient()
results = bsh.model_results(project_api_key, model_api_key)

# get the list of hourly variables
variable_list = results.hourly_data()
print(variable_list)

# select one variable for post processing
variable_name = variable_list[0]
print(variable_name)

# post process use HourlyPlot class
variable_data = results.hourly_data(variable_name)
hourly_plot = pp.HourlyPlot(variable_data, variable_name)
# pandas framework can be retrieved: hourly_plot.pandas_df()
# Heat map plot
# hourly_plot.heat_map_plot()
# hourly_plot.line_chart_plot()

# retrieve more hourly data and combine into one dataframe
variable_data = results.hourly_data('Site Outdoor Air Drybulb Temperature:Environment')
hourly_plot.add_column(variable_data, 'Site Outdoor Air Drybulb Temperature:Environment')
hourly_plot.line_chart_plot()
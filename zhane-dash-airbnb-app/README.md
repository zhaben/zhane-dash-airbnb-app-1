# zhane-dash-airbnb-app

To see the Airbnb dashboard web app, click here: https://zhane-dash-app-1.herokuapp.com

I found the Airbnb data on Kaggle: https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data		

- created this app to visualize the Airbnb listing and metric activity in NYC for 2019.

- used Heroku, a cloud application platform, to deploy it without using javascript. 

- searched Plotly (an interactive, open-source, and browser-based graphing library for Python) for mapping options. 

- decided to use a mapbox map. Mapbox is a mapping platform for custom designed maps - it integrates location into web apps.

- created a mapbox account to get a public access token to plot on mapbox maps with plotly.		
		
- used Dash (a framework for building analytic web apps using Python without Javavascript) to build the app.
  - built dash components (dropdown, checkbox, slider, date picker, graph) to allow the user to filter the data
  - built HTML components to structure items on the webpage
  - built plotly graphs (mapbox, scatterplot, line chart, bar chart) to create a mapbox map based on the documentation		
  - wrote callbacks that connect the dash components and plotly graphs to make everything interactive
		
plotly	https://plotly.com
mapbox	https://www.mapbox.com
dash	https://plotly.com/dash/

Dash core components: https://dash.plotly.com/dash-core-components		
HTML components: https://dash.plotly.com/dash-html-components	
Plotly graphing library maps:  https://plotly.com/python/maps/			
Dash callbacks: https://dash.plotly.com/basic-callbacks	

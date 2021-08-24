## Basic end-to-end Datascience Project
<p align="center">
  <img src="https://user-images.githubusercontent.com/70684994/129488272-b6dc87cc-a1aa-4e82-84d5-2160cc2f8979.png" />
</p>

## Hi
My main aim when I do this projects is smth like PoC (Proof of concept). I wanted to do the project from collecting data to serve it to client.
I picked easy task and showed every steps on it.
I really enjoyed when I do this.

## **You can ask any question about this parts (I can help you, if it is possible)**

In this repo there'll be these parts.
- [Web Scraping](#Web-Scraping)
- [Data Analyzing](#Data-Analyzing)
- [Storing Data In DB](#Storing-Data-In-DB)
- [REST API](#REST-API)
- [CreatingInteractive Dashboard](#Creating-Interactive-Dashboard)
- [Deploying](#Deploying)
  
---
## Web Scraping
I scraped data from oyyo.com. Data are about features of cars and their prices. Actually I only scraped data from only Audi category. Dataset includes about 1040 different cars and their features.
- I used beatifulsoup for scraping
- And I didnt share whole scraping code and data in this repo.
  - Because using data for commercial purposes without permission couldnot be a good idea. I dont wanna cause something like this.
- But if someone need help about web scrabing about other websites, you can contact me.
  - bilallozdemir@outlook.com
  - [@bilallozdemir](https://twitter.com/bilallozdemir)
  
## Data Analyzing
This part is include some:
- Exploratory steps,
- Data cleaning and Preprocessing,
- Basic ML algorith to train
- Grid Search optimization
- Feature Selection
- Saving parameters for REST API.

In this part I didnt spend so much time. I showed some basics. Important tasks requires maybe months of preprocessing and model selection processes as you know. I made only PoC (Proff of concept) study here.
You can check the test set predictions and the y_test values here:
* ![output](https://user-images.githubusercontent.com/70684994/130640178-2926c710-3d85-46ff-a927-9678c21f532b.png)
* It looks pretty good.

**And lastly I saved model and scaler as .sav file to use them later (In rest API and Dashboard).**

## Storing Data In DB
I used MongoDB to store data. Actually as you see this dataset is relational. And Using realtional database like Postgres, mssql or Oracle is a better option. But This is my weekend project and I only wanna store data to connect it my other applications (like Dashboard).
Bc of this I used mongodb. Bc I'll deploy mongodb in my cloud linux machine with docker, only 3-5 lines of codes.
![mongo](https://user-images.githubusercontent.com/70684994/130522674-5da86b3e-bc90-4af5-92bb-0b22035b0e5a.PNG)
* Actually my mongodb running in a docker container but I connected it with ip:port to show a sample to here. It's smth like this.

**This is why I chose mongodb (as an unsuitable option) with this task.**

## REST API
  In this step there is so basic Rest API example. This API takes values of the variables and give prediction score thanks to .sav files.
  - In the prediction page of the dashboard predictions comes from Rest API with sav files. Every requests with valid format, returns the prediction of the machine learning model. (Actually rest API scales the values at the same time) 
  - I didnt use smth like token to authenticate, If could be necessary, we can implement JWT.

## Creating Interactive Dashboard
In this step I made a interactive dashboard app as 2 pages by plotly dash.
This app includes:
- Interactive tools like dropdowns to change parameters of graphs,
- Some basic data visualization examples about data,
- Prediction screen and input boxes for parameters.
- Predicted score of the machine learning algorithm.
  - This prediction engine fed by REST API. 

Again I only use basic examples. When it is requeired we can create awesome data visualization examples.
* **And I have to say that I am really good at making beautiful datavizs.**

# **NOTE: REST API AND DASHBOARD APPLICATION RUNS DEPENDENT ON EACH OTHER!!**

## Deploying
I did deploying part on my cloud linux machine. But firstly I checked it on my local windows machine to see if everything is ok.
And later I compressed the project folder and sent it to linux machine with scp command. Actually deploying process was little hard for me but It was a good experience.

This task included some subtasks like:
- deploying mongodb,
- deploying Rest API,
- Deploying Dash App.

I did them all with docker.
Order is very important here. It should be like this:
- Deploy mongodb as container:
  - Take ip address of mongodb container
- Deploy Rest API,
  - Take Ip address of REST API container 
- Edit dashboard connection informations:
  - Changing REST API connection infos with ip address of REST API. 
  - Changing MongoDb connection infos with ip address of MongoDb. 
- And deploy dash app.

And everything is ok. You can check the example photos now.
![containers](https://user-images.githubusercontent.com/70684994/130521215-cc71b220-b0c5-474b-808e-c2218c34e1e3.PNG)
* twity is a container from my another project. You can check the project [here](https://github.com/bilative/twitter-earthquake-bot). And twitter bot is tweeting if there is bigger than 4 eartquake. Maybe you could follow me on twitter.
* Other 3 ones are containers of this project.
![dataviz](https://user-images.githubusercontent.com/70684994/130521503-4c37f5bf-242a-4f5c-a825-09998323b7f2.PNG)
![example1](https://user-images.githubusercontent.com/70684994/130521210-9d486316-0c21-41f8-a5a0-b20723a37265.PNG)
![example2](https://user-images.githubusercontent.com/70684994/130521214-47226439-fcb3-4717-b7d5-29887e287a0b.PNG)

# THIS PROJECT IS RUNNING ON THE CLOUD 7/24, IF YOU WANT MAYBE I CAN SHARE WITH YOU (NOT EVERYONE) THE DASHBOARD SCREEN CONNECTION URL.
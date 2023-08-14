## Python Web API project

In this repo I am learning Web API technology with FASTAPI. \
I am following a beautiful tutorial [here](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=8474s). \
And you can find author's repo [here](https://github.com/Sanjeev-Thiyagarajan/fastapi-course). 

### Run
- I recommend you to use a virtual env to running the project. \
Type ```python3 -m venv <name>``` in your terminal to create an environment. \
Then activate it by this command. ```source <venv_name> bin activate```
- Make sure you have all the modules in the requirements.txt file in your virtual environment \
- Run the PostgreSQL server. And make sure The db is correct for this project.
- Type and run ```uvicorn app.main:app --reload``` in the terminal. \
Here is your API is now running in your local environment.




### Documentation
![image](./api_doc.png)
To go documentation there are two ways:
- type /docs after the base url.
- type /redoc after the base url.

### Other Sections are coming soon!
### **My Notes**
- The repo is now developing with DB first approach. In Branch: feature-database. \
  **UPDATE** with the feature-orm branch I added orm functionality and removed hard coded db scripts. Also switched to Input/Output model for handling requests and responses
- At this commit I cannot use aouto documentation functionalities. I will solve later.

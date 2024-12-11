## Scholarly Search

### Introduction
CS547 class project, a web application developed by imitating the query functions of Google Scholar, arXiv, IEEE, and other websites. It mainly provides keyword query paper search services for target users such as students and professors.

Through the keywords or query statements entered by the user, the application can quickly retrieve the paper information in the database and find relevant papers, rank them according to the relevance of the content, and then return them to the user. Users can directly access the paper's relevant website by providing a link.

![Project Architecture](https://github.com/sripadanandini/CS547-IR-Scholarly-Search/blob/main/image/Project%20Architecture.png)

### Functions
1. Paper searching and filtering

2. User Management

### Dataset

|columns|description|
|-|-|
|id|INT, Primary key|
|title|TEXT, titles of papers|
|abstract|TEXT, abstracts of papers|
|authors|TEXT, authors of papers|
|published|DATE, the published dates|
|url|TEXT, arXiv link to related papers|


### Requirements
- python 3.13.1
- django 5.1.4
- mysql 8.0.4
- nltk

## Get Started

### Installation
1. If you first time to use **Django**:
```bash
	pip install django
```

2. This project uses **mysqlclient**:
```bash
	pip install mysqlclient
```

3. **nltk** module for **tokenization** and **stemming**:
```bash
	pip install nltk
```

### Instruction
For the database, there are two ways to use it in this project, either creating models and operating data sets based on Django's own ORM framework or directly connecting to an existing database to read and operate data. As an example, here the user-managed data set is operated and managed using the ORM framework, while the paper data is imported from outside. The paper data is also shared here. If you don't want to fetch the paper yourself, you can use it.

- Import the data set in the MySQL command console:
```bash
	source arxiv_papers.sql
```

- Change the database configuration in **setting.py**:
```python
	DATABASES = {  
	        "default": {  
	            "ENGINE": "django.db.backends.mysql",  
	            "NAME": "user_info",  
	            "USER": "XXXXXXX",  
	            "PASSWORD": "XXXXXXX",  
	            "HOST": "127.0.0.1",  
	            "PORT": "3306",  
	        },  
	        "arxiv_papers": {  
	            "ENGINE": "django.db.backends.mysql",  
	            "NAME": "arxiv_papers",  
	            "USER": "XXXXXXX",  
	            "PASSWORD": "XXXXXXX",  
	            "HOST": "127.0.0.1",  
	            "PORT": "3306",  
	        },  
	  
	}
```
### Running
- Run the Django server in the application-related path：
```bash
	python manage.py runserver
```

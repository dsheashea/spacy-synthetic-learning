# Spacy Synthetic Learning

### Setup

#### Requirements:
- Local Postgres 12 installation with supporting database (default is called spacy_synthetic_learning)
- Visual Studio Code build tools to match Python Version https://visualstudio.microsoft.com/vs/older-downloads/
- CUDA Toolkit for GPU Support Only https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html
#### Pacakges:
- django
- psycopg2
- spacy
- spacy-lookups-data

#### Env Variables:
``````
   PG_SPACY_SYNTHETIC_LEARNING_NAME=database_name
   PG_SPACY_SYNTHETIC_LEARNING_USER=database_user
   PG_SPACY_SYNTHETIC_LEARNING_PASS=database_password
   PG_SPACY_SYNTHETIC_LEARNING_HOST=database_host
   PG_SPACY_SYNTHETIC_LEARNING_PORT=database_port
``````

#### Install Spacy model:
`` python -m spacy download en_core_web_sm ``
> There's also en_core_web_lg 
   
### Start

`` python manage.py runserver ``
> Modify port by adding it after runserver ex runserver 8080



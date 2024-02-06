FROM mageai/mageai:latest

ARG USER_CODE_PATH=/home/src/${PROJECT_NAME}

RUN apt-get update
RUN apt-get -y install python3-pip
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install psycopg2-binary

# Note: this overwrites the requirements.txt file in your new project on first run. 
# You can delete this line for the second run :) 
COPY requirements.txt ${USER_CODE_PATH}requirements.txt 

RUN pip3 install -r ${USER_CODE_PATH}requirements.txt
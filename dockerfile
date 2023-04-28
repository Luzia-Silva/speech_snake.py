# start by pulling the python image
FROM python:3.10-slim-buster


# switch working directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . .

# configure the container to run in an executed manner
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
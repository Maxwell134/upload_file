# Set the base image to use
FROM python:3.9

# Set the working directory inside the container
WORKDIR /main

# Copy the requirements file to the working directory
COPY requirements.txt .

RUN pip install flask 
# Copy the rest of the application code to the working directory
COPY . .

# Set the command to run the application
CMD [ "python3", "main.py" ]

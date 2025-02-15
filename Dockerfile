FROM python:3.13-slim
LABEL authors="Matin Karbasioun"

ENTRYPOINT ["top", "-b"]

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV MODE=Development
ENV APP_SETTING_NAME=appSettingsDev
ENV CREDENTIALS_NAME=credentials-dev

# Run app.py when the container launches
CMD ["uvicorn", "main._init_:app", "--host", "0.0.0.0", "--port", "8000"]
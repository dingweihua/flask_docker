FROM python:3.6

# Create app directory
WORKDIR /app

# Bundle app source
COPY src /app

RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "server.py"]
# base image
FROM python:3.9-slim
# working directory 
WORKDIR /app
# Copy 
COPY . /app
# Install 
RUN pip install flask
# Expose 
EXPOSE 5000
# Command 
CMD ["python3", "index.py"]

#uses a lightweight python image
FROM python:3.10-slim

#sets working directory
WORKDIR /app

#installs dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copies project files into container
COPY . .

#what port the container should listen on
EXPOSE 8000

#command that executes when container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
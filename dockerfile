# Step 1: Use an official Python runtime as a base image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file to the container
COPY requirements.txt /app/

# Step 4: Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code
COPY . /app/

# Step 6: Expose the port that the app will run on
EXPOSE 8000

# Step 7: Set the default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Step 1: Use an official, secure, and lightweight Python base image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy only the requirements first to leverage Docker's build cache
COPY requirements.txt .

# Step 4: Install dependencies without storing the download cache
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your application code into the container
COPY . .

# Step 6: Expose the port that your Flask app runs on internally
EXPOSE 5000

# Step 7: Set production environment variables
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Step 8: Use Gunicorn as the production WSGI server to run the app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

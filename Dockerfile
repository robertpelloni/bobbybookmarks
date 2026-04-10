# Use a multi-stage build to keep the image small
FROM node:18-slim AS frontend-builder
WORKDIR /app/client
COPY bobbybookmarks-ui/client/package*.json ./
RUN npm install
COPY bobbybookmarks-ui/client/ ./
# Pass the API URL as a build arg
ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL
RUN npm run build

# Final image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    procps \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copy all source
COPY . .

# Copy the built frontend to where it's served
# Note: In a production Docker setup, you might serve static files via Nginx or similar
# Here we copy it to a location if the Flask/Node app serves it
COPY --from=frontend-builder /app/client/dist ./bobbybookmarks-ui/client/dist

# Expose ports
EXPOSE 3000 3002 5000

# Start script
RUN echo "#!/bin/bash\n\
# Start Flask\n\
gunicorn app:application --bind 0.0.0.0:5000 &\n\
# Start Express\n\
cd bobbybookmarks-ui/server && node server.js &\n\
# Start Worker\n\
python deep_research.py\n\
" > /app/start.sh && chmod +x /app/start.sh

CMD ["/app/start.sh"]

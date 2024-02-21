# Using an official Node.js runtime as the base image
FROM node:18-alpine

# Setting the working directory in the container
WORKDIR /app

# Copying package.json and package-lock.json to the working directory
COPY package.json .
COPY package-lock.json .

# Installing dependencies 
RUN npm install

# Copying the rest of the application code
COPY public/ ./public
COPY src/ ./src

# Exposing the port the app runs on (assuming your frontend app runs on port 3000)
EXPOSE 3000

# Command to run the application
CMD ["npm", "start"]
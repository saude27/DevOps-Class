FROM node:18-alpine

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm install

COPY public/ ./public
COPY src/ ./src

CMD ["npm", "start"]
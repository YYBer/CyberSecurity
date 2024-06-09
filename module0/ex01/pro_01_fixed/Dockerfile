FROM node:14-alpine
WORKDIR /app
COPY index.html .
COPY server.js .
RUN npm init -y && npm install express
RUN npm install express csurf cookie-parser body-parser express-session
EXPOSE 8080
CMD ["node", "server.js"]

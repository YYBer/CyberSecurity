FROM node:14-alpine
WORKDIR /app
COPY index.html .
COPY attacker-amount.html .
COPY server.js .
RUN npm init -y && npm install express
EXPOSE 8070
CMD ["node", "server.js"]

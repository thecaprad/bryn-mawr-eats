FROM node:16-alpine

WORKDIR /usr/src/frontend

COPY package.json ./

RUN yarn install

COPY . .

CMD npm run dev

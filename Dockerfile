FROM alpine

WORKDIR /app

COPY ./requirements.txt .

RUN apk add py3-pip
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY /app .

RUN chmod a+rwx deployment.sh

CMD ["sh", "./deployment.sh"]
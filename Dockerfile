FROM tensorflow/tensorflow

WORKDIR /usr/app

COPY . .

RUN apt-get update && apt-get -y install libgl1-mesa-glx

RUN pip install tensorflow keras flask opencv-python gunicorn

EXPOSE 8000

CMD [ "gunicorn" ]
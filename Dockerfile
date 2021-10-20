FROM tensorflow/tensorflow

WORKDIR /usr/app

COPY . .

ENV CUDA_VISIBLE_DEVICES=-1

RUN apt-get update && apt-get -y install libgl1-mesa-glx

RUN pip install --no-cache-dir tensorflow keras flask opencv-python gunicorn

EXPOSE 8000

CMD [ "gunicorn" ]
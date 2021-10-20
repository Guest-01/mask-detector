FROM tensorflow/tensorflow

WORKDIR /usr/app

COPY . .

ENV CUDA_VISIBLE_DEVICES=-1

RUN apt && apt -y install libgl1-mesa-glx

RUN pip install --no-cache-dir flask opencv-python gunicorn

EXPOSE 8000

CMD [ "gunicorn" ]
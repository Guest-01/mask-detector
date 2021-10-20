FROM tensorflow/tensorflow

WORKDIR /usr/app

COPY . .

ENV CUDA_VISIBLE_DEVICES=-1

ENV FLASK_APP=mask_detector

RUN apt update && apt -y install libgl1-mesa-glx

RUN pip install --no-cache-dir flask opencv-python gunicorn

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]
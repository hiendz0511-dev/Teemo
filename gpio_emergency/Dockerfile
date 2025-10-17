ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG=C.UTF-8
ENV PIP_BREAK_SYSTEM_PACKAGES=1

RUN apk add --no-cache python3 py3-pip python3-dev linux-headers build-base \
    && pip3 install --no-cache-dir \
       RPi.GPIO==0.7.1 gpiozero==1.6.2 paho-mqtt==1.6.1

COPY emergency_button.py /emergency_button.py
CMD ["python3", "/emergency_button.py"]

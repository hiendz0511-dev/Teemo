ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8
RUN apk add --no-cache python3 py3-pip linux-headers build-base \
 && pip3 install --no-cache-dir RPi.GPIO gpiozero paho-mqtt
COPY run.sh /run.sh
COPY emergency_button.py /emergency_button.py
RUN chmod +x /run.sh
CMD ["/run.sh"]

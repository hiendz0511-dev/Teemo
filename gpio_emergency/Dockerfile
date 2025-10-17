ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Cài Python và các lib cần thiết
RUN apk add --no-cache python3 py3-pip python3-dev linux-headers build-base \
  && pip3 install --no-cache-dir RPi.GPIO==0.7.1 gpiozero==1.6.2 paho-mqtt==1.6.1 \
  && rm -rf /root/.cache

# Chép code & services của s6
COPY emergency_button.py /emergency_button.py
COPY rootfs/ /

# BẮT BUỘC: cấp quyền thực thi cho script run của s6
RUN chmod +x /etc/services.d/gpio-emergency/run

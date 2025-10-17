ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Cài lib Python
RUN apk add --no-cache python3 py3-pip python3-dev linux-headers build-base \
  && pip3 install --no-cache-dir RPi.GPIO==0.7.1 gpiozero==1.6.2 paho-mqtt==1.6.1 \
  && rm -rf /root/.cache

# Chép script vào image
COPY emergency_button.py /emergency_button.py
COPY rootfs/ /  # để copy thư mục services.d vào đúng chỗ

# BẮT BUỘC: cho file run có quyền thực thi (GitHub UI không set được executable bit)
RUN chmod +x /etc/services.d/gpio-emergency/run


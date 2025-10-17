ARG BUILD_FROM
FROM $BUILD_FROM

# Sửa ENV về đúng format và cho phép pip cài global trong Alpine 3.22 (PEP 668)
ENV LANG=C.UTF-8 \
    PIP_NO_CACHE_DIR=1 \
    PIP_BREAK_SYSTEM_PACKAGES=1

# Cài Python toolchain + libraries Python cần thiết
RUN apk add --no-cache \
      python3 py3-pip python3-dev linux-headers build-base \
  && pip3 install --no-cache-dir --break-system-packages \
      RPi.GPIO==0.7.1 gpiozero==1.6.2 paho-mqtt==1.6.1 \
  && rm -rf /root/.cache

# Chép code & services
COPY emergency_button.py /emergency_button.py
COPY rootfs/ /

# Đảm bảo script run có quyền thực thi
RUN chmod +x /etc/services.d/gpio-emergency/run

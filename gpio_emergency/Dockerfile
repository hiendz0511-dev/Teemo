ARG BUILD_FROM
FROM $BUILD_FROM

# Locale
ENV LANG=C.UTF-8
# Cho phép pip cài vào system site-packages (trên HA base image)
ENV PIP_BREAK_SYSTEM_PACKAGES=1

# Cài Python + tool biên dịch để build RPi.GPIO trên Alpine
RUN apk add --no-cache \
      python3 \
      py3-pip \
      python3-dev \
      linux-headers \
      build-base \
  && pip3 install --no-cache-dir \
      RPi.GPIO==0.7.1 \
      gpiozero==1.6.2 \
      paho-mqtt==1.6.1 \
  # Giảm kích thước image (nếu gỡ lỗi thì có thể bỏ dòng này)
  && apk del --no-network python3-dev build-base linux-headers || true

# App của bạn
COPY emergency_button.py /emergency_button.py

# S6 services (file run bạn vừa tạo ở rootfs/etc/services.d/gpio-emergency/run)
COPY rootfs/ /

# Bảo đảm file run có quyền thực thi
RUN chmod +x /etc/services.d/gpio-emergency/run

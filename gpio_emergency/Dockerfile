ARG BUILD_FROM
FROM $BUILD_FROM

# Sửa cảnh báo ENV và bật pip cho phép cài global
ENV LANG=C.UTF-8 \
    PIP_NO_CACHE_DIR=1 \
    PIP_BREAK_SYSTEM_PACKAGES=1

# Cài tool build + Python + pip, rồi cài lib Python cần thiết
RUN apk add --no-cache \
      python3 py3-pip python3-dev linux-headers build-base \
  && pip3 install --no-cache-dir --break-system-packages \
      RPi.GPIO==0.7.1 gpiozero==1.6.2 paho-mqtt==1.6.1 \
  && rm -rf /root/.cache

# Chép code và services
COPY emergency_button.py /emergency_button.py
COPY rootfs/ /

# Đảm bảo script run có quyền thực thi (nếu chưa có)
RUN chmod +x /etc/services.d/gpio-emergency/run

# (Nếu bạn đã có CMD/ENTRYPOINT ở dưới thì giữ nguyên;
#  nếu không cần cũng được vì s6 sẽ gọi /etc/services.d/gpio-emergency/run)

import RPi.GPIO as GPIO

import cv2
import time
from datetime import datetime


# GPIO定義
GPIO_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)


# /dev/video0を指定
DEV_ID = 0


# パラメーター
WIDTH = 640
HEIGHT = 480


def main():
  # /dev/video0を指定
  cap = cv2.VideoCapture(DEV_ID)

  # 解像度指定
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

  while True:
    if (GPIO.input(GPIO_PIN) == GPIO.HIGH):

      print("感知！")

      # キャプチャの実施
      ret, frame = cap.read()
      if ret:
        # ファイル名に日付を指定
        date = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = "./" + date + ".jpg"
        cv2.imwrite(path, frame)
        print("保存：" + path)

      # 後処理
      cap.release()
      cv2.destroyAllWindows()
      break
    else:
      time.sleep(1)


if __name__ == "__main__":
  main()


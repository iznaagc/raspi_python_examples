# ------------------------------------------------------
# Import modules
# ------------------------------------------------------
import RPi.GPIO as GPIO
import time
# ======================================================

# ------------------------------------------------------
# Pin definition
# ------------------------------------------------------
pin_no = 17
# ======================================================

# ------------------------------------------------------
# Main Process Function
# ------------------------------------------------------
def main():
  # Setup
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin_no, GPIO.OUT)

  # GPIO17ピンをPWMモードで制御、周波数は100Mh
  pwm = GPIO.PWM(17, 100)
  pwm.start(0) # デューティ比を0に設定(LED消灯)

  try:  
    # Loop
    while True:
        # LEDの明るさを徐々に増やす
        for duty_cycle in range(0, 101, 1): # 0%から100%
          pwm.ChangeDutyCycle(duty_cycle)
          time.sleep(0.02) # 20ms 待つ
        
        # LEDの明るさを徐々に減らす
        for duty_cycle in range(100, -1, -1) # 100%から0%
          pwm.ChangeDutyCycle(duty_cycle)
          time.sleep(0.02) # 20ms 待つ
  except KeyboardInterrupt:
    pass

  pwm.stop() # PWMを停止
  GPIO.cleanup() # GPIOをリセット
# ======================================================

# ------------------------------------------------------
# Program Start
# ------------------------------------------------------
if __name__ == '__main__':
    main()
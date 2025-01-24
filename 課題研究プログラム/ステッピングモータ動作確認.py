import tkinter as tk
import RPi.GPIO as GPIO
import time

# GPIOピン設定（Motor 1用）
MOTOR_PINS = [14, 18, 27, 8]  # 4つの制御ピン

# ステッピングシーケンス（28BYJ-48用）
step_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

# GPIO初期化
GPIO.setmode(GPIO.BCM)
for pin in MOTOR_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# ステッピングモータを回転させる関数
def rotate_motor(steps, direction, step_delay=0.002):
    step_count = len(step_sequence)
    for _ in range(steps):
        for step in range(step_count):
            step_index = step if direction == "CW" else (step_count - step - 1)
            for pin, value in zip(MOTOR_PINS, step_sequence[step_index]):
                GPIO.output(pin, value)
            time.sleep(step_delay)

# ボタン1の動作
def button1_action():
    rotate_motor(64 * 3, "CCW")  # 左に135度回転（1回転=64ステップ x 3ギア比）
    time.sleep(2)               # 2秒保持
    rotate_motor(64, "CCW")     # 左に45度回転
    time.sleep(1)               # 1秒保持
    rotate_motor(128 * 2, "CW") # 右に180度回転

# ボタン2の動作
def button2_action():
    rotate_motor(64 * 3, "CW")  # 右に135度回転
    time.sleep(2)               # 2秒保持
    rotate_motor(64 * 3, "CCW") # 左に180度回転

# GUIのセットアップ
root = tk.Tk()
root.title("Motor Control")

button1 = tk.Button(root, text="Button 1", command=button1_action, width=20, height=2)
button1.pack(pady=10)

button2 = tk.Button(root, text="Button 2", command=button2_action, width=20, height=2)
button2.pack(pady=10)

# GUIループ開始
try:
    root.mainloop()
finally:
    GPIO.cleanup()  # プログラム終了時にGPIOをクリーンアップ

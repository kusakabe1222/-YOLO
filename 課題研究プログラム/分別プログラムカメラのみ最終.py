import cv2 
import tkinter as tk 
from PIL import Image, ImageTk 
from ultralytics import YOLO 
import threading 
import time 
import os 

# 結果保存用のディレクトリを作成 
RESULT_DIR = "run" 
os.makedirs(RESULT_DIR, exist_ok=True) 

# フレームサイズ設定 
FRAME_WIDTH = 320 
FRAME_HEIGHT = 240 

class YOLOApp: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("分別プログラム") 

        # 初期設定 
        self.running = True 
        self.detection_in_progress = False 
        self.detection_countdown = 3  # カウントダウン時間 
        self.hold_time = 5  # 検出結果を保持する時間 
        self.weight_path = "完成ウェイトyolov5.pt"
        self.current_model = YOLO(self.weight_path) 
        self.saved_frame = None 

        # メインウィジェット 
        self.video_label = tk.Label(self.root, text="映像", font=("Arial", 36), bg="gray") 
        self.video_label.pack(fill="both", expand=True) 

        self.result_label = tk.Label(self.root, text="判定結果：", font=("Arial", 24)) 
        self.result_label.pack() 

        self.prediction_label = tk.Label(self.root, text="", font=("Arial", 16), fg="blue") 
        self.prediction_label.pack() 

        self.reset_button = tk.Button(self.root, text="リセット", font=("Arial", 16), command=self.reset) 
        self.reset_button.pack() 

        # カメラとYOLOスレッドの開始 
        self.video_thread = threading.Thread(target=self.video_loop) 
        self.video_thread.daemon = True 
        self.video_thread.start() 

    # リアルタイム映像処理 
    def video_loop(self): 
        cap = cv2.VideoCapture(0) 
        while self.running: 
            ret, frame = cap.read() 
            if not ret: 
                continue 

            # フレームをリサイズ 
            frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT)) 

            if not self.detection_in_progress: 
                detections = self.run_yolo(frame) 
                if detections: 
                    self.start_detection_process(detections, frame) 
                else: 
                    # 映像をリアルタイムで表示 
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
                    frame = Image.fromarray(frame) 
                    frame = ImageTk.PhotoImage(frame) 
                    self.video_label.config(image=frame) 
                    self.video_label.image = frame 

        cap.release() 

    # YOLO推論 
    def run_yolo(self, frame): 
        results = self.current_model(frame) 
        detections = [] 
        for result in results: 
            for box in result.boxes: 
                cls = int(box.cls[0])  # クラスIDを取得 
                if cls == 0: 
                    detections.append("can") 
                elif cls == 1: 
                    detections.append("pet") 
        return detections 

    # 検出処理の開始 
    def start_detection_process(self, detections, frame): 
        self.detection_in_progress = True 
        most_common_label = max(set(detections), key=detections.count)  # 最も多いラベルを判定 
        self.detection_result = "缶" if most_common_label == "can" else "ボトル" 
        self.saved_frame = frame  # 現在のフレームを保存 

        # カウントダウン開始 
        self.countdown_thread = threading.Thread(target=self.countdown_and_display_prediction) 
        self.countdown_thread.start() 

    # カウントダウンと予測結果表示 
    def countdown_and_display_prediction(self): 
        countdown = self.detection_countdown 
        while countdown > 0 and self.running: 
            self.prediction_label.config(text=f"予想結果：{self.detection_result} （あと{countdown}秒）") 
            time.sleep(1) 
            countdown -= 1 

        if self.running: 
            # 判定結果を表示 
            self.prediction_label.config(text="") 
            self.result_label.config(text=f"判定結果：{self.detection_result}") 
            self.display_detection_frame() 

        # 5秒間保持 
        time.sleep(self.hold_time) 
        if self.running: 
            self.end_detection_process() 

    # 検出結果フレームを表示 
    def display_detection_frame(self): 
        if self.saved_frame is not None: 
            # 枠付き画像を保存 
            results = self.current_model(self.saved_frame) 
            annotated_frame = results[0].plot() 
            timestamp = int(time.time()) 
            save_path = os.path.join(RESULT_DIR, f"detection_result_{timestamp}.jpg") 
            cv2.imwrite(save_path, annotated_frame) 

            # 保存画像を表示 
            frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB) 
            frame = Image.fromarray(frame) 
            frame = ImageTk.PhotoImage(frame) 
            self.video_label.config(image=frame) 
            self.video_label.image = frame 

    # 検出完了後のリセット 
    def end_detection_process(self): 
        self.detection_in_progress = False 
        self.result_label.config(text="判定結果：") 
        self.prediction_label.config(text="") 

    # リセット処理 
    def reset(self): 
        self.result_label.config(text="判定結果：") 
        self.prediction_label.config(text="") 
        self.detection_in_progress = False 

    # 終了処理 
    def on_closing(self): 
        self.running = False 
        self.root.destroy() 

# メイン実行 
if __name__ == "__main__": 
    root = tk.Tk() 
    app = YOLOApp(root) 
    root.protocol("WM_DELETE_WINDOW", app.on_closing) 
    root.mainloop()

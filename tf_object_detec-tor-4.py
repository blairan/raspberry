import  cv2
from tflite_runtime.interpreter import  Interpreter
import numpy as np

data_path="lite-model_ssd_mobilenet_v1_1_metadata_2.tflite"
label_path="labelmap.txt"
min_conf_threshold=0.5 #最小信心指數,大於0.5表示已識別物件
#讀取標簽分類名稱
with open(label_path, 'r') as f:
    labels=[line.strip() for line in f.readlines()]


interpreter=Interpreter(model_path=data_path)
interpreter.allocate_tensors()
input_details=interpreter.get_input_details() #取得輸入資訊
output_details=interpreter.get_output_details() #取得輸出資訊
_, h, w, _ = interpreter.get_input_details()[0]["shape"]

cap=cv2.VideoCapture(0)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

while True:
    success, frame = cap.read()
    frame2rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #轉成灰偕
    fResize=cv2.resize(frame2rgb, (w, h))

    input_data=np.expand_dims(fResize, axis=0) #擴充陣列維度
    interpreter.set_tensor(input_details[0]["index"], input_data) #將維度變成可用的資料
    interpreter.invoke() #辨識物體
    boxes=interpreter.get_tensor(output_details[0]['index'])[0]
    classes=interpreter.get_tensor(output_details[1]['index'])[0]
    scroes=interpreter.get_tensor(output_details[2]['index'])[0]

    #計算物體座標並給制方框
    for i in range(len(scroes)):
        if (scroes[i]>min_conf_threshold) and (scroes[i]<=1.0):
            min_y=int(max(1, (boxes[i][0]*height)))
            min_x=int(max(1, (boxes[i][1]*width)))
            max_y=int(min(height, (boxes[i][2]*height)))
            max_x=int(min(width, (boxes[i][3]*width)))
            cv2.rectangle(frame, (min_x, min_y),
                          (max_x, max_y),(10,255,0),2)
            #取出文字內容的尺寸和位置
            object_name=labels[int(classes[i])]
            label=f"{object_name}:{int(scroes[i]*100)}"
            labelSize, baseLine=cv2.getTextSize(label,
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7,2)
            label_min_y=max(min_x, labelSize[1]+10)
            cv2.rectangle(frame, (min_x, label_min_y-labelSize[1]-10),
                          (min_x+labelSize[0], label_min_y+baseLine-10),
                          (255,255,255), cv2.FILLED)
            cv2.putText(frame, label, (min_x, label_min_y-7),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0),2)

    cv2.imshow("object detector", frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()







    



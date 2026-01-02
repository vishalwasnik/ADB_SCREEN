from ppadb.client import Client as AdbClient
import cv2
import numpy as np

# 1. ADB Connection
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

if len(devices) == 0:
    print("Koi device nahi mila! Check USB Debugging.")
    exit()

device = devices[0] # Pehla connected device uthayega

print("Screen sharing start ho rahi hai... 'q' dabaye band karne ke liye.")

while True:
    # 1. Phone se screenshot lena (Binary data)
    raw_image = device.screencap()
    
    # 2. Binary data ko numpy array mein convert karna (Processing ke liye)
    image_array = np.frombuffer(raw_image, dtype=np.uint8)
    
    # 3. Array ko OpenCV format mein decode karna
    frame = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if frame is not None:
        # 4. Image ka size thoda chota karna taaki PC screen par fit aaye (Optional)
        # 0.5 ka matlab 50% chota
        resized_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        
        # 5. PC par live window dikhana
        cv2.imshow("Mobile Screen Live", resized_frame)

    # 'q' dabane par loop band hoga
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
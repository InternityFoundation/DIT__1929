from vidgear.gears import VideoGear
from vidgear.gears import NetGear
import socket
import cv2

HOST = '192.168.1.10'
PORT = 50505

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bind complete')

s.listen(10)
print('Socket now listening')

conn, addr = s.accept()
client = NetGear(receive_mode = True)

# infinite loop
while True:
    # receive frames from network
    frame = client.recv()

    # check if frame is None
    if frame is None:
        #if True break the infinite loop
        break

    # do something with frame here

    # Show output window
    cv2.imshow("Output Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        #if 'q' key-pressed break out
        break

# close output window
cv2.destroyAllWindows()
# safely close client
client.close()

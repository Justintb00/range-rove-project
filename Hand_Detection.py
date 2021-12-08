import cv2
import mediapipe as mp
import time
import websockets, asyncio, json
from time import sleep



class handDetector():
    def __init__(self, mode = False, maxHands = 2, modelComplexity=1, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo = 0, draw = True):

        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
        return lmlist
async def hands():
   async with websockets.connect('ws://firetruck-proj:8080') as client:
        cap = cv2.VideoCapture(0)
        detector = handDetector()
        FingerTip = [4, 8, 12, 16, 20]
        

        while cap.isOpened():
            success, img = cap.read()
            img = detector.findHands(img)
            lmlist = detector.findPosition(img)

            #print(lmlist)
            FPS = int(cap.get(cv2.CAP_PROP_FPS))


            if len(lmlist) != 0:
                fingers = []
                if lmlist[FingerTip[0]][1] > lmlist[FingerTip[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for i in range(1, 5):
                    if lmlist[FingerTip[i]][2] < lmlist[FingerTip[i] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                msg = json.dumps({"message": fingers})
                print(fingers)
                await client.send(msg)
                recv = await client.recv()
                print(f'{recv}')


            cv2.imshow("Image", img)
            cv2.waitKey(1)

async def main():

    await hands()

if __name__ == "__main__":
    asyncio.run(main())

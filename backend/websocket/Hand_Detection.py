import cv2
import mediapipe as mp
from threading import Thread
import asyncio



class handDetector():
    def __init__(self, mode = False, maxHands = 2, modelComplexity=1, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.fingertips = [4,8,12,16,20]

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

    '''
        @TreJohnson - This function analyzes the hand to determine which of the fingertips are "closed" and
        which of the fingertips are open.
    '''
    def analyze_hand(self, img):
        img = self.findHands(img)
        lmlist = self.findPosition(img)
        fingers = []
        
        if len(lmlist) != 0:
            if lmlist[self.fingertips[0]][1] > lmlist[self.fingertips[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for i in range(1, 5):
                if lmlist[self.fingertips[i]][2] < lmlist[self.fingertips[i] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers
    
    async def threading(self, img):
        val = await Thread(target=self.analyze_hand, args=(img, )).start()
        print(val)
        return val
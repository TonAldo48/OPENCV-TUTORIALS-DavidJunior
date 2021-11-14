import cv2 as cv

events = [i for i in dir(cv) if 'EVENT' in i]

for i in events:
    print("{}\n".format(i))
# print(events)
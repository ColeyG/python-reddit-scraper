import prawRequest
import time
import sys

repeatInterval = 86400
amountOfImages = 1

if len(sys.argv) > 1:
    if sys.argv[1] in 'repeat':
        repeating = True
    else:
        print(sys.argv[1] + " is not expected")
else:
    repeating = False


def requests():
    prawRequest.PrawRequest().req("art", amountOfImages, ["images"])
    prawRequest.PrawRequest().req("pics", amountOfImages, ["images"])
    prawRequest.PrawRequest().req("pic", amountOfImages, ["images"])
    prawRequest.PrawRequest().req("pictures", amountOfImages, ["images"])
    prawRequest.PrawRequest().req("images", amountOfImages, ["images"])

    if repeating:
        print("Repeating in " + str(repeatInterval) + " seconds")
        time.sleep(repeatInterval)
        requests()


requests()

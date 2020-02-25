#!/usr/bin/env/python3

#Standard
import requests
import time

#Local 
from samplebase import SampleBase
from rgbmatrix import graphics

first = ""
second = ""

class NextTrain(SampleBase):
    def __init__(self, *args, **kwargs):
        super(NextTrain, self).__init__(*args, **kwargs)
        #self.parser.add_argument("-t", "--text", help="Next Train", default=str("Next Train at: "))

    def determineNext(self):
        URL = 'https://api-v3.mbta.com/schedules'
        stop = 70001
        route = 'Orange'
        direction_id = 1
        sort = 'departure_time'
        limit = 2

        t = time.localtime()
        year = str(t[0])
        month = str(t[1])
        if len(month) == 1: month = "0" + month
        day = str(t[2])
        if len(day) == 1: day = "0" + day
        hour = str(t[3])
        if len(hour) == 1: hour = "0" + hour
        minute = str(t[4])
        if len(minute) == 1: minute = "0" + minute

        min_time = hour + ":" + minute
        date = year + "-" + month + "-" + day

        PARAMS = {'stop':stop, 'route':route, 'direction_id':direction_id, 'min_time':min_time, 'date':date, 'sort':sort}

        r = requests.get(URL, params = PARAMS)

        data = r.json()

        first = data['data'][0]['attributes']['departure_time'].split("T")[1].split("-")[0][:5]
        second = data['data'][1]['attributes']['departure_time'].split("T")[1].split("-")[0][:5]

        return [first, second]

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("6x10.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = 0
        my_text = "Next: " + self.determineNext()[0] + "    After: " + self.determineNext()[1]
        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

# Main Function
if __name__ == "__main__":
    next_train = NextTrain()
    if (not next_train.process()):
        next_train.print_help()


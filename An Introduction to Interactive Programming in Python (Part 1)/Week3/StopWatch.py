# template for "Stopwatch: The Game"
import simplegui

interv = 100
cnt = 0
totalStop = 0
correctStop = 0
stop = True

def format(t):
    tenthOfASeconds = (t) % 10
    seconds = int(t / 10) % 10
    minuits = int(t / 600) % 600
    tenthOfAMinuits = int(t / 100) % 6
    displayNum = str(minuits) + ":" + str(tenthOfAMinuits) + str(seconds) + "." + str(tenthOfASeconds)
    return displayNum
pass

# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global cnt, stop
    stop = False
    timer.start()

def Stop():
    global totalStop, correctStop, stop
    if stop == False:
        if cnt % 10 == 0 and cnt != 0:
            correctStop += 1
            totalStop += 1
        elif cnt != 0:
            totalStop += 1
    stop = True
    timer.stop()
    
def Reset():
    global cnt, correctStop, totalStop
    cnt = 0
    stop = True
    totalStop = 0
    correctStop = 0
    timer.stop()
    
# define event handler for timer with 0.1 sec interval
def tick():
    global cnt
    cnt += 1

# define draw handler
def draw(canvas):
    text = format(cnt)
    canvas.draw_text(text, (100, 150), 42, "white")
    canvas.draw_text(str(correctStop) + "/" + str(totalStop), (190, 30), 24, "blue")
    
# create frame
frame = simplegui.create_frame("Stopwatch Game", 300, 300)
frame.set_canvas_background("skyblue")

# register event handlers
frame.add_button("start", Start, 100)
frame.add_button("stop", Stop, 100)
frame.add_button("reset", Reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interv, tick)

# start frame
frame.start()
Reset()

# Please remember to review the grading rubric

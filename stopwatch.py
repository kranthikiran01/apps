import simplegui
# define global variables
count=0
stop_f=0
stop_t=0
is_stopped=1
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    d=t%10
    c=(t/10)%10
    b=(t/100)%6
    a=(t/600)
    return str(a)+":"+str(b)+str(c)+"."+str(d)
def whole(count):
    """
    boolean function which returns true
    if stopped at whole second
    """
    d=count%10
    if d==0:
        return True
    return False
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_stopped
    is_stopped=0
    timer.start()
def stop():
    global stop_f,stop_t,is_stopped
    timer.stop()
    if(is_stopped==0):
        stop_f+=1
        is_stopped=1
        if whole(count):
            stop_t+=1
def reset():
    global count,is_stopped,stop_f,stop_t
    timer.stop()
    count=0
    stop_f=0
    stop_t=0
# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count+=1
# define draw handler
def draw(canvas):
    global stop_f,stop_t
    canvas.draw_text(format(count),[100,150],50,'Black')
    canvas.draw_text("Score ",[230,25],25,"Red")
    canvas.draw_text(str(stop_t)+"/"+str(stop_f),[235,45],25,'Green')
# create frame
frame=simplegui.create_frame("SWG",300,300)

# register event handlers
timer=simplegui.create_timer(100,tick)
frame.set_canvas_background("White")
frame.set_draw_handler(draw)
frame.add_button("Start",start,200)
frame.add_button("Stop",stop,200)
frame.add_button("Reset",reset,200)
# start frame
frame.start()
# Please remember to review the grading rubric
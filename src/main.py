from tkinter import *
import sys, time


#window
root = Tk()
root.title("Selective repeat animation") 
root.geometry("720x720")
#canvas
c = Canvas(root, height=500, width=500)
c.pack()


#vars
yinc = 1
ydec = -1
p_index = 1
ack_index = 13
motion_speed = 1000 # in mili seconds
rwin_x = 30
swin_x = 120



#sender packets
def create_packets():
	xs = 50
	ys = 70
	for _ in range(12): 
		s_packet = c.create_rectangle(xs, 50, ys, 70, fill="black", activefill="white")
		xs += 30
		ys += 30

#receiver packets
def create_recv_packets():
	xr = 50
	yr = 70
	for _ in range(12):
		r_packet = c.create_rectangle(xr, 304, yr, 324, fill='sky blue', activefill="black")
		xr += 30
		yr += 30

#sender and receiver windows
def create_rcv_sen_win():
	global s_window, r_window
	s_window = c.create_rectangle(46, 46, 164, 74, outline='black')
	r_window = c.create_rectangle(46, 300, 164, 328, outline='dark blue')

#moving window on successfull send and ack event
def move_win():
	pass

#sending packets
def send_packet():
	global yinc, p_index
	if p_index > 12:
		sys.exit("No more packets!!!\nUse Reset button.\n")
	elif yinc <= 22:
		c.move(p_index, 0, yinc)
		yinc += 1
		root.after(200, send_packet)
	elif yinc > 22: 
		send_ack()
		move_recv_win()
		p_index += 1
		yinc = 1
		return 0

#send acknowledgement
def send_ack():
	global ydec, ack_index
	if ydec >= -22:
		c.move(ack_index, 0, ydec)
		ydec -= 1
		root.after(200, send_ack) 
	elif ydec < -22: 
		ack_index += 1
		if (ack_index % 4) == 0:
			move_send_win()
		ydec = -1
		return 0

def move_recv_win():
	global rwin_x, r_window
	c.move(r_window, rwin_x, 0)

def move_send_win():
	global swin_x, s_window
	c.move(s_window, swin_x, 0)

#buttons
send = Button(root, text="Send", fg="Green",font = ("Helvetica", 15), command=send_packet,)
send.config(bg='white', borderwidth=0, activebackground="black", activeforeground="white", relief='sunken')
send.pack()

def main():
	create_packets()
	create_recv_packets()
	create_rcv_sen_win()

if __name__ == "__main__":
	main()

root.mainloop()

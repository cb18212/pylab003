import lab_chat as lc
from lab_chat import join_group
import time

def get_username():
	return input("Please enter your desired username: ").strip().upper()

def get_group():
	return input("What group would you like to join?: ").strip().upper()
def get_message():
	return input("What message would you like to send?: ").strip()


def initialize_chat():
	user = get_username()
	group = get_group()
	node = lc.get_peer_node(user)
	lc.join_group(node, group)
	return lc.get_channel(node, group)

def start_chat():
	channel = initialize_chat()
	while True:
		try:
			msg = get_message()
			if msg == "eris":
				discord("eris.txt", channel)
			elif msg == "bee":
				discord("bee-movie.txt", channel)
			else:
				channel.send(msg.encode('utf-8'))
		except(KeyboardInterrupt, SystemExit):
			break
	channel.send("$$STOP".encode('utf-8'))
	print("FINISHED")

def discord(name, channel):
	source = open(name, "r").readlines()
	for i in source:
		time.sleep(0.25)
		channel.send(i.strip().encode('utf-8'))

start_chat()
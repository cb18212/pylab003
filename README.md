def get_peer_node(username): # function is get_peer_node
* This function most likely creates a connection to another 'node'/version of the program on the local network
* username: unsername of node to attempt to connect to.
* returns a node that you can conect to

def join_group(node, group): #function is join_group
* joins a 'group' in the chatroom
* node: the neighbor to send this message to(the one you joined the p2p network through?)
* group: the group to join

def chat_task(ctx, pipe, n, group): #function is chat_task
* I believe that this function processes commands sent from other nodes, like people joining groups or sending messages
* ctx: no clue what this does, I suppose it stands for 'context'?
* pipe: not really sure on this one either. I suppose it has something to do with directing data??? 
* n: the node to get messages from
* group: the group you want to receive from node n

def get_channel(node, group): # function is get_channel
* creates a child process which gets messages from a channel/group and prints them
* node: node to listen to
* group: group to receive from that node.
* returns a thread which prints output of group
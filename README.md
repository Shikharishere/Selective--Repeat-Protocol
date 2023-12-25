# Selective-Repeat-Protocol
Selective repeat protocol is an sliding window protocol used for reliable data transfer between sender and reciever. This protocol or algorithm comes in handy when a very unreliable link is present. i.e. is there is higher chance of retransmissions. When multiple retransmissions are required this protocol selectively retransmits only those packets as requested by the receiver. Whereas, other sliding window protocols like Go-Back-N tend to retransmit all of the packets(which includes the packets not requested for retransmission). 

*The SR sender must respond to these events:* 
1. ACK recieved
2. Data recieved from layer above
3. Timeout 

*The SR reciever must respond to these events*
1. Packet with correct sequence number recieved
2. If already acked packet is sent again
3. Otherwise ignore the packet

*Note* : This project is not complete yet. A good SR animation can be seen [here](https://media.pearsoncmg.com/ph/esm/ecs_kurose_compnetwork_8/cw/content/interactiveanimations/selective-repeat-protocol/index.html)

### Run directions 
- Activate the venv
    - *Linux* : source .venv/bin/activate
    - *Windows* : /.venv/Scripts/activate.ps1 (for powershell)
- execute main.py
    - python3 main.py 

You should be able to run this project. 

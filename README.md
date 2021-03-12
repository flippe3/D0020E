# D0020E

## Getting started

### Prerequisites
This project uses Python 3.

### Installation
1. Clone the repository
```sh
git clone https://github.com/flippe3/D0020E.git
  ```
2.
```sh
cd D0020E
  ```
3. Install the required packages. 
```sh
python -m pip install -r requirements.txt
  ```
# Demo
[Early PoA demo](https://drive.google.com/file/d/1h7ZIZRRX2PNYf7U505KncbeTq6vk3mtU/view?usp=sharing)
# Current flow
```
OAUTH: Agent->Principal (Requests the PoA)
OAUTH: Agent<-Principal (Sends back the signed PoA)
NETWORKHANDLER: Agent->Vendor (Hands over the PoA)
```

# TODO
* Challenge Response

# Future improvements
## Summary
The implementation to create and use PoAs' is currently in it's most barebones state and is very static. With this we mean that our current use-case is the only the use-case. This problem has arisen due to some key factors. The first factor is the fact that the the project was first built to create a communication flow mimicing OAuth and in that modify the protocol to use PoA's. While this was a success it leads in to the second factor which is the project having a lot of dependencies with a lot of Python class inheritance meaning that modularity is not the the best. These two combined with generally bad project planning led to the point where we had proven the main question of the project but further development would be hard.
## Things not implemented
* Challenge response between agent and principal
* More detailed ways to verify PoA
  * Currently only checks if the Agent and Principal are valid users in the database
  * Should also look at metadata of PoA type and what it gives access to
* The agent could verify the Resource-owner/Vendor is the correct one

### Agent classes
In our project currently we have two classes for running the agent, the standard class and one for the web ui. This became the first hurdle when we wanted to further develop our system. Some of the developers were not able to run the web ui version and could not therefore implement things for it, so if we wanted to implement the challenge response for example it would have to be done in both files and considering small differences in them it could be more work than just copy-pasting.
#### Challenge response in the agent
Regarding the challenge response if it were to be implemented one way to do it is by omitting/modifying the discovery process which starts the communication flow. Instead of asking for a discovery and getting the id (note that this id is just an id to keep track of the active communications) you could instead request a challenge. When the challenge is received the agent gives the response and with that the principal will respond if the agent got approved or not. If the agent succeeded the challenge the principal could provide the id in that response thus removing the actual discovery check. A flow could look something like this.
```
Agent -> (Challenge request)  -> Principal 
Agent <-    (Challenge)       <- Principal
Agent -> (Challenge response) -> Principal
                                    |
                        Denied  |Verifies|
Agent <-  (Response) ---------- |response|
                                   |
                                   | Accepted
Agent <- (Response + ID)  <------- |
  |
 Continues with 
 requesting poa

```

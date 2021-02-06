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
[Early PoA demo](https://i.imgur.com/nCyyo16.mp4)
# Current flow
```
OAUTH: Agent->Principal (Requests the PoA)
OAUTH: Agent<-Principal (Sends back the signed PoA)
NETWORKHANDLER: Agent->Vendor (Hands over the PoA)
```

# TODO
* Make the vendor send a message back saying the PoA verified.
* Generalizations
  * Multiple PoAs
  * Letting the Agent input more data to the PoA metadata

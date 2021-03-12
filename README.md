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
## Disclaimer
When talking about users in this section it refers to users that are registered with the resource owner. A user could be either an agent or a principal. 
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
Agent <-  (Response) -----------|response|
                                    |
                                    | Accepted
Agent <- (Response + ID)  <-------- |
  |
Continues with 
requesting poa
```
#### Making them work together
Instead of creating two classes that look almost identical, revisions should have been made in Agent.py instead to support the changes needed for it to work in the WebHostServer. This would have been very easy to do in hindsight but with stress from other courses it was overlooked. Doing it would allow concurrent development in the agent class and more things would have been achieved.
#### Metadata
Currently metadata is set when the agent requests poa, this however is of course not correct. The metadata of the PoA should be stored within the principal since they are the owner of it. The agent should only be able to request a specific type of PoA from the principal which they know they have. This will be discussed further in the principal section.
### Principal
This class is probably the worst candidate when it comes to bad uses of inheritance and dependencies. The principal class itself is pretty much empty and the meat lays within the OAuth.py file. Ideally the OAuth class could become the Principal class and instead of having anonymous classes those classes should either be merged with the parent file or become seperate in some way. The inheritance used for OAuthServer should also be changed in some way, maybe with dependency injection.

The major problem that has arisen with this implementation is the fact that overriding constructors is impossible due to how inheritance works in Python. This has made it so that the principals id used to identify it within the key registry is not able to be set when the principal object has been created. This meant that we could not create a framework to support having multiple principals. We also wanted to create a way for principals to create a list of users that are allowed to access their PoAs, which leads into the second problem. In reality the principal would also store the different PoAs' or at least have some type of access to it, this way they could also define what users can access specifically.

One minor thing easily fixed is that currently the principal doesn't ask for the agents public via the key registry using the agents id sent in the /getPoa request

### Resource owner
#### Possible PoA registry
Currently the key registry is only just that and it leaves a bit of verification out of the picture. If this were to work in the real world there should also be another table in the database owned by the resource owner containing user ids and what poas' they are allowed to give out. So for example a row would contain the users id, application type of the poa and some other metadata about it. If the poa would give access to a download site the app type could be fileDownload and the metadata could specify what files they are allowed to download.

Another benefit with implementing this would be the ability to implement a UI for the agent where they could see a possible list of principals and what poas' they have. This would also remove the need for the principal to store poas themselves and instead hand over that responsibilty to the resource owner. Considering the resource owner most likely wants to verify that the principal actually has the right to delegate this power it seems logical that this is the way it should be implemented in practice.

Another point is that this could solve how principals specify what users are able to use their poa, maybe on the same row or in another table you could specify what users are able to use it. That way you could create an endpoint on the registry server allowing users (principals in this case) to add other users to the accepted list. This part however is just some speculation and no real thought has been put into how it could be solved exactly. 

#### Verifying metadata
The previous section goes hand in hand with this. Currently the implementation doesn't verify or look at any type of metadata, all it does is verify that the public keys that are in the poa exist in the database. It should also make another check to see if the public keys and the user id of said party belong to eachother which does not happen now. How it should be implemented can be discussed but maybe after verifying both parties it could take the app type and metadata of the poa and see if those belong to the principal in the aformentioned poa registry. 

#### Further issues
Another issue is of course the use of inheritance here exactly like the principal, so if it could be fixed in a similar manner that would be perfect.
## Reflection
Our problems stem from a lack of understanding of the core concepts the system wanted to, bad groundwork and pre-project planning is also an attributing factor. More than that another factor would be bad communication between project members which ulimately led to things not being understood well enough.

Overall the largest problem the project is facing is structure of code and use of inheritance etc. This is most likely the most important but tax-heaviest work to begin with if further development is to be done. A complete rewrite of the server classes could be needed which may take a long time. The other problems/missed implementations require less of a workload according to our estimate

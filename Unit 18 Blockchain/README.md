# Proof of Authority Blockchain
## This README file provides detailed guide on how to create of Proof of Authority Blockchain
1. Generate two new nodes with new account addresses that will serve as our pre-approved sealer addresses. 
Create accounts for two nodes for the network with a separate datadir for each using geth.
    - "./geth --datadir node1 account new"
    - "./geth --datadir node2 account new"
2. Generate genesis block via "./puppeth" and proceed with next few steps to complete configuration
    - input a network name
    - choose Clique
    - copy and paste both addresses
    - repeat copy and paste same addresses
    - choose a network ID
    - choose no
    - export configuration
 
 <img src="./Capture.png" />

3. Initializing nodes by entering following commands
    - ./geth --datadir node1 init homework.json
    - ./geth --datadir node2 init homework.json
4. Begin mining process by entering following commands in separate terminals since 2 nodes are created to test mining procedure
    - ./geth --datadir node1 --unlock "SEALER_ONE_ADDRESS" --mine --rpc --allow-insecure-unlock
    - ./geth --datadir node2 --unlock"SEALER_TWO_ADDRESS" --mine --port 30304 --bootnodes "enode://SEALER_ONE_ENODE_ADDRESS@127.0.01:30303" --ipcdisable --allow-insecure-unlock
5. Add blockchain to MyCrypto and initiate test transaction. This is done by 'add custom node' via change network, input the information setup during the genesis creation
- enter "http://127.0.0.1:8545" for URL as to identify local host
<img src="./Capture2.png" />
<img src="./Capture3.png" />
6. Finally, go to keystore file and navigate to the node1 directory to unlock and access wallet. Respectively go to the second node address to test whether the blockchain network is fully functional. 
<img src="./Capture4.png" />
<img src="./Capture5.png" />


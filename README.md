# Data Pipeline with Red Panda and the ECS Standard
Multi-Purpose Distributed Network: We hypothesize that this network of nodes/endpoints will function effectively as a dragnet. 🌐
Node Utilization: Each host and server on the network acts as a node that employs the data-hoover to ingest data, transform it into ECS format, and subsequently store it in the appropriate database tables. 💾

**High Processing Bandwidth:** Leveraging the capabilities of Kafka/Red Panda to achieve high processing bandwidth across the network. ⚡

**ECS Standard Schemas:** Schemas are based on the ECS Standard for use within the ELK Stack. A low-resource Docker version is available here. 🐳

### Composition
Producer: Continuously extracts data and structures it for passing to the transformer. 🛠️
Loader: Loads transformed data into the designated storage systems. 📥
Transformer: Ensures that the ingested data is converted into the ECS format and prepares it for loading into the storage systems. 🔄


### To Be Done
- Implement the ML Analysis Pipeline: Focus on clustering (Clustering ✅). 🤖
- Node Weighting: Consider methodologies for weighting nodes. ⚖️
- MITRE ATT&CK Matrices: Store the matrices in a key-value store for quick access. 📊
- Formal Data Modelling ie. How are we going to leverage SQL, NOSQL, Vector and Graph Databases while maintaining the ability for the data to flow smoothly and be used by all entities.
- Graph Metadata: Learn how to add metadata to the nodes of a graph to implement the graph of graphs for further insight. 🧩
- Smart Contracts: Understand smart contracts to integrate the reward system. 📜
- Continuous Learning Practices: Investigate practices so that users, along with humans in the loop, can provide feedback (rewards) to an offline reinforcement learning tool, contributing to the retraining of models in the higher-order analysis pipeline. 🧠
Contributing

We plead insanity in this solution as always. This is very early in the project.


#### Contact:
core@oriondefensiveai.com
www.oriondefensiveai.com


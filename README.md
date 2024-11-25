Key Tech

- Python
- Java
- Hadoop
- HiveQL
- HBase
- Shell
- Spark

Project Steps 

1. Set Up Environment 

   - Install Hadoop and configure HDFS using the provided tutorials. ✅
   - Install HBase on top of Hadoop. ✅
   - Set up Zookeeper for distributed coordination. ✅

2. Data Preprocessing 

   - Download NYC Taxi datasets. 
   - Clean and preprocess the data for ingestion. 
   - Structure the data to match HBase's column family model (e.g., trip details, fare details). 

3. Data Ingestion 

   - Use HBase Shell or Java API to define tables and column families. 
   - Import the dataset into HBase using MapReduce or Apache Spark for scalability. 

4. Query Implementation 

   - Design queries for real-time data access: 
     - Total trips by date. 
     - Average fare per trip. 
     - Trips within a specific geographical boundary. 

5. Performance Testing 

   - Simulate multiple concurrent queries. 
   - Measure response time and throughput. 
   - Test region splitting and load balancing. 

6. Visualization 

   - Use tools like Grafana or Kibana to visualize HBase metrics. 
   - Plot query results using Python (e.g., Matplotlib, Seaborn). 

Deliverables 

1. HBase cluster with NYC Taxi dataset loaded. 

2. Documentation of the ingestion and query process. 

3. Visualizations showcasing insights derived from the dataset. 

4. Performance report detailing query execution time, load balancing, and scalability. 

Evaluation Criteria 

- Correctness: Does the HBase setup handle large-scale data ingestion and querying effectively? 

- Scalability: Can the system scale under increased load? 

- Insights: Are meaningful insights extracted from the dataset? 

- Documentation: Is the process clearly documented? 
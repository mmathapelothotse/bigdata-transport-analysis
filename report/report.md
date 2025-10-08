# Big Data Analytics on NYC Taxi Transportation Data
### Part 2: MapReduce & Visualisation Analysis  
- **Student Name:** Mmathapelo Thotse  
- **Student Number:** u22888676 
- **Course:** MIT805 - Big Data Analytics 
- **Date:** 08 October 2025

---

## Table of Contents
- Introduction  
- Hadoop Overview and Setup  
- Visualisations and Their Value  
- Conclusion  
- References  
- Appendix

---

## 1. Introduction

Traditional data processing techniques are no longer adequate due to the exponential growth in data in the transportation sector.  The second stage of a Big Data project that uses **Hadoop MapReduce** and **data visualisation** tools to analyse the **New York City Yellow Taxi Trip dataset** is presented in this article.  The objective is to derive practical insights that can guide business choices about transportation planning and urban mobility.

### 1.1 Background and Context

NYC’s taxi system generates millions of trip records daily. Analysing this data requires Big Data technologies like MapReduce, which splits tasks into:
- **Map phase**: filtering and transformation
- **Reduce phase**: aggregation and summarization

### 1.2 Project Objectives

- Implement MapReduce algorithms
- Process large-scale taxi data
- Create meaningful visualisations
- Apply Big Data concepts
- Extract business value


## 2. Hadoop Overview and Setup

### 2.1 What is Hadoop?

**Apache Hadoop** is an open-source framework designed for the distributed storage and processing of large datasets across clusters of computers. It follows the **MapReduce programming model**, which splits tasks into two main phases:

- **Map Phase:** Processes and filters input data into key-value pairs.
- **Reduce Phase:** Aggregates and summarises the mapped data.

Hadoop is highly scalable and fault-tolerant, making it ideal for handling **Volume**, **Velocity**, and **Variety**—three of the core Vs of Big Data.

### 2.2 Local Hadoop Setup
To simulate a distributed environment locally, I set up a **single-node Hadoop cluster** on my machine using the following steps:

1. Installed Java (required for Hadoop runtime).
2. Downloaded and configured `hadoop-3.4.2.tar`.
3. Set environment variables (`HADOOP_HOME`, `JAVA_HOME`, etc.).
4. Formatted the HDFS namenode and started the Hadoop daemons

```bash
start-dfs.sh
start-yarn.sh
```
5. Created HDFS directories and uploaded the dataset
```bash
hdfs dfs -mkdir -p /user/mmathepelothotse/nyc_transport_csv
hdfs dfs -put yellow_taxi_combined.csv /user/mmathepelothotse/nyc_transport_csv/
```
This setup enabled me to run Python-based MapReduce jobs using Hadoop Streaming.

## 3. Visualisations and Their Value

After processing the dataset using MapReduce, I created three key visualisations to effectively communicate the insights.

### 3.1 Hourly Demand Distribution
**Visualisation:** Bar chart showing the number of trips per hour.

**Insight:**
- Clear morning peak (7–9 AM) and evening peak (5–7 PM).
- Low activity between 2–5 AM.

**Business Value:**
- Helps optimise driver allocation during peak hours.
- Supports dynamic pricing strategies to maximise revenue.

## 3.2 Tipping Behaviour Heatmap
**Visualisation:** Grouped bar chart showing average tip percentage by payment type and trip distance category (short, medium, long).

**Insight:**
- Credit card payments yield higher tips than cash.
- Medium-distance trips have the highest tip-to-fare ratio.

**Business Value:**
- Encourages cashless payments to boost driver earnings.
- Informs driver training and customer engagement strategies.

## 3.3 Route Profitability Dashboard
**Visualisation:** Interactive dashboard (Plotly) showing:

Top 100 profitable routes
Revenue per mile
Total revenue per route

**Insight:**
- Routes to/from airports and business districts are most profitable.
- Some short-distance routes yield high revenue per mile.

**Business Value:**
- Enables strategic driver positioning.
- Supports route-based pricing models and fleet optimisation.

## 4. Conclusion
This phase of the project demonstrated the power of Hadoop MapReduce in processing large-scale transportation data. The visualisations provided clear, actionable insights that can help:

- Improve operational efficiency
- Enhance customer satisfaction
- Maximise revenue through data-driven strategies

The combination of distributed processing and effective visualisation bridges the gap between raw data and business intelligence.

---

## References

1. [NYC Open Data – TLC Trip Records](https://opendata.cityofnewyork.us/)
2. Dean & Ghemawat (2004) – MapReduce
3. White (2015) – *Hadoop: The Definitive Guide*
4. [Apache Hadoop Documentation](https://hadoop.apache.org/)
5. McKinney (2017) – *Python for Data Analysis*

---

## Appendix

### A. GitHub Repository
`https://github.com/mmathapelothotse/bigdata-transport-analysis`

### B. Video Demonstration
`https://[your-video-platform]/[video-id]`


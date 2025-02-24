#Weather Forecaster

A simple project of kafka and python to demonstrate basic concepts of producer, consumer and topic

## Table of Contents

- [Installation](#installation)
- [Main idea of the project](#usage)
- [How to run the project](#contributing)

## Installation

To run this project, you need to have the JDK of java and following Python packages installed:

<ul>
  <li>matplotlib</li>
  <li>kafka-python</li>
</ul>

You can install these packages using pip:

<pre>
pip install matplotlib kafka-python
</pre>

## Usage

<ol>
  <li><strong>Producer</strong><br>
    It generates random weather data , including weatherstate , temperature and humidity.It sends this data as messages to kafka.
  </li>
  <li><strong>Topic</strong><br>
    This is where the weather data gets snt.It receives weather data messages from the producer and makes them available for consumers.
  </li>
  <li><strong>Consumer</strong><br>
    It fetches data from kafka topic and displays them in a real-time graph or chart.
  </li>
</ol>



## How to run the project

Steps to run the project:

<ol>
  <li><strong>Install kafka</strong><br>
    Extract the folder and copy the folder at any place ( here in D Partition)
    Go to kakafolder \config\server.properties.
    Edit log.dirs=D:/kafkafoldername/kafka-logs.
    Go to kafkafoldername\config\zookeeper.properties
    Edit dataDir=D:/kafkafoldername/zookeeper-data
    
  </li>
  <li><strong>Start zookeeper server</strong><br>
    Go to kafkafoldername\bin\windows and Open command propmpt and write "D:\kafka_2.12-3.7.0\bin\windows\zookeeper-server-start.bat D:\kafka_2.12-3.7.0\config\zookeeper.properties"
    Don't close the cmd window
  </li>
  <li><strong>Start kafka server in another new CMD window at the same previous path</strong><br>
    Write "D:\kafka_2.12-3.7.0\bin\windows\kafka-server-start.bat D:\kafka_2.12-3.7.0\config\server.properties"
    Don't close this CMD window
  </li>
  <li><strong>Create a kafka topic in  another new CMD window at the same previous path</strong><br>
    Write "kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic weather_forecasts"
    Don't close this CMD window
  </li>
    <li><strong>Create a kafka producer in the same previous CMD window at the same previous path</strong><br>
    Write "kafka-console-producer.bat --broker-list localhost:9092 --topic weather_forecasts"
    Don't close this CMD window
  </li>
      <li><strong>Create a kafka consumer in another new CMD window at the same previous path</strong><br>
    Write "kafka-console-consumer.bat --topic weather_forecasts --bootstrap-server localhost:9092 --from-beginning    D:\kafka_2.12-3.7.0\data\kafka"
    Don't close this CMD window
  </li>
   
      <li><strong>GO To visual studio code and run producer.py</strong><br>

  </li>
  <li><strong>GO To visual studio code and run consumer.py in another terminal</strong><br>

  </li>
</ol>

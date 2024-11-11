# KAFKA-PYTHON BASICS SCRIPT
This is the ```KAFKA-PYTHON BASICS``` script. This service is made using python and kakfa and is used to have a basic understading of how python & kafka can work together via docker.

## Getting Started
 **Steps to get started**

 *** Making it work locally ***
 

* Availability of docker 
 ```
 - Make sure docker is installed on your system.
 - Please refer to - https://docs.docker.com/engine/install/ to install docker
 ```

* Clone the repository 
 ```
 git clone https://github.com/amulyasharma27797/kafka-python.git
 ```

* Enter the main directory
 ```
 cd kafka-python
 ```

* To run the project normally
 ```
 docker-compose up --build
 ```

* To stop the project normally
 ```
 docker-compose down
 ``` 

* Running Kafka via UI
 ```
 - Open localhost:8080
 - Add a topic say "registered_user", in this case with single partition
 - Create a consumer group say "consumer-group-a", in this case with single parition
 ``` 
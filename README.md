# IndoorFarming_IoT
Smart farming has taken a leap from traditional farming as
it brings reliability and predictability at our  ngertips. Automation and
cloud software systems are tools for smart farming. Smart farming emphasises
on acquiring data collected by sensors and make productive use
of it. Smart farming employs hardware (IoT) and software (SaaS) to
capture the data and give actionable insights to manage all the operations
on the farm. The data is organized, accessible all the time that can
be monitored remotely and allows us to take necessary actions. Smart
farming analyses soil moisture content, indoor room temperature and
humidity and light intensity to get knowledge about suitable crops and
water requirements for optimization. In this project, di erent sensors are
used to detect real-time physical conditions like temperature, humidity,
light intensity and soil moisture content and send the data to Raspberry
Pi. Then, the data will be processed by Raspberry Pi and uploaded to
the Cloud. Furthermore, the system will automatically maintain ambient
conditions by modulating HVAC devices, indoor lighting and water
pumps to save energy. The web-based application aims to graphically
represent the gathered data to provide better understanding of the facility.
With the help of indoor farming using HVAC and IoT, productivity
and quality of crops are expected to increase signi cantly. Additionally,
reduction of carbon footprints is also achieved.

# Block Diagram
![image](https://user-images.githubusercontent.com/128833366/235347360-4ab35da7-7953-40d8-9202-ee275cad5560.png)

# System Architecture Design
The system architecture consists of Raspberry Pi, sensors like humidity, temper-
ature, soil moisture, light intensity sensor and actuators like automatic lighting
system to turn on/o  or to maintain the light intensity, HVAC devices that de-
liver the heat, cooling, air  ltration, and water pump.
The model is divided into Four layers: User Layer, Reasoning Layer, Ubiqui-
tous Layer, Physical Layer. The  rst layer is the physical layer, which describes
the system's hardware, software, and network environment. The perception layer
is the physical layer, which has sensors for sensing and gathering information
about the environment and actuators which enables actions to be taken in the
environment interfaced to the Raspberry Pi. MQTT protocol is used for the
sensors to send data to Raspberry Pi's mosquitto MQTT Broker, which client
devices can then receive that data. In the Reasoning/Ubiquitous layer, AI plan-
ner is implemented which gives a sequence of action depending on the outcome
of the planner, the data is published back to the raspberry Pi for the actuation.
The user layer consists of Graphical User Interface (GUI) which provides insight
real-time data like temperature, light intensity, soil moisture and humidity.


![image](https://user-images.githubusercontent.com/128833366/235347345-506d8f72-4012-4657-8281-dd09d5ad15ff.png)


# Frontend
![image](https://user-images.githubusercontent.com/128833366/235347461-e790a8b9-58c8-4a05-8aae-42d79b2838e5.png)
![image](https://user-images.githubusercontent.com/128833366/235347482-436cc834-77a6-49b9-86e7-7f4df7553360.png)

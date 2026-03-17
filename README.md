# Rock Paper Scissors Predictor AI

RPS predictor entirely build by Mayura Jayasinghe.

I used following boilerplate for the Rock Paper Scissors project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors

NOTE: I used docker to efficiently manage following python ML libaries.Also this help me to learn how docker works.so i can use docker for complex projects that docker is not an option, but necessity.For simplicity reasons sometimes i run code without docker.So u can completely ignore the docker part because following libraries work lot of time without isolation.

Tensorflow - ML libray to train the model
Pandas - for data collection and for prapare data

datacollector.py - implemented to collect data from apponent bots


# Docker Notes //still learning and not sure

---initial Docker commands to build using Dockerfile and run. if u run this again image only updates according to updates done to Dockerfile.

docker build -t rps-ml-model .           

---force rebuild again from the begining using Dockfile.

docker build --no-cache -t rps-ml-model .

---Docker Command to run with updated version of the project files.

docker run -it -v $(pwd):/app rps-ml-model

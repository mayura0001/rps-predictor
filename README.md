# Rock Paper Scissors

RPS predictor entirely build by Mayura Jayasinghe.

I used following boilerplate for the Rock Paper Scissors project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors

use docker to efficiently manage following python ML libaries.also this help me to learn how docker works.so i can use docker for complex projects that docker is not an option, but necessity.
-Tensorflow
-numpy

# initial Docker commands to build using Dockerfile and run
docker build -t rps-ml-model                                      
docker run -it rps-ml-model

# Docker Command to run with updated version of the project files
docker run -it -v $(pwd):/app rps-ml-model

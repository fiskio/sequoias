[![Build Status](https://travis-ci.com/TouchType/CiNeTeKa.svg?token=Kvb7CTuEDkyy7jzfc8sA&branch=master)](https://travis-ci.org/fiskio/sequoias)

# Sequoias
A Sequence-2-Sequence framework in CNTK

## Setup Docker

To setup the Docker image please run `dockers/build CPU` or `dockers/build GPU`. Using a GPU is strongly recomended, in this case make sure you also have [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) installed.  
To run any command within the docker image, just prepend `dockers/run` to it.  
To check that the install has been successful run: `dockers/run nosetests -s sequoias.tests.test_foo`

## Setup

If you prefer not to use Docker it is still recommended that you use a conda virtual environment.  
To install CNTK follow these [instructions](https://docs.microsoft.com/en-us/cognitive-toolkit/Setup-CNTK-on-your-machine) and use the *Python-only installation*.
To install the remaining dependencies: `pip install -r requirements.txt`.

## Testing
To run all the test use: `nosetests -s`  
To check the coding style use: `flake8`  

# Sequoias
A Sequence-2-Sequence framework in CNTK

## Setup

If you prefer not to use Docker it is still reccomended that you use a virtual environment.
To install CNTK follow these [instructions](https://docs.microsoft.com/en-us/cognitive-toolkit/Setup-CNTK-on-your-machine) and use the *Python-only installation*.  
To install the remaining python dependencies run: `pip install -r requirements.txt`.

## Setup Docker

To setup the Docker image please run `dockers/build CPU` or `dockers/build GPU`. Using a GPU is strongly recomended, in this case make sure you also have [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) installed.

To run any command within the docker image, just prepend `dockers/run` to it.

## Testing
To run all the test use: `nosetests -s`  
To check the coding style use: `flake8`  
To check that the install has been successful run: `dockers/run nosetests -s sequoias.tests.test_foo`

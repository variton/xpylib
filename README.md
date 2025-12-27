# Xpylib - x python library 
High level cross platform python packages.
This bundle of packages is intended to be used for 
tools, software components & scripts.

## Clone repository
*remark:*
    *make sure your ssh key was added to you github account*

```
git clone git@github.com:variton/xpylib.git 

```

## Environment to develop the xpylib 
*remark:*
    *make sure you have the rights to pull the docker image*

```
docker pull ghcr.io/variton/ixpylib:1.0

```

### Set the python path
Set up the following environment variable.
Once you've cd in the root project's directory:

```
export PYTHONPATH=src/$PWD

```

### Run all the tests
*remark:*
    *make sure to use the ixpylib docker image*

Execute the following cli:

```
pytest tests

```

### Generate the test report
*remark:*
    *make sure to use the ixpylib docker image*

Execute the following cli:

```
pytest --html=report.html --self-contained-html

```
This will generate a report.html file in the root folder


### Run the test coverage on a module
*remark:*
    *make sure to use the ixpylib docker image*

Execute the following cli:

```
coverage run -m pytest tests/<target>

```

### Run the local CI
*remark:*
    *make sure to use the ixpylib docker image*
    *execute the ci.sh script before committing*

Execute the following cli:

```
./local-ci.sh

```

### Generate the documentation
*remark:*
    *make sure to use the ixpylib docker image*

Execute the following cli:

```
todo
this will use sphinx

```

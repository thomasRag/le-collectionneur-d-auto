# Le collectionneur d'Auto
RESTFul api sample service using Python Flask micro-framework

## Requirement
python 3, pip, virtualenv

## Install instructions

  - install python 3
  - Create a virtualenv with command : 
  ``virtualenv -p python3 env``
   - activate it : ``source env/bin/activate``
   - run the app: ``python api.py``

## Unit tests

run the unit tests : 
    ``python -m unittest tests/units/*.py``
   
## Usage Example

   - post a new car: 
   
   ``curl -H "Content-Type: application/json" -X POST -d '{"description":"Cadillac 355 D Series 30 (Flat Windshield)","make":"Cadillac","displacement":353.5,"year":1934,"owner":"John Smith","media":"https://en.wikipedia.org/wiki/Cadillac_Series_355#/media/File:1934_Cadillac_355D_-_fvr_(4608933837).jpg"}' http://127.0.0.1:5000/cars``
   
   - get all cars:
   
   ``curl http://127.0.0.1:5000/cars``
   
   - get one cars:
   
   ``curl http://127.0.0.1:5000/cars/1``
   
    - etc.
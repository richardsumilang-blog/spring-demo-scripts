#!/bin/bash

pushit(){
  ab=$1
  scale=$2
  echo $ab
  app=ab-$ab
  cf a | grep $app && cf d -f $app
  cf push --no-route --no-start -p ab.jar $app
  cf set-env $app AB $ab
  cf start $app
  cf scale $app -i $scale
  cf map-route $app cfapps.io -n ab
}

pushit a 3
pushit b 1
python ab.py

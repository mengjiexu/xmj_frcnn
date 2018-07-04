#!/bin/bash
rm -rf data/cache 
./experiments/scripts/train_faster_rcnn.sh 0 pascal_voc vgg16

#!/bin/bash
#The size must be displayed in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

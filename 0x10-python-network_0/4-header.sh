#!/bin/bash
#A header variable X-HolbertonSchool-User-Id must be sent with the value 98
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"

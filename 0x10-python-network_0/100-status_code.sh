#!/bin/bash
# Script that get status code from url
curl -s -o /dev/null -w "%{http_code}" "$1"

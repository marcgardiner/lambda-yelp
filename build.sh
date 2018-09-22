#!/usr/bin/env bash
ZIP_PATH=""

usage()
{
cat << EOF
usage: $0 options

This script builds AWS Lambda function package

OPTIONS:
   -p      path to function package zip file
   -v      Verbose
EOF
}

while getopts “p:” OPTION;do
     case $OPTION in
         u)
             usage
             exit 1
             ;;
         p)
             ZIP_PATH=$OPTARG
             ;;
         v)
             VERBOSE=1
             ;;
         ?)
             usage
             exit
             ;;
     esac
done

if [ "$ZIP_PATH" == "" ]; then
    echo "Please input project path..."
    echo "Aborting ..."
    exit 1
fi

cd $ZIP_PATH

virtualenv --python=python3.6 "$ZIP_PATH/dist/venv"
source $ZIP_PATH/dist/venv/bin/activate

pip install -r $ZIP_PATH/src/requirements.txt

cd $ZIP_PATH/src

zip -r $ZIP_PATH/lambda-yelp.zip ./*

cd ..

cd $VIRTUAL_ENV/lib/python3.6/site-packages

zip -r9 $ZIP_PATH/lambda-yelp.zip *

cd $VIRTUAL_ENV/lib/python3.6/site-packages

zip -r9 $ZIP_PATH/lambda-yelp.zip *
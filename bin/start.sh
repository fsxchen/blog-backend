#!/bin/sh

CUR_DIR=`pwd`
HOME=`pwd`
CONF_DIR=${HOME}/etc
uwsgi --ini ${CONF_DIR}/uwsgi.ini

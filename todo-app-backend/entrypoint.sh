#!/bin/sh
##########################################
# Author: Ifeoluwa                       #
# Company: Xapic Technologies            #
# Usage: Entrypoint for todo-app-backend #
##########################################
# Create database table
flask create_db

# Run flask app
flask run
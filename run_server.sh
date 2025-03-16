#!/bin/bash

# Set the Flask application
export FLASK_APP=serve.py

while true; do
    # Run Flask and pipe output to both console and log file
    flask run 2>&1 | tee -a server.log

    echo "$(date) - Flask server stopped. Waiting 10 minutes before restart..." | tee -a server.log
    
    # Sleep for 10 minutes
    sleep 600
done 
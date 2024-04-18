#!/bin/bash

# Infinite loop
while true
do
    # Start the node script in the background
    node main.js &
    
    # Get the PID of the last background process
    PID=$!
    
    # Wait for 60 seconds
    sleep 30
    
    # Send SIGINT to the node process to gracefully exit
    kill -2 $PID
    
    # Optional: Wait a bit before restarting
    sleep 1
done
#!/usr/bin/env python3
# Author ID: 101775229

import subprocess

def free_space():
    
    command = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    output, error = process.communicate()
    free_space_str = output.decode('utf-8').strip()

    return free_space_str

if __name__ == "__main__":
    print(free_space())


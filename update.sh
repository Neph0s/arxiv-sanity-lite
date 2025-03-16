#!/bin/bash

cd /home/ec2-user/arxiv-sanity-lite/

/home/ec2-user/anaconda3/envs/sanity/bin/python arxiv_daemon.py --num 3000

if [ $? -eq 0 ]; then
    echo "$(date) - 检测到新论文，运行 compute.py" >> /home/ec2-user/arxiv-sanity-lite/cron.log
    /home/ec2-user/anaconda3/envs/sanity/bin/python compute.py >> /home/ec2-user/arxiv-sanity-lite/cron.log 2>&1
    echo "Finish compute.py
else
    echo "No new papers were added, skipping feature computation"
fi
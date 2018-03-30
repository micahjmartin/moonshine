#!/bin/bash
# Install shine for SSH

cp -rv shine /usr/lib/python3/dist-packages/
cp -v moonshine.py /usr/bin/moonshine
chmod 755 /usr/bin/moonshine
echo "ForceCommand /usr/bin/moonshine" >> /etc/ssh/sshd_config

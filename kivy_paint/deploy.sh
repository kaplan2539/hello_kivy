#!/bin/bash

time docker run --privileged -v /dev/bus/usb:/dev/bus/usb -v $PWD:/home/user/hostcwd -v $PWD/../_buildozer_cache:/home/user/.buildozer --rm -it kivy/buildozer android deploy

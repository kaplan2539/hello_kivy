#!/bin/bash

time docker run -v $PWD:/home/user/hostcwd -v $PWD/../_buildozer_cache:/home/user/.buildozer --rm -it kivy/buildozer android debug

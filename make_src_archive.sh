#!/bin/sh
#
# Creates a tar.gz-archive adept-1.0-cmake in the parent directory.

git archive --prefix=adept-1.0-cmake/ -o ../adept-1.0-cmake.tar.gz HEAD
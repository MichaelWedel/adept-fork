cmake_minimum_required(VERSION 2.8)
project(ADEPT)

include_directories(${ADEPT_SOURCE_DIR}/include)
add_library(adept ${ADEPT_SOURCE_DIR}/src/adept.cpp)
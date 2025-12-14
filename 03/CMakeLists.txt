cmake_minimum_required(VERSION 4.0)
project(03)

set(CMAKE_CXX_STANDARD 23)

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/input.txt
        ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)

add_executable(03
        main.cpp)

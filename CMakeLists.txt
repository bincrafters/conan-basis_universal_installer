cmake_minimum_required(VERSION 2.8.12)
project(cmake_wrapper)

set(CMAKE_VERBOSE_MAKEFILE ON)

message(STATUS "Conan CMake Wrapper")
include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
conan_basic_setup()

add_subdirectory("source_subfolder")

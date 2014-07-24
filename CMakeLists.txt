cmake_minimum_required ( VERSION 2.8.0 )

project ( Adept )

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/Modules/")

if ( NOT INSTALL_LIB_DIR )
    set ( INSTALL_LIB_DIR "lib" )
endif()

set ( CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin )
set ( CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib )
set ( CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib )

link_directories ( ${CMAKE_ARCHIVE_OUTPUT_DIRECTORY} ${CMAKE_LIBRARY_OUTPUT_DIRECTORY} )

# Building the actual library
include_directories ( ${CMAKE_SOURCE_DIR}/library/include )
add_subdirectory ( library )

# Building the tests supplied with the adept library
add_subdirectory( test EXCLUDE_FROM_ALL )

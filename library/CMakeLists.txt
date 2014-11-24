add_definitions(-DADEPT_DLL)
add_definitions(-DADEPT_STACK_THREAD_UNSAFE)
add_definitions(-DADEPT_RECORDING_PAUSABLE)
add_definitions(-DADEPT_MULTIPASS_SIZE=2)

add_library(adept SHARED ${CMAKE_CURRENT_SOURCE_DIR}/src/adept.cpp ${CMAKE_CURRENT_SOURCE_DIR}/include/adept.h)
SET_TARGET_PROPERTIES( adept PROPERTIES VERSION 1 )

install ( FILES ${CMAKE_CURRENT_SOURCE_DIR}/include/adept.h DESTINATION include )

if ( ${CMAKE_SYSTEM_NAME} MATCHES "Windows" )
    install ( FILES ${CMAKE_CURRENT_SOURCE_DIR}/cmake/Modules/Findadept.cmake DESTINATION  cmake/Modules )
ELSE()
    install ( FILES ${CMAKE_CURRENT_SOURCE_DIR}/cmake/Modules/Findadept.cmake DESTINATION  share/adept/cmake/Modules )
ENDIF()

install ( TARGETS adept DESTINATION ${INSTALL_LIB_DIR} )

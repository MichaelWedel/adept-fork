add_definitions(-DADEPT_DLL)
add_definitions(-DADEPT_STACK_THREAD_UNSAFE)
add_definitions(-DADEPT_RECORDING_PAUSABLE)

add_library(adept SHARED ${CMAKE_CURRENT_SOURCE_DIR}/src/adept.cpp)

install ( FILES ${CMAKE_CURRENT_SOURCE_DIR}/include/adept.h DESTINATION include )

IF(WIN32)
    install ( FILES ${CMAKE_CURRENT_SOURCE_DIR}/cmake/Modules/Findadept.cmake DESTINATION  ${CMAKE_BINARY_DIR}/cmake/Modules )
ELSE()
    install ( FILES ${CMAKE_CURRENT_SOURCE_DIR}/cmake/Modules/Findadept.cmake DESTINATION  share/adept/cmake/Modules )
ENDIF()

install ( TARGETS adept DESTINATION lib )

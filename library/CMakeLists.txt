add_definitions(-DADEPT_DLL)
add_definitions(-DADEPT_STACK_THREAD_UNSAFE)
add_definitions(-DADEPT_RECORDING_PAUSABLE)

add_library(adept SHARED ${CMAKE_CURRENT_SOURCE_DIR}/src/adept.cpp)

install ( FILES ${CMAKE_CURRENT_SOURCE_DIR}/include/adept.h DESTINATION include )
install ( TARGETS adept DESTINATION lib )
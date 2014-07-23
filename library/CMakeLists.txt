include_directories(${ADEPT_SOURCE_DIR}/library/include)
add_definitions(-DADEPT_DLL)
add_definitions(-DADEPT_STACK_THREAD_UNSAFE)
add_library(adept SHARED ${ADEPT_SOURCE_DIR}/library/src/adept.cpp)
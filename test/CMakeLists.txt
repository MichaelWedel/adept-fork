set ( LIBS ${LIBS} adept )

set ( SRC_FILES
	algorithm.cpp
	rosenbrock_banana_function.cpp
	simulate_radiances.cpp
	state.cpp
	test_adept.cpp
	test_adept_with_and_without_ad.cpp
	test_gsl_interface.cpp
	test_radiances.cpp
)

# Test program 1
add_executable ( test_adept algorithm.cpp test_adept.cpp )
target_link_libraries ( test_adept ${LIBS} )

# Test program 3
add_executable ( test_radiances test_radiances.cpp simulate_radiances.cpp )
target_link_libraries ( test_radiances ${LIBS} )

if ( ${CMAKE_SYSTEM_NAME} MATCHES "Linux" )
	find_package ( GSL REQUIRED )
	include_directories(${GSL_INCLUDE_DIR})

	set(LIBS ${LIBS} ${GSL_LIBRARIES})

	# Test program 4
	add_executable ( test_gsl_interface rosenbrock_banana_function.cpp state.cpp test_gsl_interface.cpp )
	target_link_libraries ( test_gsl_interface ${LIBS} )
endif()
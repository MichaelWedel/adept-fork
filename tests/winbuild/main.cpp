#include "adept.h"
#include <iostream>

namespace adept {
	//extern Stack * _stack_current_thread; 
}

int main( int argc, const char* argv[] )
{
  adept::Stack adeptStack;

  adept::adouble f = 10.0;
  adept::adouble x = 2.0;

  adeptStack.new_recording();
  
  adept::adouble y = f * pow(x, 2.0);
  
  y.set_gradient(1.0);
  adeptStack.compute_adjoint();
  
  std::cout << "dy/df = " << f.get_gradient() << std::endl;
  std::cout << "dy/dx = " << x.get_gradient() << std::endl;

  return 0;
}
Name:           adept
Version:        1.0
Release:     	1%{?dist}
Summary:        Automatic differentiation library

Group:          Development/Libraries
License:        GPLv3
URL:            http://www.met.rdg.ac.uk/clouds/adept/
Source0:        adept-1.0-cmake.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)     

%description
adept is a library that implements automatic differentiation
using the operator overloading approach. It is written in C++.
More information can be found on the project website: 
http://www.met.rdg.ac.uk/clouds/adept/

This packaging script was written for a CMake-based fork,
which can be found here:
https://github.com/MichaelWedel/adept

%prep
%setup -n adept-1.0-cmake

%build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DINSTALL_LIB_DIR=lib64
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_includedir}/*.h
/usr/share/adept/cmake/Modules/*



%changelog
* Thu Jul 24 2014 Michael Wedel <Michael.Wedel@psi.ch> - 1.0-1
- Initial version of the package
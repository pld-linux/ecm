Summary:	The ECMNET Project
Name:		ecm
Version:	5.0.3
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://home.in.tum.de/~kruppa/%{name}-%{version}.tar.gz
# Source0-md5:	c2541748ece10c368b3d5672406fffbd
URL:		http://www.loria.fr/~zimmerma/ecmnet/
BuildRequires:	gmp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ECMNET Project

%prep
%setup -q

sed -i -e 's#CC=gcc#CC=%{__cc}#g' \
       -e 's#CXX=gcc#CXX=%{__cxx}#g' \
       -e 's#-static# #' \
       -e 's#CFLAGS=.*#CFLAGS=%{rpmcflags}#' \
       -e 's#GMP=.*#GMP=/usr#'  Makefile
       
%build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D ecm $RPM_BUILD_ROOT/%{_bindir}/ecm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*

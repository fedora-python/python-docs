%{!?__python_ver:%define __python_ver EMPTY}

%if "%{__python_ver}" != "EMPTY"
%define main_python 0
%define python python%{__python_ver}
%else
%define main_python 1
%define python python
%endif

%define pybasever 2.4

Summary: Documentation for the Python programming language.
Name: %{python}-docs
Version: %{pybasever}
Release: 102
License: PSF - see LICENSE
Group: Documentation
Source: http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2
BuildArch: noarch

Patch4: python-2.3-nowhatsnew.patch
Patch17: python-2.4-tex-fix.patch

Requires: %{python} = %{version}
%if %{main_python}
Obsoletes: python2-docs
Provides: python2-docs = %{version}
%endif

BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildPrereq: tetex-latex, %{python}, latex2html
URL: http://www.python.org/

%description
The python-docs package contains documentation on the Python
programming language and interpreter.  The documentation is provided
in ASCII text files and in LaTeX source files.

Install the python-docs package if you'd like to use the documentation
for the Python language.

%prep
%setup -q -n Python-%{version}

%patch4 -p1 -b .nowhatsnew
%patch17 -p1 -b .tex-fix

%build
topdir=`pwd`

pushd Doc
python_bin=$(which %{python})
make PYTHON=$python_bin
rm html/index.html.in Makefile* info/Makefile tools/sgmlconv/Makefile
popd

%install
[ -d $RPM_BUILD_ROOT ] && rm -fr $RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc Misc/NEWS  Misc/README Misc/cheatsheet 
%doc Misc/HISTORY Doc/html

%changelog
* Thu Mar 17 2005 Mihai Ibanescu <misa@redhat.com> 2.4-102
- changed package to noarch

* Mon Mar 14 2005 Mihai Ibanescu <misa@redhat.com> 2.4-100
- split the doc building step into a separate source rpm

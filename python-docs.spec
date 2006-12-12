%{!?__python_ver:%define __python_ver EMPTY}

%if "%{__python_ver}" != "EMPTY"
%define main_python 0
%define python python%{__python_ver}
%else
%define main_python 1
%define python python
%endif

%define pybasever 2.5

Summary: Documentation for the Python programming language.
Name: %{python}-docs
Version: %{pybasever}
Release: 1%{?dist}
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
* Tue Dec 12 2006 Jeremy Katz <katzj@redhat.com> - 2.5-1
- update to 2.5

* Tue Oct 24 2006 Jeremy Katz <katzj@redhat.com> - 2.4.4-1
- update to 2.4.4

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.4.3-1.1
- rebuild

* Sat Apr  8 2006 Mihai Ibanescu <misa@redhat.com> 2.4.3-1
- updated to 2.4.3

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 16 2005 Mihai Ibanescu <misa@redhat.com> 2.4.2-1
- updated to 2.4.2

* Fri Apr  8 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-1
- updated to 2.4.1

* Thu Mar 17 2005 Mihai Ibanescu <misa@redhat.com> 2.4-102
- changed package to noarch

* Mon Mar 14 2005 Mihai Ibanescu <misa@redhat.com> 2.4-100
- split the doc building step into a separate source rpm

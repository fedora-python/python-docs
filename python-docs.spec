%{!?__python_ver:%define __python_ver EMPTY}

%if "%{__python_ver}" != "EMPTY"
%define main_python 0
%define python python%{__python_ver}
%else
%define main_python 1
%define python python
%endif

%define pybasever 2.6

Summary: Documentation for the Python programming language
Name: %{python}-docs
Version: %{pybasever}.2
Release: 1%{?dist}
License: Python
Group: Documentation
Source: http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2
BuildArch: noarch

Patch4: python-2.6-nowhatsnew.patch
Patch18: python-2.6-extdocmodules.patch

Requires: %{python} = %{version}
%if %{main_python}
Obsoletes: python2-docs
Provides: python2-docs = %{version}
%endif

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: %{python} python-sphinx python-docutils python-jinja
BuildRequires: python-pygments
URL: http://www.python.org/

%description
The python-docs package contains documentation on the Python
programming language and interpreter.  The documentation is provided
in ASCII text files and in LaTeX source files.

Install the python-docs package if you'd like to use the documentation
for the Python language.

%prep
%setup -q -n Python-%{version}

#patch4 -p1 -b .nowhatsnew
%patch18 -p1 -b .extdocmodules

%build
make -C Doc html
#rm html/index.html.in Makefile* info/Makefile tools/sgmlconv/Makefile

%install
rm -fr $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Misc/NEWS  Misc/README Misc/cheatsheet 
%doc Misc/HISTORY Doc/build/html

%changelog
* Fri Jul 31 2009 Jame Antill <james.antill@redhat.com> - 2.6.2-1
- Move to 2.6.2 like python itself.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Roman Rakus <rrakus@redhat.com> - 2.6-4
- Fix import error (#511647)

* Wed May 06 2009 Roman Rakus <rrakus@redhat.com> - 2.6-3
- Spec file cleanup (#226341)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.6-1
- Update to 2.6

* Wed Oct  1 2008 Jame Antill <james.antill@redhat.com> - 2.5.2-1
- Move to 2.5.2 like python itself.

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.5.1-3
- fix license tag

* Mon Feb 11 2008 Jame Antill <james.antill@redhat.com> - 2.5.1-2
- mkdir a build root to keep recent rpm/mock happy.

* Sun Jun 03 2007 Florian La Roche <laroche@redhat.com> - 2.5.1-1
- update to 2.5.1

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

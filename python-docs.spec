%if 0%{?fedora}
%global check_links 1
%else
%global check_links 0
%endif

%{!?__python_ver:%define __python_ver EMPTY}

%if "%{__python_ver}" != "EMPTY"
%define main_python 0
%define python python%{__python_ver}
%else
%define main_python 1
%define python python
%endif

%define pybasever 2.7

Summary: Documentation for the Python programming language
Name: %{python}-docs
# The Version needs to be in-sync with the "python" package:
Version: 2.7.5
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

BuildRequires: %{python} python-sphinx python-docutils
BuildRequires: python-pygments

%if %{check_links}
BuildRequires: linkchecker
%endif

URL: http://www.python.org/

%description
The python-docs package contains documentation on the Python
programming language and interpreter.

Install the python-docs package if you'd like to use the documentation
for the Python language.

%prep
%setup -q -n Python-%{version}

#patch4 -p1 -b .nowhatsnew
%patch18 -p1 -b .extdocmodules

%build
make -C Doc html

# Work around rhbz#670493:
cd Doc/build/html
ln -s py-modindex.html modindex.html

%install
rm -fr $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%check
# Verify that all of the local links work (see rhbz#670493)
#
# (we can't check network links, as we shouldn't be making network connections
# within a build.  Also, don't bother checking the .txt source files; some
# contain example URLs, which don't work)
%if %{check_links}
linkchecker \
  --ignore-url=^mailto: --ignore-url=^http --ignore-url=^ftp \
  --ignore-url=.txt\$ \
  Doc/build/html/index.html
%endif

%files
%defattr(-,root,root,-)
%doc Misc/NEWS  Misc/README Misc/cheatsheet 
%doc Misc/HISTORY Doc/build/html

%changelog
* Fri May 24 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.5-1
- Version 2.7.5.

* Thu Apr 11 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.4-1
- Version 2.7.4.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 23 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-2
- make link checking optional, to avoid needing to pull in linkchecker and
its dependencies (rbhz#823930)

* Fri Apr 13 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-1
- 2.7.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 11 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-2
- fix broken link to "Global Module Index", and add a %%check, verifying the
absence of broken links (rhbz#670493)

* Wed Jun 22 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-1
- 2.7.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 David Malcolm <dmalcolm@redhat.com> - 2.7.1-1
- 2.7.1

* Mon Aug 02 2010 Roman Rakus <rrakus@redhat.com> - 2.7-1
- Update to 2.7

* Sat Mar 20 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-1
- move to 2.6.5: http://www.python.org/download/releases/2.6.5/

* Fri Jan 29 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-3
- fix %%description (bug #559710)

* Fri Oct 30 2009 David Malcolm <dmalcolm@redhat.com> - 2.6.4-2
- update sources for 2.6.4

* Fri Oct 30 2009 David Malcolm <dmalcolm@redhat.com> - 2.6.4-1
- move to 2.6.4
- drop build requirement on python-jinja; python-sphinx requires python-jinja2
(bug 532135)

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

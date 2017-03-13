%{?scl:%scl_package nodejs-nopt}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-nopt
Version:    3.0.6
Release:    3%{?dist}
Summary:    Node.js option parsing
License:    ISC
URL:        https://github.com/isaacs/nopt
Source0:    http://registry.npmjs.org/nopt/-/nopt-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
An option parsing library for Node.js and its package manager (npm).

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/nopt
cp -pr bin lib package.json %{buildroot}%{nodejs_sitelib}/nopt

mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/nopt/bin/nopt.js %{buildroot}%{_bindir}/nopt

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/nopt
%{_bindir}/nopt
%doc README.md LICENSE examples

%changelog
* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.6-3
- Resolves: rhbz#1334856 , fixes wrong license

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.6-2
- Rebuild for rhel6

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 3.0.6-1
- New upstream release

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 3.0.1-3
- New upstream release 3.0.1

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 2.1.2-2
- replace provides and requires with macro

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.2-1
- new upstream release 2.1.2

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-2
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1.1-2
- Add support for software collections

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-1
- new upstream release 2.1.1

* Sun Jan 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.0-3
- fix symlink to nopt script

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.0-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.0-1
- new upstream release 2.0.0
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.10-4
- bring in line with newer module packaging standards

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.10-3
- guard Requires for F17 automatic depedency generation

* Sun Dec 18 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.10-2
- add Group to make EL5 happy

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> 1.0.10-1
- new upstream release

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.6-1
- initial package

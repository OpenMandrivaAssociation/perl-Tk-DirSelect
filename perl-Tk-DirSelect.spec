%define upstream_name       Tk-DirSelect
%define upstream_version 1.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Cross-platform directory selection widget
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Tk)

BuildArch:	noarch

%description
This module provides a cross-platform directory selection widget. For
systems running Microsoft Windows, this includes selection of local and
mapped network drives. A context menu (right-click or <Button3>) allows the
creation, renaming, and deletion of directories while browsing.

Note: Perl/Tk 804 added the 'chooseDirectory' method which uses native
system dialogs where available. (i.e. Windows) If you want a native feel
for your program, you probably want to use that method instead -- possibly
using this module as a fallback for systems with older versions of Tk
installed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.120.0-2mdv2011.0
+ Revision: 655239
- rebuild for updated spec-helper

* Fri Feb 19 2010 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 508046
- update to 1.12

* Sat Jul 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.0-1mdv2010.0
+ Revision: 392114
- import perl-Tk-DirSelect


* Sat Jul 04 2009 cpan2dist 1.11-1mdv
- initial mdv release, generated with cpan2dist


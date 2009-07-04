%define upstream_name       Tk-DirSelect
%define upstream_version    1.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Cross-platform directory selection widget
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(Tk)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*



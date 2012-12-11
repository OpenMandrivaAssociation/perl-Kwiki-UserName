%define upstream_name	 Kwiki-UserName
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Kwiki User Name Plugin 
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Kwiki)
BuildArch:	noarch

%description
Enable user to set their name in the preferences so changes will show they did
it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.0
+ Revision: 403386
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.14-6mdv2009.0
+ Revision: 257521
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.14-5mdv2009.0
+ Revision: 245614
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.14-3mdv2008.1
+ Revision: 122832
- kill re-definition of %%buildroot on Pixel's request


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-3mdv2007.0
- Rebuild

* Mon Apr 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-2mdk
- better sources URL
- better buildrequires syntax

* Mon Apr 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdk 
- first mandriva release


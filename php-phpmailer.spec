%define base_name	phpmailer
%define name		php-%{base_name}
%define version		1.73
%define release		%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Full featured email transfer class for PHP
License:	LGPL
Group:		Development/Other
URL:		http://phpmailer.sourceforge.net/
Source:     http://downloads.sourceforge.net/phpmailer/%{base_name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PHP email transport class featuring multiple file attachments, SMTP servers,
CCs, BCCs, HTML messages, and word wrap, and more. It can send email via
sendmail, PHP mail(), or with SMTP. Methods are based on the popular AspEmail
active server component.

%prep
%setup -q -n phpmailer

# fix encoding
for file in `find . -type f`; do
    perl -pi -e 'BEGIN {exit unless -T $ARGV[0];} s/\r\n$/\n/;' $file
done

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_libdir}/php
install -d -m 755 %{buildroot}%{_libdir}/php/language
install -m 644 *.php %{buildroot}%{_libdir}/php
install -m 644 language/*.php %{buildroot}%{_libdir}/php/language

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog.txt README LICENSE docs/* phpdoc
%{_libdir}/php/language
%{_libdir}/php/*.php




%changelog
* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.73-6mdv2011.0
+ Revision: 679623
- mass rebuild

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 1.73-5mdv2010.0
+ Revision: 397579
- Rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.73-4mdv2009.1
+ Revision: 323035
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.73-3mdv2009.0
+ Revision: 268962
- rebuild early 2009.0 package (before pixel changes)

* Sun May 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.73-2mdv2009.0
+ Revision: 205685
- Should not be noarch ed

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.73-1mdv2008.1
+ Revision: 136417
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.73-1mdv2007.0
+ Revision: 97287
- Import php-phpmailer

* Fri Dec 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.73-1mdv2007.1
- first mdv release


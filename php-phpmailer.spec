%define base_name	phpmailer
%define name		php-%{base_name}
%define version		1.73
%define release		%mkrel 5

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



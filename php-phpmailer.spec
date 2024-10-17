%define base_name	phpmailer

Name:		php-%{base_name}
Version:	5.2.7
Release:	2
Summary:	Full featured email transfer class for PHP
License:	LGPL
Group:		Development/Other
URL:		https://phpmailer.sourceforge.net/
Source:		http://downloads.sourceforge.net/phpmailer/PHPMailer-master.zip
BuildArch:	noarch

%description
PHP email transport class featuring multiple file attachments, SMTP servers,
CCs, BCCs, HTML messages, and word wrap, and more. It can send email via
sendmail, PHP mail(), or with SMTP. Methods are based on the popular AspEmail
active server component.

%prep
%setup -q -n PHPMailer-master

# fix encoding
for file in `find . -type f`; do
    perl -pi -e 'BEGIN {exit unless -T $ARGV[0];} s/\r\n$/\n/;' $file
done

%build

%install
install -d -m 755 %{buildroot}%{_libdir}/php
install -d -m 755 %{buildroot}%{_libdir}/php/language
install -m 644 *.php %{buildroot}%{_libdir}/php
install -m 644 language/*.php %{buildroot}%{_libdir}/php/language

%clean

%files
%doc LICENSE docs/*
%{_libdir}/php/language
%{_libdir}/php/*.php

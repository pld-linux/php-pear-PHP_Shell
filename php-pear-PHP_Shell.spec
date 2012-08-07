%define		status		alpha
%define		pearname	PHP_Shell
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - an interactive PHP Shell like IPython
Summary(pl.UTF-8):	%{pearname} - interaktywna powłoka PHP podobna do IPythona
Name:		php-pear-%{pearname}
Version:	0.3.2
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	ca73ede3157d3e2d8e745daa4439524d
URL:		http://pear.php.net/package/PHP_Shell/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(readline)
Requires:	php(tokenizer)
Requires:	php-common >= 4:5.0.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4
Obsoletes:	php-pear-PHP_Shell-tests
Obsoletes:	php-shell
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP-based implementation of a interactive shell with history,
tab-completion, handling of fatal errors, debugging aid, ...

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Oparta na PHP implementacja interaktywnej powłoki z historią,
dopełnianiem tabem, obsługą błędów krytycznych, pomocą przy usuwaniu
błędów...

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv docs/PHP_Shell/README .
mv .%{php_pear_dir}/examples .
mv .%{php_pear_dir}/data/PHP_Shell/scripts .
mv .%{php_pear_dir}/scripts/* scripts
%{__sed} -i -e '1i#!/usr/bin/php' scripts/php-shell-cmd.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

install -p scripts/php-shell-cmd.php $RPM_BUILD_ROOT%{_bindir}/php-shell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/php-shell
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PHP/Shell.php
%{php_pear_dir}/PHP/Shell

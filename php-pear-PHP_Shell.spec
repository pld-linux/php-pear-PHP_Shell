%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	Shell
%define		_status		alpha
%define		_pearname	PHP_Shell
Summary:	%{_pearname} - an interactive PHP Shell like IPython
Summary(pl):	%{_pearname} - interaktywna pow³oka PHP podobna do IPythona
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	1
License:	MIT
Group:		Development/Languages/PHP
#Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Source0:	http://jan.kneschke.de/projects/php-shell/PHP_Shell-%{version}.tgz
# Source0-md5:	0e5487d675dd7451138c599265a02af7
URL:		http://pear.php.net/package/PHP_Shell/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 4:5.0.0
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.4.0-0.b1
Requires:	php-readline
Requires:	php-tokenizer
Obsoletes:	php-shell
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP-based implementation of a interactive shell with history,
tab-completion, handling of fatal errors, debugging aid, ...

In PEAR status of this package is: %{_status}.

%description -l pl
Oparta na PHP implementacja interaktywnej pow³oki z histori±,
dope³nianiem tabem, obs³ug± b³êdów krytycznych, pomoc± przy usuwaniu
b³êdów...

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
%{__sed} -i -e '1i#!/usr/bin/php' ./%{php_pear_dir}/php-shell-cmd.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

mv $RPM_BUILD_ROOT%{php_pear_dir}/php-shell-cmd.php $RPM_BUILD_ROOT%{_bindir}/php-shell
chmod +x $RPM_BUILD_ROOT%{_bindir}/php-shell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/%{_pearname}/{examples/php-shell-cmd.php,README}
%attr(755,root,root) %{_bindir}/php-shell
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PHP/Shell.php
%dir %{php_pear_dir}/PHP/Shell
%{php_pear_dir}/PHP/Shell/Commands.php
%{php_pear_dir}/PHP/Shell/Extensions.php
%{php_pear_dir}/PHP/Shell/Options.php
%dir %{php_pear_dir}/PHP/Shell/Extensions
%{php_pear_dir}/PHP/Shell/Extensions/Autoload.php
%{php_pear_dir}/PHP/Shell/Extensions/AutoloadDebug.php
%{php_pear_dir}/PHP/Shell/Extensions/Colour.php
%{php_pear_dir}/PHP/Shell/Extensions/ExecutionTime.php
%{php_pear_dir}/PHP/Shell/Extensions/InlineHelp.php
%{php_pear_dir}/PHP/Shell/Extensions/LoadScript.php
%{php_pear_dir}/PHP/Shell/Extensions/Prototypes.php
%{php_pear_dir}/PHP/Shell/Extensions/VerbosePrint.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*

%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	PHP_Shell
Summary:	%{_pearname} - an interactive PHP Shell like IPython
Summary(pl.UTF-8):	%{_pearname} - interaktywna powłoka PHP podobna do IPythona
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	5
License:	MIT
Group:		Development/Languages/PHP
#Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Source0:	http://jan.kneschke.de/projects/php-shell/PHP_Shell-%{version}.tgz
# Source0-md5:	0e5487d675dd7451138c599265a02af7
URL:		http://pear.php.net/package/PHP_Shell/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(readline)
Requires:	php(tokenizer)
Requires:	php-common >= 4:5.0.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4
Obsoletes:	php-shell
Obsoletes:	php-pear-PHP_Shell-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP-based implementation of a interactive shell with history,
tab-completion, handling of fatal errors, debugging aid, ...

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Oparta na PHP implementacja interaktywnej powłoki z historią,
dopełnianiem tabem, obsługą błędów krytycznych, pomocą przy usuwaniu
błędów...

Ta klasa ma w PEAR status: %{_status}.

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

%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	Shell
%define		_status		alpha
%define		_pearname	PHP_Shell

Summary:	%{_pearname} - an interactive PHP Shell like IPython
Summary(pl):	%{_pearname} - interaktywna pow�oka PHP podobna do IPythona
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9812da88473d3952899c8048eca9ff5d
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
Oparta na PHP implementacja interaktywnej pow�oki z histori�,
dope�nianiem tabem, obs�ug� b��d�w krytycznych, pomoc� przy usuwaniu
b��d�w...

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

install usr/bin/php-shell.sh $RPM_BUILD_ROOT%{_bindir}/php-shell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/%{_pearname}/{examples/php-shell-cmd.php,README}
%attr(755,root,root) %{_bindir}/php-shell
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/php-shell-cmd.php
%{php_pear_dir}/PHP/Shell.php
%{php_pear_dir}/PHP/Shell/Commands.php
%{php_pear_dir}/PHP/Shell/Options.php
%{php_pear_dir}/PHP/Shell/Extensions.php
%{php_pear_dir}/PHP/Shell/Extensions/Autoload.php
%{php_pear_dir}/PHP/Shell/Extensions/AutoloadDebug.php
%{php_pear_dir}/PHP/Shell/Extensions/InlineHelp.php
%{php_pear_dir}/PHP/Shell/Extensions/VerbosePrint.php
%{php_pear_dir}/PHP/Shell/Extensions/Colour.php
%{php_pear_dir}/PHP/Shell/Extensions/ExecutionTime.php
%{php_pear_dir}/PHP/Shell/Extensions/Prototypes.php
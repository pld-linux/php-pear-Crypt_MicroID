%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	MicroID
%define		_status		alpha
%define		_pearname	Crypt_MicroID
Summary:	%{_pearname} - PHP MicroID library
Summary(pl.UTF-8):	%{_pearname} - biblioteka PHP MicroID
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	2
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d3516f2e05926c7184dbb530a90c18f7
URL:		http://pear.php.net/package/Crypt_MicroID/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Crypt_MicroID-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides methods needed to generate and verify MicroIDs.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten dostarcza klasę do generowania i weryfikacji MicroID.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Crypt/MicroID
%{php_pear_dir}/Crypt/MicroID.php

%if 0%{?suse_version}
%define         php_confdir %{_sysconfdir}/php5/conf.d
%define         php_extdir      %{_libdir}/php5/extensions
%else
%define         php_confdir %{_sysconfdir}/php.d
%define         php_extdir  %{_libdir}/php/modules
%endif

Name:		php-mincrypt
Version:	0.0.4
Release:	1%{?dist}%{?extra_release}
Summary:	PHP bindings for minCrypt crypto-algorithm library
Source:		http://www.migsoft.net/projects/mincrypt/php-mincrypt-%{version}.tar.gz

Group:		Development/Libraries
License:	LGPLv2+
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	libmincrypt

%if 0%{?suse_version}  
Requires:	php5
%else
Requires:	php
%endif

%description
PHP bindings for minCrypt minimal encryption/decryption system library

%prep
%setup -q -n php-mincrypt-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_bindir}/bin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README
%{php_extdir}/php-mincrypt.so
%config(noreplace) %{php_confdir}/php-mincrypt.ini

%changelog


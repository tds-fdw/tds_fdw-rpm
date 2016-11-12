Name:           postgresql-94-tds_fdw
Version:        1.0.8
Release:        1%{?dist}
Summary:        TDS foreing data wrapper for PostgreSQL 9.4

License:        None
URL:            https://github.com/GeoffMontee/tds_fdw
Source:         https://github.com/GeoffMontee/tds_fdw/archive/v%{version}.tar.gz

Requires:       postgresql94 >= 9.4.1
Requires:       postgresql94-server >= 9.4.1
Requires:       postgresql94-libs >= 9.4.1
Requires:       freetds >= 0.91

BuildRequires:  freetds-devel, postgresql94-devel 
BuildRequires:	automake, gcc-c++

%description
This is a PostgreSQL foreign data wrapper that can connect to databases that
use the Tabular Data Stream (TDS) protocol, such as Sybase databases and
Microsoft SQL server.
.
It does not yet support write operations, as added in PostgreSQL 9.3.

%global debug_package %{nil}

%prep
%setup -q -n tds_fdw-1.0.8


%build
PATH=/usr/pgsql-9.4/bin:$PATH make USE_PGXS=1

%install
rm -rf %{buildroot}
PATH=/usr/pgsql-9.4/bin:$PATH make USE_PGXS=1 install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/doc/%{name}-%{version}
mv %{buildroot}/usr/pgsql-9.5/doc/extension/README.tds_fdw.md %{buildroot}/usr/share/doc/%{name}-%{version}/README.md
rm -rf %{buildroot}/usr/share/doc/pgsql/extension/

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root)/usr/pgsql-9.4/lib/tds_fdw.so
%attr(644, root, root)/usr/pgsql-9.4/share/extension/tds_fdw--1.0.8.sql
%attr(644, root, root)/usr/pgsql-9.4/share/extension/tds_fdw.control
%doc /usr/share/doc/%{name}-%{version}/README.md



%changelog

* Sat Nov 12 2016 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.0.8
- 1.0.8 build from https://github.com/GeoffMontee/tds_fdw

* Thu Jan 07 2016 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.0.7
- 1.0.7 build from https://github.com/GeoffMontee/tds_fdw

* Sun Oct 25 2015 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.0.6
- 1.0.6 build from https://github.com/GeoffMontee/tds_fdw

* Sun Sep 13 2015 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.0.3
- 1.0.3 build from https://github.com/GeoffMontee/tds_fdw

* Sun Sep 13 2015 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.0.2
- 1.0.2 build from https://github.com/GeoffMontee/tds_fdw

* Thu Aug 28 2014 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.0.1
- Initial build of 1.0.1 from https://github.com/GeoffMontee/tds_fdw
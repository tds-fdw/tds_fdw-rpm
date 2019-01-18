Name:           postgresql-11-tds_fdw
Version:        2.0.0
Release:        alpha.3.1%{?dist}
Summary:        TDS foreing data wrapper for PostgreSQL 11

License:        None
URL:            https://github.com/tds-fdw/tds_fdw
Source:         https://github.com/tds-fdw/tds_fdw/archive/v2.0.0-alpha.3.tar.gz

Requires:       postgresql11 >= 11.0
Requires:       postgresql11-server >= 11.0
Requires:       postgresql11-libs >= 11.0
Requires:       freetds >= 0.91

BuildRequires:  gcc
BuildRequires:  freetds-devel
BuildRequires:  make
BuildRequires:  postgresql11-devel
%if 0%{?rhel} >= 7
BuildRequires:  llvm-toolset-7-clang
BuildRequires:  llvm5.0
%endif

%description
This is a PostgreSQL foreign data wrapper that can connect to databases that
use the Tabular Data Stream (TDS) protocol, such as Sybase databases and
Microsoft SQL server.
.
It does not yet support write operations, as added in PostgreSQL 9.3.

%global debug_package %{nil}

%prep
%setup -q -n tds_fdw-2.0.0-alpha.3


%build
PATH=/usr/pgsql-11/bin:$PATH make USE_PGXS=1

%install
rm -rf %{buildroot}
PATH=/usr/pgsql-11/bin:$PATH make USE_PGXS=1 install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/doc/%{name}-%{version}
mv %{buildroot}/usr/pgsql-11/doc/extension/README.tds_fdw.md %{buildroot}/usr/share/doc/%{name}-%{version}/README.md
rm -rf %{buildroot}/usr/share/doc/pgsql/extension/

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root)/usr/pgsql-11/lib/tds_fdw.so
%if 0%{?rhel} >= 7
%attr(644, root, root)/usr/pgsql-11/lib/bitcode/tds_fdw.index.bc
%attr(644, root, root)/usr/pgsql-11/lib/bitcode/tds_fdw/src/deparse.bc
%attr(644, root, root)/usr/pgsql-11/lib/bitcode/tds_fdw/src/options.bc
%attr(644, root, root)/usr/pgsql-11/lib/bitcode/tds_fdw/src/tds_fdw.bc
%endif
%attr(644, root, root)/usr/pgsql-11/share/extension/tds_fdw--2.0.0-alpha.3.sql
%attr(644, root, root)/usr/pgsql-11/share/extension/tds_fdw.control
%doc /usr/share/doc/%{name}-%{version}/README.md



%changelog

* Sat Jan 19 2019 Julio Gonzalez Gil <git@juliogonzalez.es> - 2.0.0-alpha.3.1
- 2.0.0-alpha.3 build from https://github.com/tds-fdw/tds_fdw

* Fri Jan 18 2019 Julio Gonzalez Gil <git@juliogonzalez.es> - 2.0.0-alpha.2.1
- Initial build of 2.0.0-alpha.2 from https://github.com/tds-fdw/tds_fdw
Summary:	Library for access to VPD database
Summary(pl.UTF-8):	Biblioteka dostępu do bazy danych VPD
Name:		libvpd
Version:	2.2.9
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/power-ras/libvpd/tags
Source0:	https://github.com/power-ras/libvpd/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cfcd5ab91b1e78fe409f940797e6d4f6
Patch0:		%{name}-pc.patch
URL:		https://github.com/power-ras/libvpd
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	sqlite3-devel >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libvpd library allows to access a VPD database created by vpdupdate in
the lsvpd package.

%description -l pl.UTF-8
Biblioteka libvpd pozwala na dostep do bazy danych VPD tworzonej przez
program vpdupdate z pakietu lsvpd.

%package devel
Summary:	Header files for libvpd library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvpd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	sqlite3-devel >= 3
Obsoletes:	lsvpd-devel < 1.6

%description devel
Header files for libvpd library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvpd.

%package static
Summary:	Static libvpd library
Summary(pl.UTF-8):	Statyczna biblioteka libvpd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	lsvpd-static < 1.6

%description static
Static libvpd library.

%description static -l pl.UTF-8
Statyczna biblioteka libvpd.

%package cxx
Summary:	C++ interface for access to VPD database
Summary(pl.UTF-8):	Interfejs C++ do dostępu do bazy danych VPD
Group:		Libraries

%description cxx
C++ interface for access to VPD database.

%description cxx -l pl.UTF-8
Interfejs C++ do dostępu do bazy danych VPD.

%package cxx-devel
Summary:	Header files for libvpd_cxx library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvpd_cxx
Group:		Development/Libraries
Requires:	%{name}-cxx = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description cxx-devel
Header files for libvpd_cxx library.

%description cxx-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvpd_cxx.

%package cxx-static
Summary:	Static libvpd_cxx library
Summary(pl.UTF-8):	Statyczna biblioteka libvpd_cxx
Group:		Development/Libraries
Requires:	%{name}-cxx-devel = %{version}-%{release}

%description cxx-static
Static libvpd_cxx library.

%description cxx-static -l pl.UTF-8
Statyczna biblioteka libvpd_cxx.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkgconfig
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvpd*.la
# belongs to lsvpd (rule to trigger running /usr/sbin/vpdupdate)
%{__rm} $RPM_BUILD_ROOT/etc/udev/rules.d/90-vpdupdate.rules

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	cxx -p /sbin/ldconfig
%postun	cxx -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libvpd-2.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvpd-2.2.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvpd.so
%dir %{_includedir}/libvpd-2
%{_includedir}/libvpd-2/*.h
%{_pkgconfigdir}/libvpd-2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvpd.a

%files cxx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvpd_cxx-2.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvpd_cxx-2.2.so.3

%files cxx-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvpd_cxx.so
%{_includedir}/libvpd-2/*.hpp
%{_pkgconfigdir}/libvpd_cxx-2.pc

%files cxx-static
%defattr(644,root,root,755)
%{_libdir}/libvpd_cxx.a

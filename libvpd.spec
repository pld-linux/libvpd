Summary:	Library for access to VPD database
Summary(pl.UTF-8):	Biblioteka dostępu do bazy danych VPD
Name:		libvpd
Version:	2.1.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/linux-diag/%{name}-%{version}.tar.gz
# Source0-md5:	d4e66ec416eac3a87c790cbdc1c628f4
Patch0:		%{name}-pc.patch
URL:		http://linux-diag.sourceforge.net/Lsvpd.html
BuildRequires:	libstdc++-devel
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

%description devel
Header files for libvpd library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvpd.

%package static
Summary:	Static libvpd library
Summary(pl.UTF-8):	Statyczna biblioteka libvpd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

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
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkgconfig
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvpd*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	cxx -p /sbin/ldconfig
%postun	cxx -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libvpd-2.1.so.*.*.*
%ghost %{_libdir}/libvpd-2.1.so.0

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
%attr(755,root,root) %{_libdir}/libvpd_cxx-2.1.so.*.*.*
%ghost %{_libdir}/libvpd_cxx-2.1.so.0

%files cxx-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvpd_cxx.so
%{_includedir}/libvpd-2/*.hpp
%{_pkgconfigdir}/libvpd_cxx-2.pc

%files cxx-static
%defattr(644,root,root,755)
%{_libdir}/libvpd_cxx.a

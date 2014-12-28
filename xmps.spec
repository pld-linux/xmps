#
# Conditional build:
%bcond_without	gnome	# without GNOME support
#
Summary:	X MPEG Player System
Summary(pl.UTF-8):	Odtwarzacz plików MPEG dla X
Name:		xmps
Version:	0.2.0
Release:	5
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	87937db0d26e599003f0e8db4284e16b
Patch0:		%{name}-makefile.patch
BuildRequires:	SDL-devel >= 1.0.8
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
%{?with_gnome:BuildRequires:	gdk-pixbuf-devel >= 0.6.0}
BuildRequires:	gettext-tools
%{?with_gnome:BuildRequires:	gnome-libs-devel}
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	nasm
BuildRequires:	popt-devel
BuildRequires:	smpeg-devel >= 0.4.0
Requires:	SDL >= 1.0.8
%{?with_gnome:Requires:	gdk-pixbuf >= 0.6.0}
Requires:	smpeg >= 0.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMPS stands for X MPEG Player System. It's a simple GTK+ program that
will (hopefully) play MPEG-1 files with sound under the Linux
platform.

%description -l pl.UTF-8
XMPS oznacza X MPEG Player System - Odtwarzacz MPEG dla X. Jest on
prostym programem wykorzystującym GTK+ który (miejmy nadzieję)
odtwarza pliki MPEG z obrazem i dźwiękiem pod Linuksem.

%package devel
Summary:	xmps - header files
Summary(pl.UTF-8):	xmps - pliki nagłówkowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files required for compiling xmps plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe wymagane do budowania wtyczek xmps.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%{__gettextize}
%configure \
	--enable-static=no \
	%{!?with_gnome:--disable-gnome}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	desktopdir=%{_applnkdir}/Multimedia \
	m4datadir=%{_aclocaldir}

%if ! %{with gnome}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install gui/gnome/XMPS.desktop $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
%endif

rm -f $RPM_BUILD_ROOT%{_libdir}/xmps/*{,/*}/lib*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/xmps
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_libdir}/xmps
%dir %{_libdir}/xmps/*
%dir %{_libdir}/xmps/addons/*
%dir %{_libdir}/xmps/codecs/*
%dir %{_libdir}/xmps/renderers/*
%attr(755,root,root) %{_libdir}/xmps/*/lib*.so
%attr(755,root,root) %{_libdir}/xmps/*/*/lib*.so
%{_datadir}/xmps
%{_applnkdir}/Multimedia/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmps-config
%{_libdir}/lib*.la
%{_includedir}/libxmps
%{_aclocaldir}/*.m4

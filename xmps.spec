Summary:	X MPEG Player System
Summary(pl):	Odtwarzacz plików MPEG dla X
Name:		xmps
Version:	0.2.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://xmps.sourceforge.net/sources/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
URL:		http://xmps.sourceforge.net/
Requires:	gdk-pixbuf >= 0.6.0
Requires:	SDL >= 1.0.8
Requires:	smpeg >= 0.4.0
BuildRequires:	nasm
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRequires:	popt-devel
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	gnome-libs-devel
BuildRequires:	smpeg-devel >= 0.4.0
BuildRequires:	SDL-devel >= 1.0.8
BuildRequires:	gdk-pixbuf-devel >= 0.6.0
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XMPS stands for X MPEG Player System. It's a simple Gtk program that
will (hopefully) play MPEG-1 files with sound under the Linux
platform.

%description -l pl
XMPS oznacza X MPEG Player System - Odtwarzacz MPEG dla X. Jest on
prostym programem wykorzystuj±cym Gtk który (miejmy nadziejê) odtwarza
pliki MPEG z obrazem i d¼wiêkiem na Linuksie.

%package devel
Summary:	xmps - header files
Summary(pl):	xmps - pliki nag³ówkowe
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files required for compiling xmps plugins.

%description devel -l pl
Pliki nag³ówkowe wymagane do budowania wtyczek xmps.

%prep
%setup  -q
%patch0 -p1
%build
automake
gettextize --copy --force
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	desktopdir=%{_applnkdir}/Multimedia \
	m4datadir=%{_aclocaldir}

gzip -9nf AUTHORS README ChangeLog NEWS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/xmps
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/xmps
%{_datadir}/xmps
%{_applnkdir}/Multimedia/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmps-config
%{_includedir}/libxmps
%{_libdir}/lib*.la
%{_aclocaldir}/*.m4

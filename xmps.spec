Summary:	X MPEG Player System
Summary(pl):	Odtwarzacz plików MPEG dla X
Name:		xmps
Version:	0.1.3
Release:	1
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
License:	GPL
Source0:	http://www-eleves.enst-bretagne.fr/~chavarri/xmps/sources/%{name}-%{version}.tar.gz
Patch0:		%{name}-0.1.3-destdir.patch
URL:		http://www-eleves.enst-bretagne.fr/~chavarri/xmps/
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
LDFLAGS="-s" ; export LDFLAGS
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
%dir %{_libdir}/xmps
%dir %{_libdir}/xmps/Codecs
%attr(755,root,root) %{_libdir}/xmps/Codecs/*.so
%{_libdir}/xmps/Codecs/*.la
%dir %{_libdir}/xmps/Renderers
%attr(755,root,root) %{_libdir}/xmps/Renderers/*.so
%{_libdir}/xmps/Renderers/*.la
%{_datadir}/xmps
%{_applnkdir}/Multimedia/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmps-config
%{_includedir}/xmps
%{_libdir}/lib*.la
%{_aclocaldir}/*.m4

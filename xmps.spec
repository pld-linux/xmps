Summary:	X MPEG Player System
Summary(pl):	Odtwarzacz plików MPEG dla X
Name:		xmps
Version:	0.1.0
#Version:	cvs
Release:	1
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
License:	GPL
Source0:	http://www-eleves.enst-bretagne.fr/~chavarri/xmps/sources/%{name}-%{version}.tar.gz
URL:		http://www-eleves.enst-bretagne.fr/~chavarri/xmps/
Requires:	gtk+ >= 1.2.2
Requires:	glib >= 1.2.2
Requires:	gdk-pixbuf >= 0.6.0
Requires:	SDL >= 1.0.8
BuildRequires:	nasm
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	gnome-libs-devel
BuildRequires:	smpeg-devel
BuildRequires:	SDL-devel >= 1.0.8
BuildRequires:	gdk-pixbuf-devel >= 0.6.0
BuildRequires:	esound-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XMPS stands for X MPEG Player System. It's a simple Gtk program that will
(hopefully) play MPEG-1 files with sound under the Linux platform.

%description -l pl
XMPS oznacza X MPEG Player System - Odtwarzacz MPEG dla X. Jest on prostym
programem wykorzystuj±cym Gtk który (miejmy nadziejê) odtwarza pliki MPEG z
obrazem i d¼wiêkiem na Linuksie.

%prep
%setup  -q
%build

#export NOCONFIGURE="x"
#./autogen.sh

LDFLAGS="-s" ; export LDFLAGS
%configure 

make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install -d "$RPM_BUILD_ROOT%{_applnkdir}/Multimedia"
install XMPS.desktop "$RPM_BUILD_ROOT%{_applnkdir}/Multimedia"
install xmps.png "$RPM_BUILD_ROOT%{_datadir}/pixmaps"

gzip -9nf AUTHORS README ChangeLog NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/xmps
%dir %{_libdir}/xmps/Codecs
%attr(755,root,root) %dir %{_libdir}/xmps/Codecs/*.so
%{_libdir}/xmps/Codecs/*.la
%dir %{_libdir}/xmps/Renderers
%attr(755,root,root) %{_libdir}/xmps/Renderers/*.so
%{_libdir}/xmps/Renderers/*.la

%dir %{_datadir}/xmps/skins
%{_datadir}/xmps/skins/DarkDepth
%{_datadir}/xmps/skins/default
%{_datadir}/xmps/xmps_intro.xpm

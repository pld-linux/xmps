Summary:	X MPEG Player System
Summary(pl):	Odtwarzacz plików MPEG dla X
Name:		xmps
#Version:	0.1.0
Version:	cvs20000624
Release:	1
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
License:	GPL
Source0:	http://www-eleves.enst-bretagne.fr/~chavarri/xmps/sources/%{name}-%{version}.tar.gz
Patch0:		xmps-DivXMakefile.patch
URL:		http://www-eleves.enst-bretagne.fr/~chavarri/xmps/
Requires:	gdk-pixbuf >= 0.6.0
Requires:	SDL >= 1.0.8
# Requires seeking ability introduced in 0.4.0.
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
%patch0 -p1

%build
NOCONFIGURE="yes" ./autogen.sh

LDFLAGS="-s" ; export LDFLAGS
%configure 

%{__make}

# The AVI/DivX ;) codec.
cd Input/avi
%{__make} OPT_FLAGS="$RPM_OPT_FLAGS"
cd ../..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install -d "$RPM_BUILD_ROOT%{_applnkdir}/Multimedia"
install XMPS.desktop "$RPM_BUILD_ROOT%{_applnkdir}/Multimedia"
install xmps.png "$RPM_BUILD_ROOT%{_datadir}/pixmaps"

gzip -9nf AUTHORS README ChangeLog NEWS TODO

%find_lang %{name}

# The AVI/DivX ;) codec.
install Input/avi/libavi.so "$RPM_BUILD_ROOT%{_libdir}/%{name}/Codecs"

%post
cat <<EOF
NOTE: This program gives possibility to watch "DivX ;)" compressed files.
      But this is probably done with violation of some copyright. Do it on your
      own risk.
      
      To do so, you will need this:
      http://www-eleves.enst-bretagne.fr/~chavarri/xmps/sources/divxc32.dll
      file. Put it into directory you have write access to, and then put path
      to the file into configuration dialog of "AVI Codec (DivX ;))" in
      "preferences" window.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
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
%{_datadir}/xmps/*.xpm
%{_applnkdir}/Multimedia/*
%{_datadir}/pixmaps/*

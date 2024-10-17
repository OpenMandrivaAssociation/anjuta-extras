%define url_ver %(echo %{version}|cut -d. -f1,2)

Name:		anjuta-extras
Version:	3.6.0
Release:	2
Summary:	Extensions for the Anjuta development environment
Source0:	http://download.gnome.org/sources/%name/%{url_ver}/%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Development/Other
Url:		https://anjuta.sourceforge.net/
BuildRequires:  pkgconfig(gthread-2.0) >= 2.16.0
BuildRequires:  pkgconfig(libanjuta-3.0) >= 3.1.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	graphviz-devel
BuildRequires:	binutils-devel
BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires: gcc-c++, gcc, gcc-cpp

Requires:	anjuta >= 3.1.0

%description
Anjuta DevStudio is a versatile Integrated Development Environment (IDE)
on GNOME Desktop Environment and features a number of advanced
programming facilities.

This package contains extensions to Anjuta:
* Profiler
* Sample
* Scintilla Editor
* Scratchbox
* Valgrind Plugin

%prep
%setup -q

%build
export CC=gcc
export CXX=g++
export CFLAGS+=" -fno-strict-aliasing -Wno-error=deprecated-declarations"

%configure2_5x --disable-static
%make

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -exec rm -rf {} \;

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog AUTHORS NEWS
%{_datadir}/glib-2.0/schemas/*.xml
%{_libdir}/anjuta/anjuta-*.plugin
%{_libdir}/anjuta/libanjuta-*.so
%{_datadir}/anjuta/glade/anjuta-*
%dir %{_datadir}/anjuta/properties
%{_datadir}/anjuta/properties/*.properties
%{_datadir}/anjuta/ui/anjuta-sample.ui
%{_datadir}/anjuta/ui/anjuta-scintilla.xml
%{_datadir}/pixmaps/anjuta/anjuta-*
%{_datadir}/gnome/help/anjuta-manual/*/scintilla-plugin.page

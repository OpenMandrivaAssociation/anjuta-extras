%define name anjuta-extras
%define version 2.31.92.0
%define release %mkrel 1

%define anjuta 2.31.91.0

Summary: Extensions for the Anjuta development environment
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Development/Other
Url: http://anjuta.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libanjuta-devel >= %anjuta
BuildRequires: libgnomecanvas2-devel
BuildRequires: graphviz-devel
BuildRequires: binutils-devel
BuildRequires: intltool
#BuildRequires: gnome-common
Requires: anjuta2 >= %anjuta

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
#NOCONFIGURE=yes gnome-autogen.sh

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %buildroot%_libdir/anjuta/*a
%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS NEWS
#README
%_sysconfdir/gconf/schemas/anjuta-editor-scintilla.schemas
%_sysconfdir/gconf/schemas/anjuta-valgrind.schemas
%_libdir/anjuta/anjuta-editor.plugin
%_libdir/anjuta/anjuta-sample.plugin
%_libdir/anjuta/anjuta-scratchbox.plugin
%_libdir/anjuta/anjuta-valgrind.plugin
%_libdir/anjuta/*.so*
%_libdir/anjuta/profiler.plugin
%_datadir/anjuta/glade/*
%_datadir/anjuta/properties/*
%_datadir/anjuta/ui/*
%_datadir/pixmaps/anjuta/*

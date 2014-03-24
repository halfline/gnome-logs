Name:		gnome-logs
Version:	3.12.0
Release:	1%{?dist}
Summary:	A log viewer for the systemd journal

Group:		Applications/System
License:	GPLv3+
URL:		https://wiki.gnome.org/Apps/Logs
Source0:	https://download.gnome.org/sources/gnome-logs/3.12/%{name}-%{version}.tar.xz

BuildRequires:	appdata-tools
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	libxslt
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libsystemd-journal)
Requires:	gsettings-desktop-schemas

%description
A log viewer for the systemd journal.

%prep
%setup -q


%build
%configure
make V=1 %{?_smp_mflags}


%install
%make_install
%find_lang %{name} --with-gnome


%check
make check


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f gnome-logs.lang
%doc AUTHORS COPYING README NEWS
%{_bindir}/gnome-logs
%{_datadir}/appdata/gnome-logs.appdata.xml
%{_datadir}/applications/gnome-logs.desktop
%{_datadir}/icons/hicolor/*/apps/gnome-logs.png
%{_mandir}/man1/gnome-logs.1*


%changelog
* Mon Mar 17 2014 David King <amigadave@amigadave.com> - 3.12.0-1
- Update to 3.12.0

* Mon Mar 17 2014 David King <amigadave@amigadave.com> - 3.11.92-1
- Update to 3.11.92

* Sat Mar 08 2014 David King <amigadave@amigadave.com> - 3.11.91-2
- Use pkgconfig with BuildRequires

* Mon Mar 03 2014 David King <amigadave@amigadave.com> - 3.11.91-1
- Update to 3.11.91

* Tue Feb 18 2014 David King <amigadave@amigadave.com> - 3.11.90-1
- Update to 3.11.90
- Validate the desktop file and AppData using "make check"

* Tue Feb 04 2014 David King <amigadave@amigadave.com> - 3.11.5-1
- Update to 3.11.5

* Tue Dec 17 2013 David King <amigadave@amigadave.com> - 3.11.3-1
- Update to 3.11.3

* Thu Dec 12 2013 David King <amigadave@amigadave.com> - 3.11.2-1
- New package.

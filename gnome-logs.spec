Name:           gnome-logs
Version:        3.13.3
Release:        2%{?dist}
Summary:        Log viewer for the systemd journal

Group:          Applications/System
License:        GPLv3+
URL:            https://wiki.gnome.org/Apps/Logs
Source0:        https://download.gnome.org/sources/%{name}/3.13/%{name}-%{version}.tar.xz
Patch0:         gnome-logs-3.13.3-fix-appdata-desktop.patch

BuildRequires:  appdata-tools
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libxslt
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsystemd-journal)
Requires:       gsettings-desktop-schemas

%description
A log viewer for the systemd journal.

%prep
%setup -q
%patch0 -p1


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


%files -f %{name}.lang
%doc AUTHORS COPYING README NEWS
%{_bindir}/%{name}
%{_datadir}/appdata/
%{_datadir}/applications/org.gnome.Logs.desktop
%{_datadir}/dbus-1/services/org.gnome.Logs.service
%{_datadir}/icons/hicolor/*/apps/gnome-logs.png
%{_mandir}/man1/gnome-logs.1*


%changelog
* Mon Jun 30 2014 David King <amigadave@amigadave.com> - 3.13.3-2
- Fix AppData reference to desktop file

* Mon Jun 23 2014 David King <amigadave@amigadave.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 David King <amigadave@amigadave.com> - 3.13.2-1
- Update to 3.13.2

* Tue Apr 29 2014 David King <amigadave@amigadave.com> - 3.13.1-1
- Update to 3.13.1

* Mon Apr 14 2014 David King <amigadave@amigadave.com> - 3.12.1-1
- Update to 3.12.1

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

Name:           gnome-logs
Version:        3.14.1
Release:        2%{?dist}
Summary:        Log viewer for the systemd journal

Group:          Applications/System
License:        GPLv3+
URL:            https://wiki.gnome.org/Apps/Logs
Source0:        https://download.gnome.org/sources/%{name}/3.14/%{name}-%{version}.tar.xz
# Add HighContrast application icon. Patch from upstream git.
# https://bugzilla.redhat.com/show_bug.cgi?id=1152796
Patch0:         gnome-logs-3.14.1-add-highcontrast-application-icon.patch

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  git
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libxslt
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsystemd-journal)
BuildRequires:  /usr/bin/appstream-util
Requires:       gsettings-desktop-schemas

%description
A log viewer for the systemd journal.

%prep
%setup -q
# Ugly, but necessary as patch does not support git binary diffs.
git apply %{PATCH0}


%build
%configure
make V=1 %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} INSTALL="install -p" install
%find_lang %{name} --with-gnome


%check
make check


%post
touch --no-create %{_datadir}/icons/HighContrast &>/dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/HighContrast &>/dev/null
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/HighContrast &>/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/HighContrast &>/dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%doc AUTHORS COPYING README NEWS
%{_bindir}/%{name}
%{_datadir}/appdata/org.gnome.Logs.appdata.xml
%{_datadir}/applications/org.gnome.Logs.desktop
%{_datadir}/dbus-1/services/org.gnome.Logs.service
%{_datadir}/icons/HighContrast/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/gnome-logs.1*


%changelog
* Wed Oct 15 2014 David King <amigadave@amigadave.com> - 3.14.1-2
- Add HighContrast application icon (#1152796)

* Mon Oct 13 2014 David King <amigadave@amigadave.com> - 3.14.1-1
- Update to 3.14.1

* Tue Sep 23 2014 David King <amigadave@amigadave.com> - 3.14.0-1
- Update to 3.14.0
- Do not own the appdata directory

* Mon Sep 15 2014 David King <amigadave@amigadave.com> - 3.13.92-1
- Update to 3.13.92

* Mon Sep 01 2014 David King <amigadave@amigadave.com> - 3.13.91-1
- Update to 3.13.91

* Mon Aug 18 2014 David King <amigadave@amigadave.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 David King <amigadave@amigadave.com> - 3.13.4-1
- Update to 3.13.4

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

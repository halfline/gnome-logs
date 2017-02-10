Name:           gnome-logs
Version:        3.23.4
Release:        2%{?dist}
Summary:        Log viewer for the systemd journal

License:        GPLv3+
URL:            https://wiki.gnome.org/Apps/Logs
Source0:        https://download.gnome.org/sources/%{name}/3.23/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libxslt
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  /usr/bin/appstream-util
Requires:       gsettings-desktop-schemas

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
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f %{name}.lang
%doc AUTHORS README NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/appdata/org.gnome.Logs.appdata.xml
%{_datadir}/applications/org.gnome.Logs.desktop
%{_datadir}/dbus-1/services/org.gnome.Logs.service
%{_datadir}/glib-2.0/schemas/org.gnome.Logs.*.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/symbolic/apps/%{name}-symbolic.svg
%{_mandir}/man1/gnome-logs.1*


%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 David King <amigadave@amigadave.com> - 3.23.4-1
- Update to 3.23.4

* Mon Dec 12 2016 David King <amigadave@amigadave.com> - 3.23.3-1
- Update to 3.23.3

* Tue Nov 22 2016 David King <amigadave@amigadave.com> - 3.23.2-1
- Update to 3.23.2

* Tue Oct 25 2016 David King <amigadave@amigadave.com> - 3.23.1-1
- Update to 3.23.1

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-2
- Don't set group tags
- Use make_install macro

* Mon Oct 10 2016 David King <amigadave@amigadave.com> - 3.22.1-1
- Update to 3.22.1

* Tue Sep 20 2016 David King <amigadave@amigadave.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 David King <amigadave@amigadave.com> - 3.21.92-1
- Update to 3.21.92

* Tue Aug 16 2016 David King <amigadave@amigadave.com> - 3.21.90-1
- Update to 3.21.90

* Tue Jun 21 2016 David King <amigadave@amigadave.com> - 3.21.3-1
- Update to 3.21.3

* Mon Apr 11 2016 David King <amigadave@amigadave.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 David King <amigadave@amigadave.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 David King <amigadave@amigadave.com> - 3.19.92-1
- Update to 3.19.92

* Mon Feb 29 2016 David King <amigadave@amigadave.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 David King <amigadave@amigadave.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 David King <amigadave@amigadave.com> - 3.19.4-1
- Update to 3.19.4

* Mon Dec 14 2015 David King <amigadave@amigadave.com> - 3.19.3-1
- Update to 3.19.3

* Tue Nov 24 2015 David King <amigadave@amigadave.com> - 3.19.2-1
- Update to 3.19.2

* Mon Oct 26 2015 David King <amigadave@amigadave.com> - 3.19.1-1
- Update to 3.19.1

* Tue Oct 13 2015 David King <amigadave@amigadave.com> - 3.18.1-1
- Update to 3.18.1

* Tue Sep 22 2015 David King <amigadave@amigadave.com> - 3.18.0-1
- Update to 3.18.0

* Tue Sep 01 2015 David King <amigadave@amigadave.com> - 3.17.91-1
- Update to 3.17.91

* Mon Aug 17 2015 David King <amigadave@amigadave.com> - 3.17.90-1
- Update to 3.17.90

* Tue Jul 21 2015 David King <amigadave@amigadave.com> - 3.17.4-1
- Update to 3.17.4

* Mon Jun 22 2015 David King <amigadave@amigadave.com> - 3.17.3-1
- Update to 3.17.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 David King <amigadave@amigadave.com> - 3.17.2-1
- Update to 3.17.2

* Mon Apr 27 2015 David King <amigadave@amigadave.com> - 3.17.1-1
- Update to 3.17.1

* Mon Apr 13 2015 David King <amigadave@amigadave.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 David King <amigadave@amigadave.com> - 3.16.0-1
- Update to 3.16.0

* Mon Mar 16 2015 David King <amigadave@amigadave.com> - 3.15.92-1
- Update to 3.15.92

* Mon Mar 02 2015 David King <amigadave@amigadave.com> - 3.15.91-1
- Update to 3.15.91

* Wed Feb 18 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Use license macro for COPYING

* Mon Jan 19 2015 David King <amigadave@amigadave.com> - 3.15.4-1
- Update to 3.15.4

* Mon Dec 15 2014 David King <amigadave@amigadave.com> - 3.15.3-1
- Update to 3.15.3

* Mon Nov 24 2014 David King <amigadave@amigadave.com> - 3.15.2-1
- Update to 3.15.2

* Tue Oct 28 2014 David King <amigadave@amigadave.com> - 3.15.1-1
- Update to 3.15.1

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

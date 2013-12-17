Name:		gnome-logs
Version:	3.11.3
Release:	1%{?dist}
Summary:	A log viewer for the systemd journal

Group:		Applications/System
License:	GPLv3+
URL:		https://wiki.gnome.org/Apps/Logs
Source0:	http://download.gnome.org/sources/gnome-logs/3.11/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
BuildRequires:	gtk3-devel
BuildRequires:	intltool
BuildRequires:	libxslt
BuildRequires:	systemd-devel
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
%find_lang gnome-logs --with-gnome


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/gnome-logs.desktop


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


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
* Tue Dec 17 2013 David King <amigadave@amigadave.com> - 3.11.3-1
- Update to 3.11.3

* Thu Dec 12 2013 David King <amigadave@amigadave.com> - 3.11.2-1
- New package.

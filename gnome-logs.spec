Name:		gnome-logs
Version:	3.11.2
Release:	1%{?dist}
Summary:	A log viewer for the systemd journal

Group:		Applications/System
License:	GPLv3+
URL:		https://wiki.gnome.org/Apps/Logs
Source0:	http://download.gnome.org/sources/gnome-logs/3.11/%{name}-%{version}.tar.xz
# Fixed with appdata-tools > 0.1.6
Patch0:		gnome-logs-fix-appdata-xml-m4.patch

BuildRequires:	appdata-tools
BuildRequires:	desktop-file-utils
BuildRequires:	gtk3-devel
BuildRequires:	intltool
BuildRequires:	systemd-devel
Requires:	gsettings-desktop-schemas

%description
A log viewer for the systemd journal.

%prep
%setup -q
%patch0 -p1


%build
%configure --disable-maintainer-mode
make V=1 %{?_smp_mflags}


%install
%make_install
%find_lang gnome-logs --with-gnome


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/gnome-logs.desktop


%files -f gnome-logs.lang
%doc AUTHORS COPYING README NEWS
%{_bindir}/gnome-logs
%{_datadir}/appdata/gnome-logs.appdata.xml
%{_datadir}/applications/gnome-logs.desktop


%changelog
* Thu Dec 12 2013 David King <amigadave@amigadave.com> - 3.11.2-1
- New package.

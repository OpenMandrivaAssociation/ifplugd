Summary:	Detect and perform actions when an ethernet cable is (un)plugged
Name:		ifplugd
Version:	0.28
Release:	17
License:	GPLv2
Group:		System/Configuration/Networking
Url:		http://0pointer.de/lennart/projects/ifplugd/
Source0:	http://0pointer.de/lennart/projects/ifplugd/%{name}-%{version}.tar.bz2
Patch0:		ifplugd-0.28-exit-status.patch
Patch1:		ifplugd-0.28-event.patch
Patch2:		ifplugd-0.28-include.patch
Patch3:		ifplugd-0.28-onlink.patch
BuildRequires:	doxygen
BuildRequires:	lynx
BuildRequires:	pkgconfig(libdaemon)

%description
ifplugd is a Linux daemon which will automatically configure your
ethernet device when a cable is plugged in and automatically
unconfigure it if the cable is pulled. This is useful on laptops with
onboard network adapters, since it will only configure the interface
when a cable is really connected.

%prep
%setup -q
%apply_patches

%build
%configure2_5x	--sbindir=/sbin
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_sysconfdir}/init.d/ifplugd

%files
%doc doc/README doc/NEWS doc/README.html doc/style.css LICENSE
%dir %{_sysconfdir}/ifplugd
%config(noreplace) %{_sysconfdir}/ifplugd/ifplugd.conf
%{_sysconfdir}/ifplugd/ifplugd.action
/sbin/ifplugd
/sbin/ifplugstatus
%{_mandir}/man?/ifplugd*
%{_mandir}/man?/ifplugstatus*


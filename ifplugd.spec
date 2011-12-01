Summary:	Detect and perform actions when an ethernet cable is (un)plugged
Name:		ifplugd
Version: 	0.28
Release: 	%mkrel 14
Source0:	http://0pointer.de/lennart/projects/ifplugd/%{name}-%{version}.tar.bz2
Patch0:		ifplugd-0.28-exit-status.patch
Patch1:		ifplugd-0.28-event.patch
Patch2:		ifplugd-0.28-include.patch
Patch3:		ifplugd-0.28-onlink.patch
License:	GPL
Group:		System/Configuration/Networking
URL:		http://0pointer.de/lennart/projects/ifplugd/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	doxygen lynx pkgconfig libdaemon-devel

%description
ifplugd is a Linux daemon which will automatically configure your
ethernet device when a cable is plugged in and automatically
unconfigure it if the cable is pulled. This is useful on laptops with
onboard network adapters, since it will only configure the interface
when a cable is really connected.

%prep
%setup -q
%patch0 -p1 -b .exit-status
%patch1 -p1 -b .event
%patch2 -p1 -b .include
%patch3 -p1 -b .onlink

%build
%configure2_5x	--sbindir=/sbin
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_sysconfdir}/init.d/ifplugd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/README doc/NEWS doc/README.html doc/style.css LICENSE
/sbin/ifplugd
/sbin/ifplugstatus
%{_mandir}/man?/ifplugd*
%{_mandir}/man?/ifplugstatus*
%dir %{_sysconfdir}/ifplugd
%config(noreplace) %{_sysconfdir}/ifplugd/ifplugd.conf
%{_sysconfdir}/ifplugd/ifplugd.action



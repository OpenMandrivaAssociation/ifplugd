Summary:	Detect and perform actions when an ethernet cable is (un)plugged
Name:		ifplugd
Version: 	0.28
Release: 	%mkrel 16
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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/init.d/ifplugd

%clean
rm -rf $RPM_BUILD_ROOT

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




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.28-14mdv2011.0
+ Revision: 665505
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.28-13mdv2011.0
+ Revision: 605973
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.28-12mdv2010.1
+ Revision: 520124
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.28-11mdv2010.0
+ Revision: 425330
- rebuild

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.28-10mdv2009.1
+ Revision: 316762
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.28-9mdv2009.0
+ Revision: 221614
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.28-8mdv2008.1
+ Revision: 170894
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.28-7mdv2008.1
+ Revision: 150284
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Feb 25 2007 Olivier Blin <oblin@mandriva.com> 0.28-6mdv2007.0
+ Revision: 125568
- pass "onlink" argument to ifup/ifdown in ifplugd action script
- bunzip patches
- bunzip patches
- Import ifplugd

* Wed Jul 26 2006 Olivier Blin <blino@mandriva.com> 0.28-5mdv2007.0
- do not abort if mdv-network-event fails

* Fri Jul 21 2006 Olivier Blin <blino@mandriva.com> 0.28-4mdv2007.0
- Patch1: send link up/down events using mdv-network-event
- Patch2: fix include conflict with linux headers by defining __KERNEL_STRICT_NAMES

* Fri Jan 27 2006 Olivier Blin <oblin@mandriva.com> 0.28-3mdk
- remove included libdaemon (thus making Laurent's fix finally valid :-)
- remove man page path workaround
- remove Patch0 (don't workaround unsupported MII, let configuration tools do that)
- simplify Patch1
- remove Patch2 (not needed, /dev/null should be available)

* Fri Jun 24 2005 Laurent MONTEL <lmontel@mandriva.com> 0.28-2mdk
- Fix buildrequires

* Sat Jun 18 2005 Olivier Blin <oblin@mandriva.com> 0.28-1mdk
- 0.28
- libdaemon 0.8
- rediff Patch0, Patch1, Patch2

* Wed Feb 02 2005 Frederic Lepied <flepied@mandrakesoft.com> 0.26-2mdk
- fixed normal startup return code (patch0)

* Sun Dec 19 2004 Mandrakelinux Team <http://www.mandrakeexpert.com> 0.26-1mdk
- New release 0.26

* Sun May 30 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.25-1mdk
- 0.25

* Sun Apr 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.24-1mdk
- 0.24
- libdaemon 0.6
- updated url
- regenerate P2
- fix buildrequires


Summary:	User-space NFSv3 server
Name:		unfs3
Version:	0.9.22
Release:	%mkrel 2
License:	BSD
Group:		System/Servers
URL:		http://sourceforge.net/projects/unfs3/
Source0:	http://prdownloads.sourceforge.net/unfs3/unfs3-%{version}.tar.gz
Source1:	unfs.sysinit
Requires:	rpcbind
Provides:	nfs-server
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
UNFS3 is a user-space implementation of the NFS (Network File System) version 3
server specification. It provides a daemon that supports both the MOUNT and NFS
protocol.

%prep

%setup -q
cp %{SOURCE1} unfs3.init

%build
%configure2_5x
%__make

%install
rm -rf "%{buildroot}"
%makeinstall_std

install -d %{buildroot}%{_initrddir}
install -m0755 unfs3.init %{buildroot}%{_initrddir}/unfs3

%post
%_post_service unfs3

%preun
%_preun_service unfs3

%clean
rm -rf "%{buildroot}"

%files
%attr(-,root,root)
%doc CREDITS README* LICENSE NEWS contrib doc
%{_initrddir}/unfs3
%{_sbindir}/unfsd
%{_mandir}/man7/tags.*
%{_mandir}/man8/unfsd.*


%changelog
* Sun Jul 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.22-2mdv2010.0
+ Revision: 400300
- disable parallel build, it breaks on klodia
- fix dependencies
- spec cleanup

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0.9.22-1mdv2009.1
+ Revision: 332920
- New upstream release

  + Oden Eriksson <oeriksson@mandriva.com>
    - 0.9.21

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.17-3mdv2009.0
+ Revision: 255145
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1mdv2008.1-current
+ Revision: 140924
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Feb 06 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.17-1mdv2007.0
+ Revision: 116603
- Import unfs3

* Tue Feb 06 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.17-1
- 0.9.17

* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.15-1mdk
- initial Mandriva package (mille-xterm import)


Summary:	UNFS3 user-space NFSv3 server
Name:		unfs3
Version:	0.9.17
Release:	%mkrel 1
License:	BSD
Group:		System/Servers
Url:		http://sourceforge.net/projects/unfs3/
Source0:	http://prdownloads.sourceforge.net/unfs3/unfs3-%{version}.tar.bz2
Source1:	unfs.sysinit
Requires:	portmap
Provides:	nfs-server
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRequires:	bison
BuildRequires:	flex

%description
UNFS3 is a user-space implementation of the NFS (Network File System) version 3
server specification. It provides a daemon that supports both the MOUNT and NFS
protocol.

%prep

%setup -q
cp %{SOURCE1} unfs3.init

%build

%configure2_5x

%make

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
%attr(0755,root,root) %{_initrddir}/unfs3
%attr(0755,root,root) %{_sbindir}/unfsd
%attr(0644,root,root) %{_mandir}/man7/tags.*
%attr(0644,root,root) %{_mandir}/man8/unfsd.*



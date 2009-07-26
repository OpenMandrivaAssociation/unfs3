Summary:	UNFS3 user-space NFSv3 server
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
%{_initrddir}/unfs3
%{_sbindir}/unfsd
%{_mandir}/man7/tags.*
%{_mandir}/man8/unfsd.*

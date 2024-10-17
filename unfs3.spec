Summary:	UNFS3 user-space NFSv3 server
Name:		unfs3
Version:	0.9.22
Release:	5
License:	BSD
Group:		System/Servers
Url:		https://sourceforge.net/projects/unfs3/
Source0:	http://prdownloads.sourceforge.net/unfs3/unfs3-%{version}.tar.gz
Source1:	unfs.sysinit
# Based on http://www.spinics.net/lists/linux-nfs/msg05399.html
Patch0:		unfs3-0.9.22-tirpc.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig(libtirpc)
Requires:	rpcbind
Provides:	nfs-server
Requires(post,preun):	rpm-helper

%description
UNFS3 is a user-space implementation of the NFS (Network File System) version 3
server specification. It provides a daemon that supports both the MOUNT and NFS
protocol.

%files
%doc CREDITS README* LICENSE NEWS contrib doc
%{_initrddir}/unfs3
%{_sbindir}/unfsd
%{_mandir}/man7/tags.*
%{_mandir}/man8/unfsd.*

%post
%_post_service unfs3

%preun
%_preun_service unfs3

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
cp %{SOURCE1} unfs3.init

%build
%configure2_5x
make

%install
%makeinstall_std

install -d %{buildroot}%{_initrddir}
install -m0755 unfs3.init %{buildroot}%{_initrddir}/unfs3


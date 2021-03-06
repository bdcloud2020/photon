Summary:        rcpsvc protocol.x files and headers
Name:           rpcsvc-proto
Version:        1.4.2
Release:        1%{?dist}
Source0:        https://github.com/thkukuk/rpcsvc-proto/releases/download/v1.4/rpcsvc-proto-1.4.2.tar.xz
%define sha1    rpcsvc=1730b5812393ea8bee3a1530a41759c181eb8182
License:        LGPLv2+
Group:          System Environment/Libraries
URL:            https://github.com/thkukuk/rpcsvc-proto
Vendor:         VMware, Inc.
Distribution:   Photon
%define BuildRequiresNative rpcsvc-proto

%description
The rpcsvc-proto package contains the rcpsvc protocol.x files and headers,
formerly included with glibc, that are not included in replacement
libtirpc-1.1.4, along with the rpcgen program.

%package    devel
Summary:    Development files for the rpcsvc library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description    devel
This package includes header files and libraries necessary for developing programs which use the rpcsvc library.

%prep
%setup -q

%build
if [ %{_host} != %{_build} ]; then
  # use native rpcgen
  sed -i 's#$(top_builddir)/rpcgen/##' rpcsvc/Makefile.am
fi
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/rpcgen
%{_mandir}/man1/*

%files devel
%{_includedir}/rpcsvc/*

%changelog
* Thu Jul 09 2020 Gerrit Photon <photon-checkins@vmware.com> 1.4.2-1
- Automatic Version Bump
* Thu Nov 15 2018 Alexey Makhalov <amakhalov@vmware.com> 1.4-2
- Cross compilation support
* Fri Sep 21 2018 Alexey Makhalov <amakhalov@vmware.com> 1.4-1
- Initial version

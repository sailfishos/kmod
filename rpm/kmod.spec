Name:       kmod
Summary:    Linux kernel module handling
Version:    29
Release:    1
License:    GPLv2
URL:        https://github.com/sailfishos/kmod
Source0:    %{name}-%{version}.tar.xz
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  libxslt
Provides:   module-init-tools > 3.15
Obsoletes:   module-init-tools <= 3.15

%description
kmod is a set of tools to handle common tasks with Linux kernel modules like
insert, remove, list, check properties, resolve dependencies and aliases.


%package libs
Summary:    Libraries for kmod
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
License: LGPLv2+

%description libs
Libraries for kmod.

%package devel
Summary:    Devel files for libkmod
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libs = %{version}-%{release}

%description devel
Development files for libkmod.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure --disable-static \
    --with-xz \
    --with-zlib --disable-manpages

%make_build

%install
rm -rf %{buildroot}
%make_install

mkdir -p $RPM_BUILD_ROOT/sbin/
ln -sf %{_bindir}/kmod $RPM_BUILD_ROOT/sbin/modprobe
ln -sf %{_bindir}/kmod $RPM_BUILD_ROOT/sbin/modinfo
ln -sf %{_bindir}/kmod $RPM_BUILD_ROOT/sbin/insmod
ln -sf %{_bindir}/kmod $RPM_BUILD_ROOT/sbin/rmmod
ln -sf %{_bindir}/kmod $RPM_BUILD_ROOT/sbin/depmod
ln -sf %{_bindir}/kmod $RPM_BUILD_ROOT/sbin/lsmod

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/depmod.d
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/modprobe.d

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license tools/COPYING
%dir %{_sysconfdir}/depmod.d
%dir %{_sysconfdir}/modprobe.d
%dir %{_prefix}/lib/modprobe.d
%{_bindir}/kmod
/sbin/modprobe
/sbin/modinfo
/sbin/insmod
/sbin/rmmod
/sbin/lsmod
/sbin/depmod
%{_datadir}/bash-completion/completions/kmod

%files libs
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libkmod.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libkmod.h
%{_libdir}/pkgconfig/libkmod.pc
%{_libdir}/libkmod.so

